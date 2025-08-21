import cv2
import numpy as np
import tensorflow as tf

# Load TensorFlow model for face recognition
model_file = r"C:\Users\sseno\OneDrive\Documents\FYP\best_model.keras"  
model = tf.keras.models.load_model(model_file)

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Flag to track if SEIF face is detected
seif_detected = False

def simulate_door_unlock():
    print("Door is unlocking...")
    # Simulate unlocking by printing a message or waiting
    import time
    time.sleep(2)  # Simulate unlocking delay

def simulate_door_lock():
    print("Door is locking...")
    # Simulate locking by printing a message or waiting
    import time
    time.sleep(1)  # Simulate locking delay

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image from webcam")
            break

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30))

        # Reset SEIF detection flag
        seif_detected = False

        # Process each detected face
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]

            # Preprocess image for model input
            resized_img = cv2.resize(face_img, (224, 224))  # Resize to 224x224
            normalized_img = resized_img.astype('float32') / 255.0
            preprocessed_img = np.expand_dims(normalized_img, axis=0)

            # Make prediction using the loaded model
            prediction_value = model.predict(preprocessed_img)[0][0]

            # Determine label based on prediction threshold
            if prediction_value > 0.4:  # Adjust threshold as needed
                label = "SEIF"
                color = (0, 255, 0)  # Green for SEIF
                seif_detected = True  # Set SEIF detected flag
            else:
                label = "Not SEIF"
                color = (0, 0, 255)  # Red for Not SEIF

            # Draw bounding box around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # Check if SEIF was detected to decide door lock/unlock
        if seif_detected:
            simulate_door_unlock()  # Simulate door unlock
        else:
            simulate_door_lock()  # Simulate door lock

        # Display the resulting frame
        cv2.imshow('Face Recognition', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()
