# 🚦 Intelligent Traffic Control System using AI

An AI-powered Intelligent Traffic Control System that uses **YOLOv8** for vehicle detection and dynamically allocates traffic signal timings based on real-time traffic density. The system also supports emergency vehicle prioritization for faster and safer traffic management.

---

## 📌 Features

- 🚗 Detects vehicles using YOLOv8
- 📷 Image-based traffic analysis
- 📊 Calculates traffic density
- ⏱️ Dynamically allocates green signal timings
- 🚑 Emergency vehicle detection and priority support
- 🎯 Simple Streamlit web interface
- ⚡ Fast and efficient AI-based processing

---

## 🛠️ Technologies Used

- Python 3.11+
- Streamlit
- OpenCV
- Ultralytics YOLOv8
- NumPy
- Pillow

---

## 📂 Project Structure

```
SmartTrafficSystem/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── best.pt
│
├── utils/
│   ├── detector.py
│   └── timer.py
│
├── uploads/
│
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Gayatri218/Intelligent-Traffic-Control-System.git
```

### 2. Navigate to the project

```bash
cd Intelligent-Traffic-Control-System
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🚦 How It Works

1. Upload traffic images from different road directions.
2. YOLOv8 detects all vehicles.
3. Vehicle counts are calculated.
4. Traffic density is estimated.
5. Green signal time is allocated dynamically.
6. If an emergency vehicle is detected, that lane receives priority.

---

## 📊 Vehicle Classes Detected

- Car
- Bus
- Truck
- Motorcycle
- Ambulance
- Fire Truck
- Police Vehicle

---

## 📈 Future Improvements

- Live CCTV camera support
- Traffic prediction using Deep Learning
- GPS integration
- IoT-enabled smart traffic lights
- Cloud deployment
- Traffic analytics dashboard
- Automatic violation detection

---

## 📸 Sample Workflow

```
Upload Images
       │
       ▼
YOLOv8 Vehicle Detection
       │
       ▼
Vehicle Counting
       │
       ▼
Traffic Density Calculation
       │
       ▼
Green Signal Time Allocation
       │
       ▼
Emergency Vehicle Priority
```

---

## 📦 Requirements

Install dependencies using

```bash
pip install -r requirements.txt
```

---

## 👩‍💻 Author

**Gayatri Devi**

B.Tech Computer Science and Engineering

Shri Vishnu Engineering College for Women

GitHub: https://github.com/Gayatri218

---

## ⭐ Acknowledgements

- Ultralytics YOLOv8
- OpenCV
- Streamlit
- Python Community

---

## 📜 License

This project is developed for educational and research purposes.
