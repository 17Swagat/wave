import customtkinter as ctk
from components import *

class Menu(ctk.CTkTabview):
    def __init__(self,parent, 
                 mouse_smoothness, 
                 video_on_off,
                 show_handlandmarks,
                 pccontrol):
        
        super().__init__(master=parent,)
        self.grid(row=0, column=0, sticky='news', pady=10, padx=10)
        
        # tabs
        self.add(name='Controls')
        self.add(name='Help')
        
        # widgets
        ControlsFrame(self.tab('Controls'), 
                      mouse_smoothness, 
                      video_on_off,
                      show_handlandmarks,
                      pccontrol)
        HelpFrame(self.tab('Help'))

class ControlsFrame(ctk.CTkFrame):
    def __init__(self, 
                 parent, 
                 mouse_smoothness, 
                 video_on_off,
                 show_handlandmarks,
                 pccontrol):
        
        super().__init__(master=parent,) 
        self.pack(expand=True, fill='both')
        
        # Switches 
        OnOffSwitchPanel(self, text='Video', 
                         showVideo=video_on_off,
                         showHandlandmarks=show_handlandmarks,
                         control_pc=pccontrol)
        
        # Slider
        SliderPanel(self, text='Mouse smoothness', 
                    data_var=mouse_smoothness,
                    min_value=3, max_value=10)

        # Theme change
        font_1 = ctk.CTkFont(family=FONT_1, size=15, weight='bold')
        font_2 = ctk.CTkFont(family=FONT_2, size=BUTTON_FONT_SIZE-2, weight='bold')
        self.appearance_mode_label = ctk.CTkLabel(self,
                                                  text="Theme",
                                                  font=font_1,
                                                  anchor="w").pack(side='left',
                                                                   anchor='sw',
                                                                   padx=5,
                                                                   pady=5)
        theme_strvar = ctk.StringVar(value=THEME['Dark'])
        def combobox_callback(theme):
            ctk.set_appearance_mode(theme)
        theme_box = ctk.CTkComboBox(master=self,
                                   values=[THEME['Dark'], THEME['Light']],
                                   command=combobox_callback,
                                   variable=theme_strvar,)
        theme_box.pack(side='left', anchor='sw',
                       padx=5, pady=5)


class HelpFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='red')
        self.pack(expand=True, fill='both')