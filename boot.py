import network
import time

SSID = "xyz"       # Your Wi-Fi SSID
PASSWORD = "xyz"  # Your Wi-Fi Password

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
            print(".", end="")
    print("\nConnected to Wi-Fi!")
    print("IP Address:", wlan.ifconfig()[0])

connect_to_wifi()
