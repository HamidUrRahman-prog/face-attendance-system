# 🎓 Real-Time Face Attendance System

> AI-powered attendance system that recognizes faces and logs attendance automatically — no hardware needed, just a camera!

![Python](https://img.shields.io/badge/Python-3.10-blue)
![DeepFace](https://img.shields.io/badge/DeepFace-Latest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![OpenCV](https://img.shields.io/badge/OpenCV-Latest-brightgreen)

---

## 🚀 What it does

- ✅ Register unlimited people with a single photo
- ✅ Detects and recognizes multiple faces in one image
- ✅ Marks attendance only once per person per day
- ✅ Logs attendance with name, date, and timestamp
- ✅ Export full attendance records as CSV

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| DeepFace | Face recognition |
| OpenCV | Face detection |
| Streamlit | Web dashboard |
| Pandas | Data handling |
| Google Colab | Cloud deployment |

---

## ▶️ How to run

### Option 1 — Google Colab (recommended)
Open the notebook and run all cells top to bottom.

### Option 2 — Local
```bash
git clone https://github.com/HamidUrRahman-prog/face-attendance-system
cd face-attendance-system
pip install deepface streamlit opencv-python pandas Pillow tf-keras
streamlit run app.py
```

---

## 📁 Project Structure

```
face_attendance_system/
│
├── app.py              # Streamlit dashboard
├── attendance.py       # Face recognition logic
├── utils.py            # Helper functions
├── data/
│   └── known_faces/    # Registered face images
├── attendance_log/
│   └── attendance.csv  # Auto-generated records
└── README.md
```



## 🔍 What I learned

- How to use DeepFace for real-world face verification
- Building multi-page Streamlit dashboards
- Handling CSV-based data logging
- Deploying AI apps on Google Colab

---

## 👨‍💻 Author

**Hamid Ur Rahman**
- LinkedIn: [hamid-ur-rahman-ai](https://linkedin.com/in/hamid-ur-rahman-ai)
- GitHub: [HamidUrRahman-prog](https://github.com/HamidUrRahman-prog)

---

⭐ Star this repo if you found it useful!
