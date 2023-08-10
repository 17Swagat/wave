import customtkinter as ctk
from components import *

class Menu(ctk.CTkTabview):
    def __init__(self,parent, mouse_smoothness, video_on_off):
        super().__init__(master=parent,)
        self.grid(row=0, column=0, sticky='news', pady=10, padx=10)
        
        # tabs
        self.add(name='Controls')
        self.add(name='Help')
        # self.add(name='Effects')
        # self.add(name='Export')
        
        # widgets
        ControlsFrame(self.tab('Controls'), mouse_smoothness, video_on_off)
        HelpFrame(self.tab('Help'))

class ControlsFrame(ctk.CTkFrame):
    def __init__(self, parent, mouse_smoothness, video_on_off):
        super().__init__(master=parent,) 
        self.pack(expand=True, fill='both')
        # Components
        # ON_OFF_ButtonPanel(self, text='Video', data_var=video_on_off)
        OnOffSwitchPanel(self, text='Video', 
                    data_var=video_on_off,
                    min_value=3, max_value=10)
        SliderPanel(self, text='Mouse smoothness', 
                    data_var=mouse_smoothness,
                    min_value=3, max_value=10)

class HelpFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='red')
        self.pack(expand=True, fill='both')