# All Rights reserved @smdetroja 
import face_recognition
import cv2
import numpy as np
import csv
import os
import datetime

video_capture = cv2.VideoCapture(0)

#importing images and encoding it
#add more portraits manually using below two lines and add photo to photos folder 
sanket_image = face_recognition.load_image_file("photos/BillGates.jpg")
sanket_encoding = face_recognition.face_encodings(sanket_image)

#list all encodings 
known_face_encoding = [ sanket_encoding ]
#list name of all portraits
known_faces_names = ["Bill Gates"]

students = known_faces_names.copy()
#making list variable for storing locations encoding and names 
face_locations = []
face_encodings = []
face_names = []
s = True

#set date and rime for current states 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

#create and open csv file and write name and time when the face was recognised 
f = open(current_data + '.csv', 'w+', newline ='')
inwriter = csv.writer(f)

while True:
    #creating frame to recognise person 
    _,frame = video_capture.read()
    #making small size copy frame camera frame and store as rgb (ed green blue)
    small_frame = cv2.resize(frame,(0,0), fx = 0.25, fy = 0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = fcae_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        #storing names to below list in the time of identification 
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name=""
            face_distance = fcae_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                
            face_names.append(name)
            if name in known_faces_names:
                if name in students: 
                    students.remove(name)
                    print(students)
                    currents_time = now.strftime("%H-%M-%S")
                    inwriter.writerow([name, current_time])
    cv2.imshow("attendence system", fname)
    #by pressing 'q' it will quit the camera 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
#csv file will show data after completion of program
f.close()
