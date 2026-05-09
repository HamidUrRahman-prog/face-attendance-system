
import streamlit as st
import numpy as np
from PIL import Image
from datetime import datetime
from attendance import load_known_faces, recognize_faces_in_image, draw_boxes
from utils import ensure_dirs, mark_attendance, load_attendance

ensure_dirs()
st.set_page_config(page_title="Face Attendance", layout="wide", page_icon="🎓")
st.sidebar.title("🎓 Face Attendance")
page = st.sidebar.radio("Navigate", ["📸 Take Attendance", "📋 View Records", "➕ Register Face"])
st.sidebar.caption(f"Today: {datetime.now().strftime('%A, %d %B %Y')}")

@st.cache_resource
def get_known_faces():
    return load_known_faces()

known_faces = get_known_faces()

if page == "📸 Take Attendance":
    st.title("📸 Take Attendance")
    st.info(f"{len(known_faces)} people registered.")
    uploaded = st.file_uploader("Upload a photo", type=["jpg","jpeg","png"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        image_array = np.array(image)
        with st.spinner("Recognizing faces..."):
            results = recognize_faces_in_image(image_array, known_faces)
            annotated = draw_boxes(image_array, results)
        st.image(annotated, use_container_width=True)
        for face in results:
            if face["recognized"]:
                was_new = mark_attendance(face["name"])
                if was_new:
                    st.success(f"✅ Marked present: {face['name']}")
                else:
                    st.info(f"ℹ️ Already marked today: {face['name']}")
        unknowns = sum(1 for f in results if not f["recognized"])
        if unknowns:
            st.warning(f"⚠️ {unknowns} unknown face(s) detected.")

elif page == "📋 View Records":
    st.title("📋 Attendance Records")
    df = load_attendance()
    if df.empty:
        st.info("No records yet.")
    else:
        today = datetime.now().strftime("%Y-%m-%d")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records", len(df))
        col2.metric("Present Today", len(df[df["Date"]==today]))
        col3.metric("Total People", df["Name"].nunique())
        st.dataframe(df.sort_values("Date", ascending=False), use_container_width=True)
        st.download_button("⬇️ Download CSV", df.to_csv(index=False), "attendance.csv")

elif page == "➕ Register Face":
    st.title("➕ Register New Face")
    name = st.text_input("Full name", placeholder="e.g. Hamid Ur Rahman")
    photo = st.file_uploader("Upload clear front-facing photo", type=["jpg","jpeg","png"])
    if st.button("Register", disabled=not (name and photo)):
        image = Image.open(photo).convert("RGB")
        safe_name = name.strip().replace(" ", "_").lower()
        image.save(f"data/known_faces/{safe_name}.jpg")
        st.success(f"✅ {name} registered successfully!")
        st.cache_resource.clear()
