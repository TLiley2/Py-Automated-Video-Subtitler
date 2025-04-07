import tkinter as tk
from tkinter import filedialog

should_run = True

# Create App class
class App(tk.Tk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Video Subtitler") 
        self.geometry("300x300")
        self.minsize(300, 300)
        self.maxsize(300, 300)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.label = tk.Label(self, text="Welcome to Py-Automated-Video-Subtitler")
        self.label.grid(row=0, column=0)

        def openFile():
            self.entry1.delete(0,"end")
            import os
            username = os.getlogin()
            filepath = filedialog.askopenfilename(initialdir=(r"C:\Users\\"+username+r"\Downloads"), title="Open file okay?", filetypes= (("text files","*.mp4"), ("all files","*.*")))
            self.entry1.insert(0, filepath)
        def on_focus_in(e):
            if e.widget.get() == "Enter .mp4 file location":
                e.widget.delete(0,"end")
        self.entry1 = tk.Entry(self, selectbackground="lightblue", selectforeground="black",font=("arial"))
        self.entry1.insert(0, "Enter .mp4 file location")
        self.entry1.bind("<FocusIn>", on_focus_in)
        self.entry1.grid(row=1, column=0)

        self.button1 = tk.Button(self, text="Open",command=openFile)
        self.button1.grid(row=1, column=1)

        def button_click():
            string1 = self.entry1.get()
            if ":/" in string1:
                pathz = string1.replace(r"/", "\\")
                import subtitler
                subtitler.suber(pathz)
                newWindow = tk.Toplevel(self)
                newWindow.title("New Window")
                newWindow.minsize(100, 100)
                newWindow.maxsize(100, 100)
                newWindow.configure(bg='white')
                newWindow.columnconfigure(0, weight=1)
                newWindow.label = tk.Label(newWindow, text="Job is done")
                newWindow.label.grid(row=0, column=0)
        self.button2 = tk.Button(self, text="Start",command=button_click)
        self.button2.grid(row=2, column=0)

        self.label = tk.Label(self, text="Please be aware that the GUI may become \n unresonive for a minute or two \n during the subtitling process")
        self.label.grid(row=3, column=0)

if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop() 