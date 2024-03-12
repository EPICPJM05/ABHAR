import os
import cv2
import face_recognition
import pyttsx3
from datetime import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to say hello or good morning
def greet_person(name):
    current_hour = datetime.now().hour
    if current_hour < 12:
        engine.say(f"Good morning, {name}!")
    else:
        engine.say(f"Hello, {name}!")
    engine.runAndWait()

# Load known faces and names
known_faces = []
known_names = []

face_know_dir = "Attendence_with_face/data_sets"

# Check if the directory exists
if os.path.exists(face_know_dir):
    for file_name in os.listdir(face_know_dir):
        name = os.path.splitext(file_name)[0]
        image_path = os.path.join(face_know_dir, file_name)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]  # Assuming only one face per image
        known_faces.append(encoding)
        known_names.append(name)
else:
    print("Error: Directory 'face_know' does not exist.")

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame from BGR to RGB (required by face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all the faces and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face matches any known face
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        # Check if any known face is found
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the name below the face
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Greet the person if known
        if name != "Unknown":
            greet_person(name)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
