from djitellopy import Tello
import cv2, math
import numpy as np
import jetson.inference
import jetson.utils
from threading import Thread
import time

net = jetson.inference.detectNet("ssd-mobilenet-v1", threshold=0.5) #facenet is working; ssd-mobilenet-v1

drohne = Tello()
drohne.connect()
print(drohne.get_battery())
drohne.streamon()
frame_read = drohne.get_frame_read()
img = frame_read.frame
img = cv2.resize(img, (480, 360)) #360,240 480,360
key = cv2.waitKey(1) & 0xff
	

def move():
	while True:
		if key == 27:
			break
		elif key == ord('t'):
			drohne.takeoff()
		elif key == ord('e'):
			drohne.rotate_clockwise(30)
		elif key == ord('r'):
			drohne.move_up(30)
		elif key == ord('w'):
			drohne.move_forward(30)
		elif key == ord('s'):
			drohne.move_back(30)
		elif key == ord('a'):
			drohne.move_left(30)
		elif key == ord('d'):
			drohne.move_right(30)
		elif key == ord('q'):
			drohne.rotate_counter_clockwise(30)
		elif key == ord('f'):
			drohne.move_down(30)
			
	drohne.land()
	
if __name__ == "__main__":
	t1 = Thread(target = move)
	t1.setDaemon(True)
	t1.start()
	while True:
		img = frame_read.frame
		#img = cv2.resize(img, (480, 360)) #360,240 480,360
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA).astype(np.float32)
		img = jetson.utils.cudaFromNumpy(img)
		detections = net.Detect(img)
		img = jetson.utils.cudaToNumpy(img)
		img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB).astype(np.uint8)
		img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
		cv2.imshow("Drone Surveillance", img)
		key = cv2.waitKey(1) & 0xff
		pass
		
