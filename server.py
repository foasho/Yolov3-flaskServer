from flask import Flask, render_template, Response
import threading
import numpy
import cv2, time
from yolo_video import yoloCamera

app = Flask(__name__)

@app.route('/')
def index():
    print('request received')
    return render_template('index.html')

def getStream(yolo_camera):
    while True:
        mainFrame = yolo_camera.getFrame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+mainFrame+b'\r\n\r\n')

@app.route('/getimg')
def getimg():
    yolo_camera_data = yoloCamera()
    return Response(getStream(yolo_camera_data), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True)


