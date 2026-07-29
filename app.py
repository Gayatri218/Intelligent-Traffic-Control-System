import streamlit as st
import tempfile
from PIL import Image
from datetime import datetime

from utils.detector import detect_vehicles
from utils.timer import calculate_density, allocate_timers

st.set_page_config(
    page_title="AI Smart Traffic Signal",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 AI-Based Smart Traffic Signal Management System")
st.write("### Intelligent Traffic Density Analysis using YOLOv8")
st.write("📅", datetime.now().strftime("%d-%m-%Y   %H:%M:%S"))

st.divider()

st.subheader("Upload Traffic Images")

col1, col2 = st.columns(2)

with col1:
    road1 = st.file_uploader("🚗 Upload Road 1", type=["jpg", "jpeg", "png"])
    road2 = st.file_uploader("🚗 Upload Road 2", type=["jpg", "jpeg", "png"])

with col2:
    road3 = st.file_uploader("🚗 Upload Road 3", type=["jpg", "jpeg", "png"])
    road4 = st.file_uploader("🚗 Upload Road 4", type=["jpg", "jpeg", "png"])

st.divider()

if st.button("🚦 Analyze Traffic"):

    if None in [road1, road2, road3, road4]:
        st.error("Please upload all four traffic images.")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    roads = [
        ("Road 1", road1),
        ("Road 2", road2),
        ("Road 3", road3),
        ("Road 4", road4)
    ]

    road_scores = []
    emergency_roads = []

    st.header("🚘 Vehicle Detection Results")

    for index, (road_name, uploaded_file) in enumerate(roads):

        status.info(f"Analyzing {road_name}...")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.read())
            image_path = tmp.name

        vehicle_counts, detected_image, emergency_detected, emergency_types = detect_vehicles(image_path)

        score = calculate_density(vehicle_counts)

        road_scores.append((road_name, score))

        if emergency_detected:
            emergency_roads.append(road_name)

        st.subheader(road_name)

        c1, c2 = st.columns(2)

        with c1:
            st.image(
                Image.open(image_path),
                caption="Original Image",
                width="stretch"
            )

        with c2:
            st.image(
                detected_image,
                channels="BGR",
                caption="YOLO Detection",
                width="stretch"
            )

        st.write("### 🚗 Vehicle Count")

        colA, colB, colC, colD = st.columns(4)

        colA.metric("Cars", vehicle_counts["car"])
        colB.metric("Motorcycles", vehicle_counts["motorcycle"])
        colC.metric("Buses", vehicle_counts["bus"])
        colD.metric("Trucks", vehicle_counts["truck"])

        if emergency_detected:
            st.error(f"🚨 Emergency Vehicle Detected: {emergency_types}")
        else:
            st.success("✅ No Emergency Vehicle Detected")
        st.info(f"""
### Density Formula

Density Score =
(Car × 2)
+ (Motorcycle × 1)
+ (Bus × 6)
+ (Truck × 8)

Current Density Score = **{score}**
""")

        progress.progress((index + 1) / 4)

        st.divider()

    status.success("Analysis Completed Successfully ✅")

    priority = allocate_timers(road_scores)

    if emergency_roads:
        priority.sort(
            key=lambda x: (
                x[0] not in emergency_roads,
                -x[1]
            )
        )

    st.header("🚦 Traffic Signal Decision")

    st.table({
        "Road": [x[0] for x in priority],
        "Density Score": [x[1] for x in priority],
        "Green Time (Seconds)": [x[2] for x in priority]
    })

    st.subheader("🚦 Signal Status")

    for i, (road, score, timer) in enumerate(priority):

        if timer == 0:
            st.info(f"⏭️ {road} → No Vehicles (Skipped)")
        elif i == 0:
            st.success(f"🟢 {road} → GREEN SIGNAL ({timer} Seconds)")
        else:
            st.error(f"🔴 {road} → RED SIGNAL")

    st.metric(
        label="🟢 Current Green Signal",
        value=priority[0][0]
    )

    st.metric(
        label="⏱ Allocated Green Time",
        value=f"{priority[0][2]} Seconds"
    )

    