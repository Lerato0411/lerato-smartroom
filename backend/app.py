from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Data stores
sensor_data = {
    "ldr": 0,
    "pir": 0
}

control_data = {
    "overrideLED": False,
    "led": False,
    "overrideFan": False,
    "analog_output": 0
}

# HTML Dashboard Template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Room Dashboard</title>
    <meta http-equiv="refresh" content="1">
    <style>
        body { font-family: Arial; text-align: center; padding: 30px; background-color: #f8f8f8; }
        h1 { color: #222; }
        .section {
            margin: 20px auto;
            border: 1px solid #ccc;
            padding: 20px;
            width: 400px;
            border-radius: 10px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        p { font-size: 16px; margin: 8px 0; }
    </style>
</head>
<body>
    <h1>Smart Room IoT Dashboard</h1>
    
    <div class="section">
        <h2>Data from ESP32</h2>
        <p><strong>Light Level (LDR):</strong> {{ esp_data['ldr'] }}</p>
        <p><strong>Presence (PIR):</strong> {{ 'YES' if esp_data['pir'] else 'NO' }}</p>
    </div>

    <div class="section">
        <h2>Data from Flet Frontend</h2>
        # <p><strong>Override LED:</strong> {{ 'ON' if flet_data['overrideLED'] else 'OFF' }}</p>
        <p><strong>LED State:</strong> {{ 'ON' if flet_data['led'] else 'OFF' }}</p>
        # <p><strong>Override Fan:</strong> {{ 'ON' if flet_data['overrideFan'] else 'OFF' }}</p>
        <p><strong>Fan Speed:</strong> {{ flet_data['analog_output'] }}</p>
    </div>
</body>
</html>
"""



@app.route('/')
def index():
    return render_template_string(html_template, esp_data=sensor_data, flet_data=control_data)

@app.route('/esp/update', methods=['POST'])
def esp_update():
    data = request.get_json()
    sensor_data['ldr'] = data.get('ldr', 0)
    sensor_data['pir'] = data.get('pir', 0)
    print("ESP32 Sensor Update:", sensor_data)
    return jsonify({'status': 'success'})

@app.route('/esp/control', methods=['GET'])
def esp_control():
    auto_led = sensor_data["ldr"] < 1000 and sensor_data["pir"] == 1
    auto_fan_speed = 180 if sensor_data["pir"] == 1 else 0

    return jsonify({
        "led": control_data["led"] if control_data["overrideLED"] else auto_led,
        "analog_output": control_data["analog_output"] if control_data["overrideFan"] else auto_fan_speed
    })

@app.route('/esp/sensor', methods=['GET'])
def esp_sensor():
    return jsonify(sensor_data)

@app.route('/flet/update', methods=['POST'])
def flet_update():
    data = request.get_json()
    control_data.update({
        "overrideLED": data.get("overrideLED", False),
        "led": data.get("led", False),
        "overrideFan": data.get("overrideFan", False),
        "analog_output": int(data.get("analog_output", 0))
    })
    print("Flet Control Update:", control_data)
    return jsonify({'status': 'updated'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
