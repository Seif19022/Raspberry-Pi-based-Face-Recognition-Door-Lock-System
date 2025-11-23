# Raspberry Pi-Based Face Recognition Door Lock System

An intelligent, real-time facial recognition door lock system built using **Raspberry Pi**, **OpenCV**, **DeepFace**, **face_recognition**, and **IoT-based notification features**.  
This project forms the core of my Final Year Project at Multimedia University (2024/2025) and includes advanced features such as:

- 🔐 **Real-time Face Recognition**
- 🤖 **Adaptive Learning** (system improves accuracy over time)
- 👤 **Dynamic Addition of New Users**
- 😊 **Emotion Detection**
- 📢 **IoT Notification System** (sends alerts to a laptop with text-to-speech)
- 💡 **Lighting Adaptation (CLAHE + Gamma Correction)**
- 🔌 **Solenoid Lock Control via GPIO & Relay**

---

## 🚀 Features

### 🔹 **1. Real-Time Face Recognition**
- Uses HOG-based detection + 128-dimensional encodings  
- Recognizes authorized users  
- Rejects unknown users  
- Works at ~564 ms per detection (measured in real test)  
*(Source: Performance tables in the project report, page 100–105 :contentReference[oaicite:0]{index=0})*

---

### 🔹 **2. Adaptive Learning**
The system **updates your face encodings automatically** every time you are detected.  
This solves:
- Appearance changes
- Lighting differences
- Aging differences  
*(Adaptive learning workflow shown in Figures 3.3.14–3.3.19)*

It also allows:
- Adding new users **in real time** by pressing `'a'`  
*(Ref: Figures 4.12–4.14)*

---

### 🔹 **3. Emotion Detection**
Using **DeepFace**, the system can detect:
- happy  
- neutral  
- sad  
- angry  
- fear  
- surprise  
- disgust  

Emotion detection takes ~327 ms on Raspberry Pi.  
*(Table 4.4 in report)*

---

### 🔹 **4. IoT Notification System**
System sends messages to a remote laptop via TCP:
- “Access granted for SEIF!”
- “Unknown face detected!”
- “Detected emotion: Neutral”

Laptop plays audible TTS feedback.  
*(Server/client code shown around page 75–80)*

---

### 🔹 **5. Lighting Adaptation**
Implements:
- CLAHE Histogram Equalization  
- Gamma correction  

Improves detection in:
- low light  
- dim light  
- backlit environments  
*(Figures 3.3.12–3.3.13 show the lighting improvement)*

---

### 🔹 **6. Solenoid Lock Control**
Uses:
- Relay module  
- GPIO 17  
- 12V solenoid lock  

Authorized face → GPIO HIGH → Opens lock for 5 seconds  
*(Hardware diagrams: pages 27–40)*

---

## 📁 Project Structure
│──Simulation.py # Initial laptop-based face recognition simulation
│── noti.py # Notification server (TCP + text-to-speech)
│── final script.txt # Full Raspberry Pi code (facial recognition + lock control)



---

🛠️ Installation & Setup
1. Install dependencies**

pip install opencv-python face_recognition deepface psutil picamera2

2. Enable Raspberry Pi camera
sudo raspi-config


Enable:

Camera Interface

GPIO

3. Run the main script
python3 main.py

4. Run the notification server on laptop
python3 noti.py

🎥 How It Works (Pipeline)

Capture frame from Pi Camera

Apply lighting normalization

Detect face using HOG

Generate 128-D encoding

Compare with saved encodings

If match:

Unlock solenoid lock

Update encoding

Send notification

If unknown:

Show terminal prompt

Optionally add as new user

If emotion detection enabled:

Send emotion info to notification client

📊 Performance Summary
Metric	Value
Average Face Detection Time	564.43 ms
Average Emotion Detection Time	327.63 ms
Recognition Accuracy	96.7%
Notification Delay	~200 ms
Total Frames Processed (test)	180

(All stats are from the official project testing in Chapter 4 of the report.)

🧪 Test Scenarios

The system was tested under:

✔ Bright Light
✔ Low Light
✔ Dim Light
✔ Different Distances
✔ Narrow Angles
✔ Multiple People
✔ Dynamic lighting
✔ Unknown person detection

Figures 4.1–4.7 show real captured frames proving these cases.

🔮 Future Improvements

As proposed in the official project conclusion:

Upgrade to Raspberry Pi 4 for faster processing

Add night-vision / IR camera

Implement anti-spoofing

Build mobile app for remote control

Integrate cloud-based federated learning
(Ref: Section 5.2 in the report)

📜 Academic Reference

This project is documented in the official university report:
“Raspberry Pi-Based Face Recognition Door Lock System”
By Seifeldin Sherif Elnozahy (2025)
Multimedia University

🧑‍💻 Author

Seifeldin Elnozahy
AI & Software Engineer
📩 elnozahyseif2@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/seif-elnozahy
🧑‍🏫 Published in IoT & Face Recognition Research
