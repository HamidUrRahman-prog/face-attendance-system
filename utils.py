
import os, csv
from datetime import datetime

ATTENDANCE_FILE = "attendance_log/attendance.csv"

def ensure_dirs():
    os.makedirs("data/known_faces", exist_ok=True)
    os.makedirs("attendance_log", exist_ok=True)
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Date", "Time", "Status"])

def mark_attendance(name):
    today = datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%H:%M:%S")
    already_marked = False
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Name"] == name and row["Date"] == today:
                    already_marked = True
                    break
    if not already_marked:
        with open(ATTENDANCE_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, today, now_time, "Present"])
        return True
    return False

def load_attendance():
    import pandas as pd
    if os.path.exists(ATTENDANCE_FILE):
        return pd.read_csv(ATTENDANCE_FILE)
    return pd.DataFrame(columns=["Name", "Date", "Time", "Status"])
