import customtkinter as ctk
from appsettings import *
from menu import Menu
from videoNdcontrol import WebCamView

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000


class App(ctk.CTk):
    def __init__(self):
        # ctk settings
        super().__init__()
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.resizable(False, False)
        self.title('Wave')
        self.init_parameters()
        
        # layout
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')
        self.rowconfigure(0, weight=1)

        # cv settings & vid showing
        self.webcamView = WebCamView(self)
        self.menu = Menu(self, self.mouse_smoothness)

        # run
        self.mainloop()
    
    def init_parameters(self):
        self.mouse_smoothness = ctk.IntVar(value=DEFAULT_MOUSE_SMOOTHNESS)
        self.mouse_smoothness.trace('w', self.change_mouse_smoothness)
    
    def change_mouse_smoothness(self, *args):
        pass

# main
if __name__ == '__main__':
    App()
