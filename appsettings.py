import pyautogui

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000
SCREEN_WIDTH, SCREEN_HEIGHT  = pyautogui.size()
FUNCTIONING_ON = {'on':True, 'off':False}
SHOW_HANDLANDMARKS = True
DEFAULT_MOUSE_SMOOTHNESS = 4 #10
HANDSIGN = {
    0:  'Fist',               #    OFF
    1:  'Closed-Palm',        #    ON
    2:  'Open-Palm',          # *  WIN + TAB
    3:  'Pointing',           # *  MOUSE POINTING 
    4:  'Point-Right(Thumb)', # *  (WEB): TAB-RIGHT
    5:  'Point-Left(Thumb)',  # *  (WEB): TAB-LEFT
    
    # N eed to remove
    6:  'Close-YO',           #    SCREENSHOT
    7:  'Open-YO',            # *  WIN + D
    
    8:  'Pinky',              #    (ESC)
    9:  'Mouse-Click',        # *  MOUSE-CLICK
    10: 'Thumbs-Up',         # *  (WEB) SCROLL-UP
    11: 'Thumbs-Down',       # *  (WEB) SCROLL-DOWN
}

FRAME_REDUCTION=100

# Colors
BACKGROUND_COLOR='#242424'
WHITE = '#FFF'
GRAY = 'grey'
BLUE = '#1f6aa5'
DARK_GREY = '#4a4a4a'
CLOSE_RED = '#8a0606'
SLIDER_BG = '#64676b' 

# Temporary
plocX, plocY = 0, 0 # previous (X, Y) coordinates (Mouse-Pointer)
clocX, clocY = 0, 0 # current  (X, Y) coordinates (Mouse-Pointer)