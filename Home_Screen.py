from tkinter import *


def init_home_page(window):
    image1 = PhotoImage(file="assets/article1.png")

    # Use the reference to the image to create the button.
    image1_button = Button(
        window,
        image=image1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=lambda: show_article(window)
    )
    image1_button.image = image1  # Keep a reference to the image.
    image1_button.place(x=400, y=150, width=400, height=136)


def show_article(window):
    toplevel = Toplevel(window)
    toplevel.title('Article')
    toplevel_width = 750
    toplevel_height = 735
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#525561")

    image11 = PhotoImage(file="assets/article11.png")
    label = Label(toplevel, width=650, height=735)
    label.image = image11
    label.configure(image=image11)
    label.pack()

