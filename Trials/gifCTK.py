import tkinter
import customtkinter as tk #type: ignore
from PIL import Image, ImageTk
import os

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("idk")

        file = os.path.join("assets", "hello.gif")
        info = Image.open(file)

        frames = info.n_frames 

        photoimage_objects = []

        with Image.open(file) as im:
            for i in range(frames):
                im.seek(i)
                im.save(os.path.join("assets", "Hello", f"{i}.png"))
                path = Image.open(os.path.join("assets", "Hello", f"{i}.png"))
                obj = tk.CTkImage(light_image = path, dark_image = path, size = (400, 400))
                photoimage_objects.append(obj)

        def animation(current_frame=0):
            global loop
            image = photoimage_objects[current_frame]

            gif_label.configure(image=image)
            current_frame = current_frame + 1

            if current_frame == frames:
                current_frame = 0

            loop = self.after(50, lambda: animation(current_frame))


        def stop_animation():
            self.after_cancel(loop)


        gif_label = tk.CTkLabel(self, image = None, text = '')
        gif_label.place(x = 0, y = 0)
        animation()

        start = tk.CTkButton(self, text="Start", command=lambda: animation(current_frame=0))
        #start.pack()

        stop = tk.CTkButton(self, text="Stop", command=stop_animation)
        #stop.pack()


app = App()
app.mainloop()




