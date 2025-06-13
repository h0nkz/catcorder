import io 
import time
import picamera2
import threading
from flask import Flask, Response

app = Flask(__name__)
picam2 = picamera2.Picamera2()
picam2.configure(picamera2.preview_configuration['preview'])
picam2.start()

def generate():
    while True:
        frame = picam2.capture_array()
        # Convert frame to JPEG
        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)