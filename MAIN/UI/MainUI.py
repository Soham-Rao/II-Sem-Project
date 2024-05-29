#Imports
import tkinter
from PIL import Image, ImageTk 
import customtkinter as tk #type: ignore
import os

#Main Class
class App(tk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.windims = (1500, 770)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_coordinate = int((self.screen_width/2)-(self.windims[0]/2))
        y_coordinate = int((self.screen_height/2)-(self.windims[1]/2))-35

        self.geometry(f"{self.windims[0]}x{self.windims[1]}+{x_coordinate}+{y_coordinate}")
        self.resizable(False, False)
        self.title("ΔRCADE")

        icon_path = ImageTk.PhotoImage(file = os.path.join("MAIN", "UI", "assets", "pixel-art", "Sprite-0003.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, icon_path)

        self.images()

    def images(self) -> None:
        bg_img = Image.open(os.path.join("MAIN", "UI", "assets", "bg.jpg"))
        bg_img = tk.CTkImage(light_image = bg_img, dark_image = bg_img, size = (self.screen_width, self.screen_height))
        bg_label = tk.CTkLabel(self, width = self.screen_width, height = self.screen_height, image = bg_img, text = '')
        bg_label.place(x = 0, y = 0)

        portal_img = Image.open(os.path.join("MAIN", "UI", "assets", "portal3.png"))
        portal_img = tk.CTkImage(light_image = portal_img, dark_image = portal_img, size = (350, 350))
        portal_label = tk.CTkLabel(self, width = 350, height = 350, image = portal_img, text = '')
        portal_label.place(x = self.windims[0]//2-175, y = self.windims[1]//2-175)


#Splash screen class
class Splash(tk.CTk):
    def __init__(self):
        super().__init__()

        self.windims = (500, 200)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_coordinate = int((self.screen_width/2)-(self.windims[0]/2))+105
        y_coordinate = int((self.screen_height/2)-(self.windims[1]/2))

        self.geometry(f"{self.windims[0]}x{self.windims[1]}+{x_coordinate}+{y_coordinate}")
        self.resizable(False, False)
        
        self.animations()

        self.after(5_000, self.destroy)

    def animations(self):
        self.gif("Triangle")
        
    def gif(self, path):
        file = os.path.join("MAIN", "UI", "assets", "pixel-art", f"{path}.gif")
        file_info = Image.open(file)
        frames = file_info.n_frames

        photoimage_objects = []
        with Image.open(file) as im:
            for i in range(frames):
                im.seek(i)
                im.save(os.path.join("MAIN", "UI", "assets", "pixel-art", path, f"{i}.png"))
                obj = Image.open(os.path.join("MAIN", "UI", "assets", "pixel-art", path, f"{i}.png"))
                obj = tk.CTkImage(light_image = obj, dark_image = obj, size = (64, 64))
                photoimage_objects.append(obj)
        
        def anim(current_frame = 0):
            global loop
            img = photoimage_objects[current_frame]
            gif_label.configure(image = img)
            current_frame += 1

            if current_frame == frames:
                return

            loop = self.after(50, lambda: anim(current_frame))
        
        gif_label = tk.CTkLabel(self, image = None, text = '')
        gif_label.place(x = 200, y = 70)
        anim()
        

#__main__#
def main() -> None:
    splash = Splash()
    splash.after(2, splash.overrideredirect, 1)
    splash.mainloop()

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()