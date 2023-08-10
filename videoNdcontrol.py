from tkinter import Canvas
import cv2 as cv
from appsettings import *
import mediapipe as mp
import pickle
import numpy as np
from PIL import Image, ImageTk
# from handtrackingModule import HandsDetector
from my_handtrackingmodule import HandsDetector

# mediapipe stuff
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Hand tracking module
detector = HandsDetector() #detectionCon=0.8, maxHands=2)

# prediction model loading
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

class WebCamView(Canvas):
    def __init__(self, parent):
        super().__init__(master=parent, background='#242424', bd=0, highlightthickness=0, relief='ridge')
        self.grid(row=0, column=1, sticky='news')
        
        if FUNCTIONING_ON['on']:
            self.cap = cv.VideoCapture(0)
            self.update_frame()

    def update_frame(self):
        self.data_aux=[]
        self.x_ = []
        self.y_ = []

        ret, frame = self.cap.read()
        H, W, _=  frame.shape

        if ret:
            self.delete('all')
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            # hands detection
            hands, frame = detector.findHands(frame)
            # print(len(hands)) # 0 or 1 or 2
            # print(type(hands)) # list

            # Video (with gesture visualization) :=>
            frame = cv.resize(frame, (self.winfo_width(), self.winfo_height()))
            frame_tk = ImageTk.PhotoImage(Image.fromarray(frame))
            self.create_image(0, 0, image=frame_tk, anchor='nw')
            self.img = frame_tk  # Store a reference to prevent garbage collection
        
        self.after(1, self.update_frame)

