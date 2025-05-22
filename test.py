import cv2
import socket
import pickle
import struct
from picamera2 import Picamera2

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(5)

print("Server is listening...")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} accepted")


picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

try:
    while True:

        frame = picam2.capture_array()
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        data = pickle.dumps(frame_bgr)
        message = struct.pack("Q", len(data)) + data 
        client_socket.sendall(message)

        #cv2.imshow('Server', frame_bgr)
        #if cv2.waitKey(1) == 13:
        #    break
    
except KeyboardInterrupt:
        print("Exiting..")
picam2.release()
client_socket.close()
server_socket.close()
cv2.destroyAllWindows()