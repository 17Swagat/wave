import pyautogui

# FUNCTION CONTROLS
SHOW_VIDEO = True
SHOW_HANDLANDMARKS = True
FUNCTIONING_ON = False # 0 -> Off, 1 -> On


WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000
SCREEN_WIDTH, SCREEN_HEIGHT  = pyautogui.size()
THEME = {
    'Dark': 'dark',
    'Light': 'light',
}
DEFAULT_MOUSE_SMOOTHNESS = 4 #10
HANDSIGN = {
    0:  'DO NOTHING',               #    OFF
    1:  'Closed-Palm',        #    ON
    2:  'WIN + TAB',#'Open-Palm',          # *  WIN + TAB
    3:  'POINTING',           # *  MOUSE POINTING 
    4:  'RIGHT TAB',#'Point-Right(Thumb)', # *  (WEB): TAB-RIGHT
    5:  'LEFT TAB',#'Point-Left(Thumb)',  # *  (WEB): TAB-LEFT
    
    # N eed to remove
    6:  'SCREENSHOT',#'Close-YO',           #    SCREENSHOT
    7:  'MINIMIZE APP',#'Open-YO',            # *  WIN + D
    
    8:  'ESC',              #    (ESC)
    9:  'MOUSE-CLICK',        # *  MOUSE-CLICK
    10: 'SCROLL UP', #'Thumbs-Up',         # *  (WEB) SCROLL-UP
    11: 'SCROLL DOWN', #'Thumbs-Down',       # *  (WEB) SCROLL-DOWN
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

# Font
FONT_1 = 'Calibri'
FONT_2 = 'Helvetica'
BUTTON_FONT_SIZE = 15

# Temporary
plocX, plocY = 0, 0 # previous (X, Y) coordinates (Mouse-Pointer)
clocX, clocY = 0, 0 # current  (X, Y) coordinates (Mouse-Pointer)