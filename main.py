import customtkinter as ctk
from appsettings import *
from menu import Menu
# from videoNdcontrol import WebCamView
from vid_nd_control import WebCamView
from appsettings import *

class App(ctk.CTk):
    def __init__(self):
        # ctk settings
        super().__init__()
        x_offset = int(WINDOW_WIDTH//4) 
        y_offset = int(WINDOW_HEIGHT//4) 
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_offset}+{y_offset}')
        self.resizable(False, False)
        self.title('Wave')
        self.init_parameters()
        
        # layout
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')
        self.rowconfigure(0, weight=1)  

        # cv settings & vid showing
        self.webcamView = WebCamView(self, 
                                     self.mouseSmoothness_var,
                                     self.videoOnOff_var,
                                     self.handlandmarkOnOff_var,
                                     self.pccontrol_var)
        # Menu
        self.menu = Menu(self, 
                         self.mouseSmoothness_var,
                         self.videoOnOff_var,
                         self.handlandmarkOnOff_var,
                         self.pccontrol_var)

        # run
        self.mainloop()
    
    def init_parameters(self):
        
        # initializing tk variables
        # self.videoOnOff_var = ctk.StringVar(value='on')
        self.videoOnOff_var = ctk.BooleanVar(value=True)
        self.handlandmarkOnOff_var = ctk.BooleanVar(value=True)#False)
        self.pccontrol_var = ctk.BooleanVar(value=False)#False)
        self.mouseSmoothness_var = ctk.IntVar(value=DEFAULT_MOUSE_SMOOTHNESS)
        
# main
if __name__ == '__main__':
    App()
