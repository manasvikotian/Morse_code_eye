# USAGE
# python detect_blinks.py --shape-predictor shape_predictor_68_face_landmarks.dat --video blink_detection_demo.mp4
# python detect_blinks.py --shape-predictor shape_predictor_68_face_landmarks.dat

# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
from spellchecker import SpellChecker
spell = SpellChecker()
from tkinter import *
from PIL import ImageTk , Image
import os
root = Tk()
img = ImageTk.PhotoImage(Image.open('images\hospital.jpg'))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
#f = open(r"C:\xampp\htdocs\text.txt", "w")
#f.write(" **Incorrect input** ")
#f.close()
def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])

	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)

	# return the eye aspect ratio
	return ear
#to chech the morse code
def checkKey(lang, key):
    if key in lang.keys():
        print(key ,'= ', lang[key])
    else:
        print('not present')

def checkKey1(hospital, key):
    if key in lang.keys():
        print(key ,'= ', hospital[key])
    else:
        print('not present')
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-v", "--video", type=str, default="",
	help="path to input video file")
args = vars(ap.parse_args())
 
# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold
EYE_AR_THRESH = 0.25
EYE_AR_SHORT = 2
EYE_AR_LONG = 7
EYE_OPEN = 100

# initialize the frame counters and the total number of blinks
COUNTER = 0
COUNT_OPEN = 0
TOTAL_SHORT = 0
TOTAL_LONG = 0

array_count = 0

check = 0
check_open = 0

#print("\nEnter 1 for normal english language")
#print("\nEnter 2 for hospital environment")
#choice = int(input("\n\nEnter the choice : "))

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# start the video stream thread
print("[INFO] starting video stream thread...")
vs = FileVideoStream(args["video"]).start()
fileStream = True
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
fileStream = False
time.sleep(1.0)

#creatin array
import array

arr = [None]*0
ar=''
s=''
go=0
counter=0
# loop over frames from the video stream
while True:
        
	# if this is a file video stream, then we need to check if
	# there any more frames left in the buffer to process
	if fileStream and not vs.more():
		break

	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale
	# channels)
	frame = vs.read()
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale frame
	rects = detector(gray, 0)
        
	# loop over the face detections
	for rect in rects:
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		# extract the left and right eye coordinates, then use the
		# coordinates to compute the eye aspect ratio for both eyes
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)

		# average the eye aspect ratio together for both eyes
		ear = (leftEAR + rightEAR) / 2.0

		# compute the convex hull for the left and right eye, then
		# visualize each of the eyes
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (255, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (255, 255, 0), 1)

		# check to see if the eye aspect ratio is below the blink
		# threshold, and if so, increment the blink frame counter
		if ear < EYE_AR_THRESH:
			COUNTER += 1
			check=1

		# otherwise, the eye aspect ratio is not below the blink
		# threshold
		else:
			# if the eyes were closed for a sufficient number of
			# then increment the total number of blinks
			if ((COUNTER >= EYE_AR_SHORT) and (COUNTER <=EYE_AR_LONG) and (go == 1)):
				TOTAL_SHORT += 1
				print ("\n0")
				check = 0
				if(check==0):
                                        ar1='0'
                                        ar=ar+ar1
                                        array_count+=1
                                        check = 1
                                        counter+=1
			if((COUNTER > EYE_AR_LONG) and (go == 1)):
                                TOTAL_LONG +=1
                                print ("\n1")
                                if(check!=0):
                                        ar1='1'
                                        ar=ar+ar1
                                        array_count+=1
                                        check = 1
                                        counter+=1
			# reset the eye frame counter
			COUNTER = 0

		if ear > EYE_AR_THRESH:
                        COUNT_OPEN +=1
                        check_open=0
                        if((COUNT_OPEN >= EYE_OPEN) and (check_open == 0)):
                                print("\n Break")
                                ar1='B'
                                ar=ar+ar1
                                array_count+=1
                                check_open=1
                                COUNT_OPEN = 0
                                if(ar[0:3:]=='BBB'):
                                        go = 1
                                        tempx=len(ar)
                                        if((ar[:tempx-4:-1]=='BBB') and (counter > 0)):
                                                go=0
                                                hospital={'0':'YES', '00':'NO', '1':'HELP', '11':'PAIN', '01':'Call DOCTOR', '10':'Water', '000':'WATER', '001':'MEDICIN', '010':'Lights'}
                                                ar=ar[3::]
                                                arr = ar.split('BBB')
                                                print(arr)
                                                a=len(arr)-1
                                                i=0
                                                while (i<a):
                                                        key=arr[i]
                                                        if key in hospital.keys():
                                                                print(key ,'= ', hospital[key])
                                                                temp=hospital[key]
                                                                s=s+temp
                                                                f = open("text.txt", "w")
                                                                f.write(temp)
                                                                f.close()
                                                        else:
                                                                print('not present')
                                                        i=i+1

                                                ar=''
                                                go=0
                                                counter=0
		# draw the total number of blinks on the frame along with
		# the computed eye aspect ratio for the frame
		
		cv2.putText(frame, "Blink Count long: {}".format(TOTAL_LONG), (30, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
		cv2.putText(frame, "Blink Count short: {}".format(TOTAL_SHORT), (30, 60),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
		cv2.putText(frame, "Ratio: {:.2f}".format(ear), (300, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (40, 80, 255), 2)
		# show the frame
	
	cv2.imshow("Frame", frame)
	
	key = cv2.waitKey(1) & 0xFF
        
  
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
lang={'01':'A', '1000':'B', '1010':'C', '100':'D', '0':'E', '0010':'F', '110':'G', '0000':'H', '00':'I', '0111':'J', '101':'K', '0100':'L', '11':'M', '10':'N', '111':'O', '0110':'P', '1101':'Q', '010':'R', '000':'S', '1':'T', '001':'U', '0001':'V', '011':'W', '1001':'X', '1011':'Y', '1100':'Z'}
hospital={'0':'YES', '00':'NO', '1':'HELP', '11':'PAIN', '01':'Call DOCTOR', '10':'Water', '000':'WATER', '001':'MEDICIN', '010':'Lights'}

print(ar)
al=''
s=''
choice = 2
'''
if choice == 1:
        arr = ar.split('BB')
        print(arr)
        a=len(arr)-1
        i=0
        temp1=0
        while (i<a):
            arrr= arr[i].split('B')
            print(arrr)
            j=0
            b=len(arrr[j])
            print(b)
            while (j<=b):
                    key=arrr[j]
                    if key in lang.keys():
                        print(key ,'= ', lang[key])
                        temp=lang[key]
                        s=s+temp
                    else:
                        print('not present')
                    j=j+1
            print ("\n\n",s)
            al=al+s
            s=''
            #misspelled = spell.unknown([s])
            #for word in misspelled:
            #        print(spell.correction(word))
            #        print(spell.candidates(word))
            print("\t")
            i=i+1
            al=al+'_'
            print(al)
            '''
if choice == 2:
        arr = ar.split('B')
        print(arr)
        a=len(arr)-1
        i=0
        while (i<a):
                key=arr[i]
                if key in hospital.keys():
                        print(key ,'= ', hospital[key])
                        temp=hospital[key]
                        s=s+temp
                        f = open("text.txt", "w")
                        f.write(al)
                        f.close()

                else:
                        print('not present')
                i=i+1


# do a bit of cleanup

cv2.destroyAllWindows()
vs.stop()

# E A
