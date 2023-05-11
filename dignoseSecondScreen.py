from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import traceback
import os
import shutil

import globalsVar

window = Tk()

height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#525561")

# ================Background Image ====================
backgroundImage = PhotoImage(file="assets\\image_1.png")
bg_image = Label(
    window,
    image=backgroundImage,
    bg="#525561"
)
bg_image.place(x=120, y=28)

# keep track of the number of images uploaded
num_images_uploaded = 0
headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label3 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#272A37"
)
headerText_image_label3.place(x=60, y=45)

headerText6 = Label(
    bg_image,
    text="Diagnoses Page",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 26 * -1),
    bg="#272A37"
)
headerText6.place(x=110, y=45)

# ================ Header Text Right ====================
headerText_image_right = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label = Label(
    bg_image,
    image=headerText_image_right,
    bg="#272A37"
)
headerText_image_label.place(x=500, y=45)

headerText2 = Label(
    bg_image,
    anchor="nw",
    text="BactiVision",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 26 * -1),
    bg="#272A37"
)
headerText2.place(x=550, y=45)

headerText3 = Label(
    bg_image,
    anchor="nw",
    text="Please upload the pictures of the bacteria you want to diagnose",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 18 * -1),
    bg="#272A37"
)
headerText3.place(x=100, y=100)


# ===================== upload image section resizable the images to one sieze and display on screen ==================

def upload_image():
    global num_images_uploaded
    if num_images_uploaded < 3:
        file_path = askopenfilename()
        try:
            # open the image using PIL
            image = Image.open(file_path)
            # resize the image to a maximum width and height of 400 pixels
            max_size = 200
            resized_image = image.resize((max_size, max_size))
            # convert the image to a PhotoImage object that tkinter can display
            photo = ImageTk.PhotoImage(resized_image)
            # create a label to display the image
            label = Label(window, image=photo, bg="#525561", bd=0, highlightthickness=0, padx=0, pady=0)
            label.image = photo  # keep a reference to the image to prevent garbage collection
            # display the label in a different position for each image
            if num_images_uploaded == 0:
                label.place(x=240, y=340)

                d_button = Button(window, fg='#f8f8f8', text="Diagnose", bg='#1D90F5',
                                  font=("yu gothic ui", 18, "bold"),
                                  cursor='hand2', relief="flat", bd=0, highlightthickness=0,
                                  activebackground="#1D90F5",
                                  command=lambda: diagnosing_func())
                d_button.place(x=740, y=200, width=250, height=70)
            elif num_images_uploaded == 1:
                label.place(x=540, y=340)
            elif num_images_uploaded == 2:
                label.place(x=840, y=340)
            # copy the image to the Dataset folder
            filename = os.path.basename(file_path)
            dst = os.path.join("UsersUploads", filename)
            # here we save the new path for the result screen
            if image.format != "PNG":
                filename = os.path.splitext(filename)[0] + ".png"
                dst = os.path.join("UsersUploads", filename)
                image.save(dst, "PNG")
            if num_images_uploaded == 0:
                globalsVar.path_image1 = filename
            elif num_images_uploaded == 1:
                globalsVar.path_image2 = filename
            else:
                globalsVar.path_image3 =filename

            shutil.copy(file_path, dst)

            num_images_uploaded += 1
        except Exception as e:
            # print out the error message for debugging purposes
            print(traceback.format_exc())
            messagebox.showerror("Error", "Failed to open image file.")
    else:
        messagebox.showwarning("Warning", "You can upload a maximum of 3 images.")


def diagnosing_func():
    window.destroy()
    import diagnosing_splash


# ============= upload image buttooon =========================
upload_button = Button(window, fg='#f8f8f8', text="Upload Images", bg='#1D90F5', font=("yu gothic ui", 18, "bold"),
                       cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                       command=upload_image)
upload_button.place(x=240, y=200, width=250, height=70)
# ============= prev image button =========================
prev_image = PhotoImage(file="assets/big_prev.png")


def back_to_user_Screen():
    window.destroy()
    import UserScreen


prev_button = Button(
    window,
    image=prev_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#3D404B",
    cursor="hand2", bg="#3D404B",
    command=lambda: back_to_user_Screen()
)
prev_button.image = prev_image  # Keep a reference to the image.
prev_button.place(x=140, y=550, width=54, height=54)

window.mainloop()
