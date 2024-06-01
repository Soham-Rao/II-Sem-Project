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
        '''
        triangle_objects = []
        triangle = self.gif("Triangle", triangle_objects)
        triangle.place(x = 200, y = 70)
        
        def T1anim(current_frame = 0):
            global loop
            img = triangle_objects[current_frame]
            triangle.configure(image = img)
            current_frame += 1

            if current_frame == self.frames:
                return

            loop = self.after(50, lambda: T1anim(current_frame))


        T1anim()
        
        triangle_objects2 = []
        triangle2 = self.gif("Triangle", triangle_objects2)
        triangle2.place(x = 250, y = 70)
        
        def T2anim(current_frame = 0):
            global loop
            img = triangle_objects2[current_frame]
            triangle2.configure(image = img)
            current_frame += 1

            if current_frame == self.frames:
                return

            loop = self.after(50, lambda: T2anim(current_frame))


        T2anim()
        '''

        def Tanim(o, L, current_frame = 0):
            global loop
            img = L[current_frame]
            o.configure(image = img)
            current_frame += 1

            if current_frame == self.frames:
                return

            loop = self.after(50, lambda: Tanim(o, L, current_frame))

        triangle_objects = []
        triangle = self.gif("Triangle", triangle_objects)
        triangle.place(x = 200, y = 70)
        
        Tanim(triangle, triangle_objects)

        triangle_objects2 = []
        triangle2 = self.gif("Triangle", triangle_objects2)
        triangle2.place(x = 250, y = 70)

        Tanim(triangle2, triangle_objects2)


    def gif(self, path, letter_objects):
        file = os.path.join("MAIN", "UI", "assets", "pixel-art", f"{path}.gif")
        file_info = Image.open(file)
        self.frames = file_info.n_frames
        
        with Image.open(file) as im:
            for i in range(self.frames):
                im.seek(i)
                im.save(os.path.join("MAIN", "UI", "assets", "pixel-art", path, f"{i}.png"))
                obj = Image.open(os.path.join("MAIN", "UI", "assets", "pixel-art", path, f"{i}.png"))
                obj = tk.CTkImage(light_image = obj, dark_image = obj, size = (64, 64))
                letter_objects.append(obj)
        #global anim
        gif_label = tk.CTkLabel(self, image = None, text = '')
        return gif_label
        #gif_label.place(x = 200, y = 70)
        #anim()
        

#__main__#
def main() -> None:
    splash = Splash()
    splash.after(2, splash.overrideredirect, 1)
    splash.mainloop()

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()