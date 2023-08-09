import customtkinter as ctk
from appsettings import *

class ComponentFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', pady=(0, 10), ipadx=8)

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