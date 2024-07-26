import cv2
import streamlit as st

def app():
    st.header('Live Camera Stream')
    st.write('Welcome!')

    # Open the default camera
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        st.error("Error: Could not open video stream.")
        return

    # Create a placeholder to display video frames
    frame_placeholder = st.empty()
    stop_button = st.button("Stop Stream")

    while True:
        if stop_button:
            break

        ret, frame = cap.read()
        if not ret:
            st.error("Error: Could not read frame.")
            break

        # Convert the frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in the placeholder
        frame_placeholder.image(frame, channels="RGB")

        # Add a delay to control the frame rate
        cv2.waitKey(1)

    cap.release()

if __name__ == "__main__":
    app()
