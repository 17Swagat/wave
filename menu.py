import customtkinter as ctk
from components import SliderPanel

class Menu(ctk.CTkTabview):
    def __init__(self,parent, mouse_smoothness):
        super().__init__(master=parent,)
        self.grid(row=0, column=0, sticky='news', pady=10, padx=10)
        
        # tabs
        self.add(name='Controls')
        self.add(name='Help')
        self.add(name='Effects')
        self.add(name='Export')
        
        # widgets
        BasicControlsFrame(self.tab('Controls'), mouse_smoothness)
        ColorFrame(self.tab('Help'))
        EffectsFrame(self.tab('Effects'))
        ExportFrame(self.tab('Export'))

class BasicControlsFrame(ctk.CTkFrame):
    def __init__(self, parent, mouse_smoothness):
        super().__init__(master=parent,) #fg_color='white')##303030')
        self.pack(expand=True, fill='both')
        # Components
        SliderPanel(self, text='Mouse smoothness', 
                    data_var=mouse_smoothness,
                    min_value=3, max_value=10)

class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='red')
        self.pack(expand=True, fill='both')

class EffectsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='pink')
        self.pack(expand=True, fill='both')

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='yellow')
        self.pack(expand=True, fill='both')