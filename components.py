import customtkinter as ctk
from appsettings import *

class ComponentFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', pady=(0, 10), ipadx=8)
        self.font_1 = ctk.CTkFont(family=FONT_1, size=BUTTON_FONT_SIZE+5, weight='bold')
        self.font_2 = ctk.CTkFont(family=FONT_2, size=BUTTON_FONT_SIZE-2, weight='bold')

class SliderPanel(ComponentFrame):
    def __init__(self, parent, text, data_var,
                 min_value, max_value):
        super().__init__(parent=parent)
        
        # layout
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(self, text=text).grid(column=0, row=0, sticky='w', padx=8)
        self.num_label = ctk.CTkLabel(self, text=data_var.get())
        self.num_label.grid(column=1, row=0, sticky='e',padx=8)
        
        ctk.CTkSlider(self, fg_color=SLIDER_BG,
                      variable=data_var,
                      from_=min_value, to=max_value,
                      command=self.update_text).grid(column=0, row=1, columnspan=2, pady=5, padx=5,sticky='we')
    
    def update_text(self, value): 
        self.num_label.configure(text=f'{int(value)}')


class OnOffSwitchPanel(ComponentFrame):
    def __init__(self, 
                 parent, 
                 text, 
                 showVideo,
                 showHandlandmarks, 
                 control_pc):
        super().__init__(parent=parent)
        
        # layout
        self.rowconfigure((0, 1, 2, 3), weight=1)
        self.columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(self, text=text, font=self.font_1).grid(column=0, row=0, sticky='w', padx=8)

        def show_video():
            # print('video :=> ', showVideo.get())
            pass
        ctk.CTkSwitch(master=self, 
                     font=self.font_2,
                     text="WebCam", #ON/OFF", 
                     fg_color=SLIDER_BG,
                    #  progress_color='grey',
                    #  command=lambda: print(data_var.get()),
                    # command=show_video,
                     variable= showVideo,
                     switch_width=38,
                     switch_height=19,
                     onvalue=True, 
                     offvalue=False).grid(column = 0, row=1, pady=8, padx=5, sticky='we')
        
        # def handlandmarks_on_off(self):
        #     FUNCTIONING_ON = not FUNCTIONING_ON
        ctk.CTkSwitch(master=self, 
                     font=self.font_2,
                     text="HandLandmarks",
                     fg_color=SLIDER_BG,
                    #  command= handlandmarks_on_off,#lambda: print(data_var.get()),
                     variable=showHandlandmarks,
                     switch_width=38,
                     switch_height=19,
                     onvalue= True,#"on", 
                     offvalue=False).grid(column = 0, row=2, pady=8, padx=5, sticky='we')

        ctk.CTkSwitch(master=self, 
                     font=self.font_2,
                     text="PC-Control",
                     fg_color=SLIDER_BG,
                    #  command=lambda: print(data_var.get()),
                     variable=control_pc,
                     switch_width=38,
                     switch_height=19,
                     onvalue=True,
                     offvalue=False).grid(column = 0, row=3, pady=8, padx=5, sticky='we')
