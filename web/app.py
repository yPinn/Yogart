import cv2
import mediapipe as mp

from flask_socketio import SocketIO
from flask import Flask, render_template, Response
from threading import Thread, Lock

from warrior_I_pose import*
from warrior_II_pose import generate_framesB
from downward_facing_dog import generate_frameC
from chair_pose import generate_framesD
from mountain_pose import generate_framesE
from tree_pose import generate_framesF
from triangle_pose import generate_framesG
from half_moon_pose import generate_framesH
from full_boat_pose import generate_framesI
from happy_baby_pose import generate_framesJ



app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

mp_drawing = mp.solutions.drawing_utils
detection_lock = Lock()
detection_ongoing = False

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.3, model_complexity=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/warrior_I_pose')
def run_warrior_I_pose():
    generate_framesA()
    return "Pose detection started."

@app.route('/warrior_II_pose')
def run_warrior_II_pose():
    generate_framesB()
    return "Pose detection started."

@app.route('/downward_facing_dog')
def run_downward_facing_dog():
    generate_frameC()
    return "Pose detection started."

@app.route('/chair_pose')
def run_chair_pose():
    generate_framesD()
    return "Pose detection started."

@app.route('/mountain_pose')
def run_mountain_pose():
    generate_framesE()
    return "Pose detection started."

@app.route('/tree_pose')
def run_tree_pose():
    generate_framesF()
    return "Pose detection started."

@app.route('/triangle_pose')
def run_triangle_pose():
    generate_framesG()
    return "Pose detection started."

@app.route('/half_moon_pose')
def run_half_moon_pose():
    generate_framesH()
    return "Pose detection started."

@app.route('/full_boat_pose')
def run_full_boat_pose():
    generate_framesI()
    return "Pose detection started."

@app.route('/happy_baby_pose')
def run_happy_baby_pose():
    generate_framesJ()
    return "Pose detection started."

@app.route('/yolo')
def run_Yolo():

    import sys
    sys.path.append("../..")

    from yogart.yolov5.detect import run,parse_opt

    opt = parse_opt()
    run(**vars(opt))

    return "Yolov5 started."

if __name__ == "__main__":

    from gevent import pywsgi

    server = pywsgi.WSGIServer(('127.0.0.1',5000),app)
    server.serve_forever()