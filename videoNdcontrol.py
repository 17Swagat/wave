from tkinter import Canvas
import cv2 as cv
from appsettings import *
import mediapipe as mp
import pickle
import numpy as np
from PIL import Image, ImageTk

# mediapipe stuff
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

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

            # new code
            # #############
            self.isHandsDetected, self.handsCount = self.check_hands(frame) # bool, num => e.g-> True, 2
            # if self.isHandsDetected:
            #     if (self.handsCount == 1):
            #         for hand in results.multi_handedness:
            #             # RIGHT-HAND
            #             if hand.classification[0].label == 'Left':
            #                 pass
            #             # LEFT-HAND
            #             elif hand.classification[0].label == 'Right':
            #                 pass
            #         pass
            #     pass

            # #############
            
            # old code
            ########################
            # mediapipe-stuff
            # results = hands.process(frame)
            # if results.multi_hand_landmarks and (len(results.multi_hand_landmarks) == 1):
            #     hand_handedness = results.multi_handedness
            #     for hand in hand_handedness:
            #         # NOTE: RIGHT-HAND!!!
            #         ################################################################ 
            #         if hand.classification[0].label == 'Left':
            #             for hand_landmarks in results.multi_hand_landmarks:
            #                 mp_drawing.draw_landmarks(frame,  
            #                                           hand_landmarks,  
            #                                           mp_hands.HAND_CONNECTIONS,  # hand connections
            #                                           mp_drawing_styles.get_default_hand_landmarks_style(),
            #                                           mp_drawing_styles.get_default_hand_connections_style())
                        
            #             for hand_landmarks in results.multi_hand_landmarks:
            #                 for i in range(len(hand_landmarks.landmark)):
            #                     x = hand_landmarks.landmark[i].x
            #                     y = hand_landmarks.landmark[i].y
            #                     self.x_.append(x)
            #                     self.y_.append(y)
            #                 for i in range(len(hand_landmarks.landmark)):
            #                     x = hand_landmarks.landmark[i].x
            #                     y = hand_landmarks.landmark[i].y
            #                     self.data_aux.append(x - min(self.x_))
            #                     self.data_aux.append(y - min(self.y_))

            #             # BBox coordinates
            #             # 1. top-left
            #             x1 = int(min(self.x_) * W) - 10
            #             y1 = int(min(self.y_) * H) - 10
            #             # 2. bottom-rself.ight
            #             x2 = int(max(self.x_) * W) - 10
            #             y2 = int(max(self.y_) * H) - 10

            #             # Gesture prediction
            #             prediction = model.predict([np.asarray(self.data_aux)])
            #             predicted_label = HANDSIGN[int(prediction[0])]


            #             # bbox
            #             cv.rectangle(frame, 
            #                         (x1, y1), 
            #                         (x2, y2), 
            #                         (0, 0, 0), 
            #                         4)
            #             # predicted-label-text
            #             cv.putText(frame, 
            #                     predicted_label, 
            #                     (x1, y1 - 10), 
            #                     cv.FONT_HERSHEY_SIMPLEX, 
            #                     1.3, (0, 0, 0), 3,cv.LINE_AA)
            
            #         # NOTE: LEFT-HAND
            #         ################################################################ 
            #         elif hand.classification[0].label == 'Right':
            #             # Detected hand is the left hand
            #             # print('LEFT-HAND')
            #             pass
            # ########################

            # Video (with gesture visualization) :=>
            frame = cv.resize(frame, (self.winfo_width(), self.winfo_height()))
            frame_tk = ImageTk.PhotoImage(Image.fromarray(frame))
            self.create_image(0, 0, image=frame_tk, anchor='nw')
            self.img = frame_tk  # Store a reference to prevent garbage collection
        
        self.after(1, self.update_frame)


    def check_hands(self, img):
        results = hands.process(img)
        handsCount = 0
        if results.multi_hand_landmarks:
            # counting hands in the frame
            handsCount = len(results.multi_hand_landmarks) # 1 or 2
            # drawing hands
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing_styles.get_default_hand_landmarks_style(),
                                          mp_drawing_styles.get_default_hand_connections_style())
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    self.x_.append(x)
                    self.y_.append(y)
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    self.data_aux.append(x - min(self.x_))
                    self.data_aux.append(y - min(self.y_))
            
            # BBox coordinates
            # 1. top-left
            H, W, _=  img.shape
            x1 = int(min(self.x_) * W) - 10
            y1 = int(min(self.y_) * H) - 10
            # 2. bottom-rself.ight
            x2 = int(max(self.x_) * W) - 10
            y2 = int(max(self.y_) * H) - 10
            cv.rectangle(img, 
                         (x1, y1), 
                         (x2, y2), 
                         (0, 0, 0), 
                         4)
            
            # predicted-label-text
            # cv.putText(img, 
            #         predicted_label, 
            #         (x1, y1 - 10), 
            #         cv.FONT_HERSHEY_SIMPLEX, 
            #         1.3, (0, 0, 0), 3,cv.LINE_AA)
            
            return True, handsCount

        else:
            # handsCount = 0
            return False, handsCount 