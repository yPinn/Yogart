import math
import cv2
import mediapipe as mp
from mediapipe.python.solutions import pose as mp_pose
from threading import Thread, Lock

mp_drawing = mp.solutions.drawing_utils

detection_lock = Lock()
detection_ongoing = False

def calculateAngle(landmark1, landmark2, landmark3):
    x1, y1 = landmark1.x, landmark1.y
    x2, y2 = landmark2.x, landmark2.y
    x3, y3 = landmark3.x, landmark3.y
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360
    return angle

def generate_framesA():
    global detection_ongoing
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    mp_pose_instance = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.3, model_complexity=2)

    while cap.isOpened():
        with detection_lock:
            if not detection_ongoing:
                detection_ongoing = True
                # Start pose detection in a new thread
                detection_thread = Thread(target=pose_detection_thread)
                detection_thread.start()

        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to read frame.")
            break

        green = (0, 255, 0)
        red = (0, 0, 255)

        landmark_drawing_spec = mp_drawing.DrawingSpec(color=red, thickness=2, circle_radius=2)
        
        results = mp_pose_instance.process(frame)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            left_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER],
                                          landmarks[mp_pose.PoseLandmark.LEFT_ELBOW],
                                          landmarks[mp_pose.PoseLandmark.LEFT_WRIST])
    
            right_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST])   
        
            left_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW],
                                                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER],
                                                landmarks[mp_pose.PoseLandmark.LEFT_HIP])

            right_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP],
                                                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER],
                                                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW])

            left_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP],
                                            landmarks[mp_pose.PoseLandmark.LEFT_KNEE],
                                            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE])

            right_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE])
            
            right_back_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_HIP],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE])

            left_back_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER],
                                            landmarks[mp_pose.PoseLandmark.LEFT_HIP],
                                            landmarks[mp_pose.PoseLandmark.LEFT_KNEE])
            
            left_hip_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_KNEE],
                                        landmarks[mp_pose.PoseLandmark.LEFT_HIP],
                                        landmarks[mp_pose.PoseLandmark.RIGHT_HIP])

            # Get the angle between the right hip, knee and ankle points 
            right_hip_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_KNEE],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_HIP],
                                            landmarks[mp_pose.PoseLandmark.LEFT_HIP])

            # Get the angle between the right elbow, right shoulder and left shoulder
            right_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER],
                                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER])

            # Get the angle between the left  elbow, left shoulder and right shoulder
            left_hand_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW],
                                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER],
                                            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER])
        
        
            green_drawing_spec = mp_drawing.DrawingSpec(color=green, thickness=2)
            red_drawing_spec = mp_drawing.DrawingSpec(color=red, thickness=2)
            
            hand_color = red_drawing_spec
            elbow_color = red_drawing_spec
            thigh_color = red_drawing_spec
            calf_color = red_drawing_spec
            body_color = red_drawing_spec
        
            
            if (80 < right_knee_angle < 160 and 160 < left_knee_angle < 200) or (160 < right_knee_angle < 200 and 210 < left_knee_angle < 270) or (80 < right_knee_angle < 160 and 160 < left_knee_angle < 200) or (160 < right_knee_angle < 200 and 210 < left_knee_angle < 270):
                calf_color = green_drawing_spec
            else:
                calf_color = red_drawing_spec
            
            if (120 < right_back_angle < 150 or 120 < left_back_angle < 150):
                thigh_color = green_drawing_spec
            else:
                thigh_color = red_drawing_spec

            if (165 < right_elbow_angle < 195 or 165 < left_elbow_angle < 195):
                hand_color = green_drawing_spec
            else:
                hand_color = red_drawing_spec
            
            if (165 < right_shoulder_angle < 195 or 165 < left_shoulder_angle < 195):
                elbow_color = green_drawing_spec
            else:
                elbow_color = red_drawing_spec
            
            connection_drawing_spec = {}
            
            connection_drawing_spec[(mp_pose.PoseLandmark.LEFT_SHOULDER.value, mp_pose.PoseLandmark.LEFT_ELBOW.value)] = elbow_color
            connection_drawing_spec[(mp_pose.PoseLandmark.RIGHT_SHOULDER.value, mp_pose.PoseLandmark.RIGHT_ELBOW.value)] = elbow_color
            connection_drawing_spec[(mp_pose.PoseLandmark.LEFT_ELBOW.value, mp_pose.PoseLandmark.LEFT_WRIST.value)] = hand_color
            connection_drawing_spec[(mp_pose.PoseLandmark.RIGHT_ELBOW.value, mp_pose.PoseLandmark.RIGHT_WRIST.value)] = hand_color
            connection_drawing_spec[(mp_pose.PoseLandmark.LEFT_HIP.value, mp_pose.PoseLandmark.LEFT_KNEE.value)] = thigh_color
            connection_drawing_spec[(mp_pose.PoseLandmark.RIGHT_HIP.value, mp_pose.PoseLandmark.RIGHT_KNEE.value)] = thigh_color
            connection_drawing_spec[(mp_pose.PoseLandmark.LEFT_KNEE.value, mp_pose.PoseLandmark.LEFT_ANKLE.value)] = calf_color
            connection_drawing_spec[(mp_pose.PoseLandmark.RIGHT_KNEE.value, mp_pose.PoseLandmark.RIGHT_ANKLE.value)] = calf_color
            
            connection_drawing_spec[(6, 8)] = green_drawing_spec
            connection_drawing_spec[(5, 6)] = green_drawing_spec
            connection_drawing_spec[(4, 5)] = green_drawing_spec
            connection_drawing_spec[(0, 4)] = green_drawing_spec
            connection_drawing_spec[(0, 1)] = green_drawing_spec
            connection_drawing_spec[(1, 2)] = green_drawing_spec
            connection_drawing_spec[(2, 3)] = green_drawing_spec
            connection_drawing_spec[(3, 7)] = green_drawing_spec
            connection_drawing_spec[(9, 10)] = green_drawing_spec
            connection_drawing_spec[(11, 12)] = green_drawing_spec
            connection_drawing_spec[(11, 23)] = green_drawing_spec
            connection_drawing_spec[(12, 24)] = green_drawing_spec
            connection_drawing_spec[(23, 24)] = green_drawing_spec
            connection_drawing_spec[(28, 32)] = green_drawing_spec
            connection_drawing_spec[(30, 32)] = green_drawing_spec
            connection_drawing_spec[(28, 30)] = green_drawing_spec
            connection_drawing_spec[(27, 31)] = green_drawing_spec
            connection_drawing_spec[(29, 31)] = green_drawing_spec
            connection_drawing_spec[(27, 29)] = green_drawing_spec
            connection_drawing_spec[(16, 22)] = green_drawing_spec
            connection_drawing_spec[(16, 18)] = green_drawing_spec
            connection_drawing_spec[(18, 20)] = green_drawing_spec
            connection_drawing_spec[(16, 20)] = green_drawing_spec
            connection_drawing_spec[(15, 21)] = green_drawing_spec
            connection_drawing_spec[(15, 17)] = green_drawing_spec
            connection_drawing_spec[(17, 19)] = green_drawing_spec
            connection_drawing_spec[(15, 19)] = green_drawing_spec
        
            landmark_drawing_spec = green_drawing_spec

            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=landmark_drawing_spec,
                connection_drawing_spec=connection_drawing_spec)
            
            cv2.putText(frame, 'Warrior I Pose', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow('Warrior I Pose', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
