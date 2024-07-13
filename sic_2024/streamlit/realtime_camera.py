import cv2
import streamlit as st
from ultralytics import YOLO
import time

def app():
    st.header('Object Detection Web App')
    st.subheader('Powered by YOLOv8')
    st.write('Welcome!')
    model = YOLO('yolov8n.pt')
    object_names = list(model.names.values())

    with st.form("my_form"):
        selected_objects = st.multiselect('Choose objects to detect', object_names, default=['person']) 
        min_confidence = st.slider('Confidence score', 0.0, 1.0)
        st.form_submit_button(label='Submit')
    
    stframe = st.empty()
    
    video_stream = cv2.VideoCapture(0)  # Access the built-in camera

    if not video_stream.isOpened():
        st.error("Error: Could not open video device.")
        return

    prev_time = 0
    while True:
        ret, frame = video_stream.read()
        if not ret:
            st.error("Error: Could not read frame.")
            break

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        result = model(frame)
        for detection in result[0].boxes.data:
            x0, y0 = (int(detection[0]), int(detection[1]))
            x1, y1 = (int(detection[2]), int(detection[3]))
            score = round(float(detection[4]), 2)
            cls = int(detection[5])
            object_name = model.names[cls]
            label = f'{object_name} {score}'

            if object_name in selected_objects and score > min_confidence:
                cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 0, 0), 2)
                cv2.putText(frame, label, (x0, y0 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Overlay FPS on the frame
        fps_text = f'FPS: {fps:.2f}'
        cv2.putText(frame, fps_text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        stframe.image(frame, channels="BGR", use_column_width=True)

    video_stream.release()

if __name__ == "__main__":
    app()
