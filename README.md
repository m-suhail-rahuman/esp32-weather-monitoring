
## 🌡️ ESP32 Temperature Monitoring with AWS IoT Core  

### 🚀 Overview  
This project demonstrates how an **ESP32** microcontroller collects temperature data and publishes it to **AWS IoT Core** using **MQTT over TLS**. The data can be used for real-time monitoring and visualization in the cloud.  

### 🛠️ Tech Stack  
- **ESP32** (MicroPython)  
- **AWS IoT Core**  
- **MQTT Protocol**  
- **Python**  

## 📌 Features  
✅ **Wi-Fi Connectivity** – ESP32 connects to a wireless network  
✅ **MQTT Messaging** – Secure data transmission to AWS IoT Core  
✅ **TLS Security** – Encrypted communication using certificates  
✅ **Randomized Temperature Data** – Simulating sensor readings  

## 🏗️ Project Setup  

### 1️⃣ Install Required Software  
Ensure you have the following installed:  
- **Thonny IDE** (or any MicroPython-compatible IDE)  
- **MicroPython firmware** flashed on your ESP32  

### 3️⃣ Flash MicroPython to ESP32  
If you haven't installed MicroPython, use:  
```bash
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firmware.bin
```
*(Replace `/dev/ttyUSB0` with your ESP32’s port.)*  

### 4️⃣ Upload Files to ESP32  
Copy the necessary files to ESP32:  
- **boot.py** (Wi-Fi connection)  
- **main.py** (MQTT publisher)  
- **AWS IoT certificates**  

Use **Thonny IDE** or **ampy**:  
```bash
ampy --port /dev/ttyUSB0 put boot.py
ampy --port /dev/ttyUSB0 put main.py
ampy --port /dev/ttyUSB0 put devicecert.crt
ampy --port /dev/ttyUSB0 put private.key
ampy --port /dev/ttyUSB0 put AmazonRootCA1.pem
```

## 📡 Configuration  

### 1️⃣ Update Wi-Fi Credentials  
Edit `boot.py` and replace these:  
```python
SSID = "Your_WiFi"
PASSWORD = "Your_Password"
```

### 2️⃣ Configure AWS IoT Core  
- Create an **AWS IoT Thing** in the **AWS Console**.  
- Download the **Root CA, device certificate, and private key**.  
- Replace the placeholders in `main.py`:  
```python
BROKER_ENDPOINT = "your-aws-endpoint"
CLIENT_ID = "esp32_client"
TOPIC = "temperature"
```

## 🚀 Running the Project  
After uploading the files, restart ESP32:  
```bash
import machine
machine.reset()
```
It should connect to Wi-Fi and start publishing temperature data to AWS IoT Core.  

## 📊 Future Enhancements  
🔹 Add a **DHT11/DHT22** sensor for real-world temperature data  
🔹 Implement **AWS Lambda & DynamoDB** for cloud storage  
🔹 Create a **real-time dashboard** for data visualization  

## 🔗 Resources  
- [MicroPython Docs](https://docs.micropython.org/en/latest/)  
- [AWS IoT MQTT Guide](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html)  
- [ESP32 Getting Started](https://randomnerdtutorials.com/getting-started-with-esp32/)  

## 📬 Let's Connect!  
If you have any suggestions or improvements, feel free to contribute! 🚀  

