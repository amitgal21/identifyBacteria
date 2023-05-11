import os
from tkinter import *
from tkinter import messagebox
import globalsVar
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label3 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#272A37"
)
headerText_image_label3.place(x=60, y=25)

headerText6 = Label(
    bg_image,
    text="Result Page",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 28 * -1),
    bg="#272A37"
)
headerText6.place(x=110, y=25)


# ========================= Bacteria Name ========================================
def create_text(str1, x1, y1):
    text1 = Label(
        window,
        anchor="nw",
        text=str1,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text1.place(x=x1, y=y1)


create_text("Bacteria Name: ", 500, 160)
create_text("Bacteria Type: ", 500, 210)
create_text("Accuracy: ", 500, 260)
create_text("Treatment recommendations: ", 500, 310)


# ============================ Separate The Screen ===============================
# ===================MIDDLE lINE =========================
underline = Frame(window, bg="white", highlightthickness=0)
underline.place(x=160, y=450, height=2, width=900)
# =================== Your Images Title ===================
text = Label(
    window,
    anchor="nw",
    text="Your Images:",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 18 * -1),
    bg="#272A37"
)
text.place(x=160, y=460)
# ===================Open The Images That the User Insert  =========================
if globalsVar.path_image1 != "":
    # open the image using PIL
    image = Image.open("UsersUploads\\" + globalsVar.path_image1)
    # resize the image to a maximum width and height of 400 pixels
    max_size = 100
    resized_image = image.resize((max_size, max_size))
    # convert the image to a PhotoImage object that tkinter can display
    photo = ImageTk.PhotoImage(image=resized_image)
    # create a label to display the image
    label = Label(window, image=photo, bg="#525561", bd=0, highlightthickness=0, padx=0, pady=0)
    label.image = photo  # keep a reference to the image to prevent garbage collection
    # display the label in a different position for each image
    label.place(x=200, y=500)
if globalsVar.path_image2 != "":
    # open the image using PIL
    image = Image.open("UsersUploads\\" + globalsVar.path_image2)
    # resize the image to a maximum width and height of 400 pixels
    max_size = 100
    resized_image = image.resize((max_size, max_size))
    # convert the image to a PhotoImage object that tkinter can display
    photo = ImageTk.PhotoImage(image=resized_image)
    # create a label to display the image
    label = Label(window, image=photo, bg="#525561", bd=0, highlightthickness=0, padx=0, pady=0)
    label.image = photo  # keep a reference to the image to prevent garbage collection
    # display the label in a different position for each image
    label.place(x=350, y=500)
if globalsVar.path_image3 != "":
    # open the image using PIL
    image = Image.open("UsersUploads\\" + globalsVar.path_image3)
    # resize the image to a maximum width and height of 400 pixels
    max_size = 100
    resized_image = image.resize((max_size, max_size))
    # convert the image to a PhotoImage object that tkinter can display
    photo = ImageTk.PhotoImage(image=resized_image)
    # create a label to display the image
    label = Label(window, image=photo, bg="#525561", bd=0, highlightthickness=0, padx=0, pady=0)
    label.image = photo  # keep a reference to the image to prevent garbage collection
    # display the label in a different position for each image
    label.place(x=500, y=500)
# =============================== pie chart ===============================

# Create a matplotlib figure with blue background
fig = plt.figure(figsize=(3, 3), facecolor='#272A37')
s=[80, 5, 5, 8, 2]
l = ["Cocci", "Bacilli", "Spirilla", "Vibrio's", "Spirochaetes"]
plt.pie(s, labels=l)

# Adjust the position of the pie chart within its area
fig.subplots_adjust(left=0, top=1)

# Draw the figure on a tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()

# Position the canvas on the screen
canvas.get_tk_widget().place(x=150, y=150)




window.mainloop()
