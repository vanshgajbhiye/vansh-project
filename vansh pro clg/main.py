import cv2
import face_recognition
import time
from black_screen import black_screen   # import black screen

# Load known image
known_image = face_recognition.load_image_file("known.jpeg")
known_encoding = face_recognition.face_encodings(known_image)[0]

cap = cv2.VideoCapture(0)

start_time = time.time()
access = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces([known_encoding], face_encoding)

        if True in match:
            print("✅ Access Granted")
            access = True
            break

    if access:
        break

    # 5 sec timeout
    if time.time() - start_time > 1:
        print("❌ Access Denied")
        break

    cv2.imshow("Scanning...", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# If not matched → black screen
if not access:
    black_screen()


    

    






    





