from tkinter import Canvas
import cv2 as cv
from appsettings import *
import mediapipe as mp
import pickle
import numpy as np
from PIL import Image, ImageTk
import keyboard
import time

# mediapipe stuff
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# prediction model loading
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

class WebCamView(Canvas):
    def __init__(self, parent, 
                 mouse_smoothness,
                 video_on_off,
                 handlandmarks_on_off,
                 pccontrol_on_off):
        super().__init__(master=parent, background='#242424', bd=0, highlightthickness=0, relief='ridge')
        
        self.VIDEOFRAME_WIDTH = self.winfo_width()
        self.VIDEOFRAME_HEIGHT = self.winfo_width()

        self.mouse_smoothness = mouse_smoothness
        
        self.grid(row=0, column=1, sticky='news', padx=40, pady=55)
        
        # if SHOW_VIDEO: 
        if video_on_off.get():
            self.cap = cv.VideoCapture(0)
            self.update_frame()

    def update_frame(self):
        
        self.data_aux=[]
        self.x_ = []
        self.y_ = []

        ret, frame = self.cap.read()
        # H, W, _=  frame.shape

        if ret:
            self.delete('all')
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

            if SHOW_HANDLANDMARKS:
                # bool, num 
                self.isHandsDetected, self.handsCount = self.check_hands(frame) 
            
            # Video (with gesture visualization) :=>
            # if SHOW_VIDEO:
            frame = cv.resize(frame, (self.winfo_width(), self.winfo_height()))
            frame_tk = ImageTk.PhotoImage(Image.fromarray(frame))
            self.create_image(0, 0, image=frame_tk, anchor='nw')
            self.img = frame_tk  # Store a reference to prevent garbage collection
            # else:
            #     pass
        
        self.after(1, self.update_frame)

    def perform_function(self, predicted_handSign):
        pass

    def check_hands(self, img):
        results = hands.process(img)
        handsCount = 0
        
        if results.multi_hand_landmarks\
            and (len(results.multi_hand_landmarks) == 1):
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
            
            # Gesture prediction
            prediction = model.predict([np.asarray(self.data_aux)])
            predicted_label = HANDSIGN[int(prediction[0])]
            # predicted-label-text
            cv.putText(img, 
                    predicted_label, 
                    (x1, y1 - 10), 
                    cv.FONT_HERSHEY_SIMPLEX, 
                    1.3, (0, 0, 0), 3,cv.LINE_AA)
            
            # FUNCTIONING_ON = False
            if (FUNCTIONING_ON):

                # self.perform_function(predicted_handSign=predicted_label)
                
                # DO-NOTHING
                # FIST
                if predicted_label == HANDSIGN[0]:
                    print('Fist')
                
                elif predicted_label == HANDSIGN[1]:
                    print('Closed-Palm')
                
                # WIN + TAB
                # OPEN-PALM
                elif predicted_label == HANDSIGN[2]:
                    print('Open-Palm')
                    keyboard.press('win')
                    time.sleep(0.2)  # Delay for a smooth transition
                    keyboard.press_and_release('tab')
                    keyboard.release('win')
                    time.sleep(0.2)  # Delay for a smooth transition
                
                # MOUSE-POINTER
                # POINTING
                elif predicted_label == HANDSIGN[3]:
                    print('Pointing')
                    
                    # Getting RHand-INDEX'S-TIP
                    x1 = int(hand_landmarks.landmark[8].x * W)  # x-coordinate of index finger tip
                    y1 = int(hand_landmarks.landmark[8].y * H)  # y-coordinate of index finger tip

                    # Draw a circle at the index finger tip
                    cv.circle(img, (x1, y1), 10, (0, 0, 255), cv.FILLED)
                    
                    # MATHS (SETTING-COORDINATES FOR THE MOUSE-POINTER)
                    x_mouse = np.interp(x1, 
                                (FRAME_REDUCTION, 640 - FRAME_REDUCTION),
                                (0, SCREEN_WIDTH))
                    # y-1
                    # y_mouse = np.interp(y1, 
                    #                     (FRAME_REDUCTION, CV_WIN_HEIGHT - FRAME_REDUCTION),
                    #                     (0, SCREEN_HEIGHT))
                    
                    # y-2
                    # Adjusting for the taskbar's height by subtracting a value
                    
                    y_adjustment = 100  # Adjust this value based on the taskbar's height
                    y_mouse = np.interp(y1, 
                                        # (FRAME_REDUCTION, WINDOW_HEIGHT - FRAME_REDUCTION - y_adjustment), (0, SCREEN_HEIGHT))
                                        (FRAME_REDUCTION, 480 - FRAME_REDUCTION - y_adjustment), (0, SCREEN_HEIGHT))
                    
                    # SMOOTHENING-MOUSE-MOVEMENT-COORDINATES
                    global clocX, plocX, clocY, plocY
                    clocX = plocX + (x_mouse - plocX) / self.mouse_smoothness.get() 
                    clocY = plocY + (y_mouse - plocY) / self.mouse_smoothness.get() 

                    # print(x1, y1)
                    
                    if (abs(clocX - plocX) < 5):
                        plocX, plocY = clocX, clocY
                        # continue
                    elif (abs(clocY - plocY) < 5):
                        plocX, plocY = clocX, clocY
                        # continue
                    else:
                        # MOUSE-POINTER-MOVEMENT
                        pyautogui.moveTo(SCREEN_WIDTH - clocX, 
                                    clocY)
                    
                    plocX, plocY = clocX, clocY
                
                # GOTO: RIGHT TAB
                # THUMB-RIGHT
                elif predicted_label == HANDSIGN[4]:
                    print('Point-Right(Thumb)')
                    keyboard.press_and_release('ctrl+tab')
                    time.sleep(0.6)  # Delay for a smooth transition
                
                # GOTO: LEFT TAB
                # THUMB-LEFT
                elif predicted_label == HANDSIGN[5]:
                    print('Point-Left(Thumb)')
                    keyboard.press_and_release('ctrl+shift+tab')
                    time.sleep(0.6)  # Delay for a smooth transition
                
                # SCREENSHOT
                # CLOSED-YO
                elif predicted_label == HANDSIGN[6]:
                    print('Close-YO')
                    keyboard.press('win')
                    time.sleep(0.2)  # Delay for a smooth transition
                    keyboard.press_and_release('shift+s')
                    keyboard.release('win')
                    time.sleep(0.2)  # Delay for a smooth transition
                
                # MINIMIZE
                # OPEN-YO
                elif predicted_label == HANDSIGN[7]:
                    print('Open-YO')
                    keyboard.press('win')
                    time.sleep(0.1)  
                    keyboard.press_and_release('d')
                    keyboard.release('win')
                    time.sleep(0.5)
                
                # ESC
                # PINKY
                elif predicted_label == HANDSIGN[8]:
                    print('Pinky')
                    keyboard.press_and_release('esc')
                    time.sleep(0.6)  # Delay for a smooth transition
                
                elif predicted_label == HANDSIGN[9]:
                    print('Mouse-Click')
                     # print('click!!')
                    x1 = int(hand_landmarks.landmark[8].x * W)  # x-coordinate of index finger tip
                    y1 = int(hand_landmarks.landmark[8].y * H)  # y-coordinate of index finger tip
                    cv.circle(img, (x1, y1), 15, (0, 255, 0), cv.FILLED)
                    # time.sleep(0.2)
                    pyautogui.click() # Left-click
                    # time.sleep(0.4)
                
                # (WEB) SCROLL-UP
                # THUMBS-UP
                elif predicted_label == HANDSIGN[10]:
                    print('Thumbs-Up')
                    keyboard.press('up')
                
                # (WEB) SCROLL-DOWN
                # THUMBS-DOWN
                elif predicted_label == HANDSIGN[11]:
                    print('Thumbs-Down')
                    keyboard.press('down')
                
                else:
                    print('None')
                pass
            
            return True, handsCount

        else:
            # handsCount = 0
            return False, handsCount 