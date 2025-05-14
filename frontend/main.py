import flet as ft
import requests

BACKEND_URL = "http://localhost:5000"

def main(page: ft.Page):
    page.title = "Smart Room Controller"
    page.scroll = "AUTO"

    ldr_display = ft.Text("LDR: -")
    pir_display = ft.Text("PIR: -")

    override_led = ft.Switch(label="Override LED")
    led_control = ft.Switch(label="LED ON")
    override_fan = ft.Switch(label="Override Fan")
    fan_speed = ft.Slider(min=0, max=255, divisions=51, label="Fan Speed", value=0)

    def send_control_data(_=None):
        try:
            requests.post(f"{BACKEND_URL}/flet/update", json={
                "overrideLED": override_led.value,
                "led": led_control.value,
                "overrideFan": override_fan.value,
                "analog_output": int(fan_speed.value)
            })
        except Exception as e:
            print("Error sending control data:", e)

    # Bind controls
    for control in [override_led, led_control, override_fan, fan_speed]:
        control.on_change = send_control_data

    def poll_sensors():
        try:
            res = requests.get(f"{BACKEND_URL}/esp/sensor").json()
            ldr_display.value = f"LDR: {res['ldr']}"
            pir_display.value = f"PIR: {'Motion' if res['pir'] else 'No Motion'}"
            page.update()
        except Exception as e:
            print("Error polling sensor data:", e)

    page.add(ft.Column([
        ft.Text("Smart Room Dashboard", size=24, weight="bold"),
        ldr_display,
        pir_display,
        override_led,
        led_control,
        override_fan,
        fan_speed
    ], spacing=10))

    page.run_thread(poll_sensors, interval=3000)

ft.app(target=main)
