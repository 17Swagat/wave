import customtkinter as ctk
import cv2 as cv
from PIL import Image, ImageTk
from tkinter import Canvas

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

class App(ctk.CTk):
    def __init__(self):
        # ctk settings
        super().__init__()
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.resizable(False, False)
        self.title('Wave')
        
        # layout
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')
        self.rowconfigure(0, weight=1)

        # cv settings & vid showing
        self.webcamView = WebCamView(self)

        # run
        self.mainloop()
    

class WebCamView(Canvas):
    def __init__(self, parent):
        super().__init__(master=parent, background='yellow',
                         bd=0, highlightthickness=0,
                         relief='ridge')
        self.grid(row=0, column=1, sticky='news')
        self.cap = cv.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.delete('all')
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame = cv.resize(frame, (self.winfo_width(), self.winfo_height()))
            frame_tk = ImageTk.PhotoImage(Image.fromarray(frame))
            self.create_image(0, 0, image=frame_tk, anchor='nw')
            self.img = frame_tk  # Store a reference to prevent garbage collection
        self.after(10, self.update_frame)


# main
if __name__ == '__main__':
    App()
