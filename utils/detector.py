from ultralytics import YOLO

# Vehicle counting model
vehicle_model = YOLO("yolov8n.pt")

# Emergency vehicle model
emergency_model = YOLO("models/best.pt")

# COCO classes
CLASS_MAP = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck"
}


def detect_vehicles(image_path):

    # Vehicle detection
    vehicle_results = vehicle_model(image_path)

    vehicle_counts = {
        "car": 0,
        "motorcycle": 0,
        "bus": 0,
        "truck": 0
    }

    for box in vehicle_results[0].boxes:
        cls = int(box.cls[0])
        if cls in CLASS_MAP:
            vehicle_counts[CLASS_MAP[cls]] += 1

    # Emergency detection
    emergency_results = emergency_model(image_path, conf=0.25)

    emergency_detected = False
    emergency_types = []

    EMERGENCY_CLASSES = [
        "ambulance",
        "ambulance_108",
        "ambulance_SOL",
        "ambulance_lamp",
        "ambulance_text",
        "fire_truck",
        "fireladder",
        "firesymbol",
        "firewriting",
        "police",
        "police_lamp",
        "police_lamp_ON"
    ]

    for box in emergency_results[0].boxes:
        cls = int(box.cls[0])
        label = emergency_results[0].names[cls]

        if label in EMERGENCY_CLASSES:
            emergency_detected = True

            if label not in emergency_types:
                emergency_types.append(label)

    if emergency_detected:
        annotated_image = emergency_results[0].plot()
    else:
        annotated_image = vehicle_results[0].plot()

    return (
        vehicle_counts,
        annotated_image,
        emergency_detected,
        emergency_types
    )