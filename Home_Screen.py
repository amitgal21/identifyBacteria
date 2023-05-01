from tkinter import *
import globalsVar

global dlike_button2, disslike_button, like_button, like_button2, image1_button, image2_button, text1, text2
global text_1, text_2, text_3, text_4


def init_home_page(window):
    global disslike_button, like_button, like_button2, dlike_button2, image1_button, image2_button
    global text_1, text_2, text_3, text_4
    image1 = PhotoImage(file="assets/article1/article1.png")
    # Use the reference to the image to create the button.
    image1_button = Button(
        window,
        image=image1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=lambda: show_article1(window, "assets/article1/article11.png")
    )
    image1_button.image = image1  # Keep a reference to the image.
    image1_button.place(x=400, y=150, width=400, height=136)

    # ==================== Like And DissLike ====================================
    if globalsVar.itsClick1 == 1:
        text_1 = Label(
            window,
            anchor="nw",
            text="Next Time We Will Do It Better",
            fg="red",
            font=("yu gothic ui Bold", 17 * -1),
            bg="#272A37"
        )
        text_1.place(x=850, y=200)
    elif globalsVar.itsClick2 == 1:
        text_2 = Label(
            window,
            anchor="nw",
            text="Thank You Very Much",
            fg="green",
            font=("yu gothic ui Bold", 17 * -1),
            bg="#272A37"
        )
        text_2.place(x=850, y=200)
    else:
        like_image = PhotoImage(file="assets/like4.png")
        like_button = Button(
            window,
            image=like_image,
            borderwidth=0,
            highlightthickness=0,  # Set to the exact color value of the window's background color
            relief="flat",
            activebackground="#272A37",
            cursor="hand2", command=lambda: vote(1, 2, window)
        )
        like_button.image = like_image  # Keep a reference to the image.
        like_button.place(x=850, y=200, width=97, height=42)

        disslike_image = PhotoImage(file="assets/dislike4.png")
        disslike_button = Button(
            window,
            image=disslike_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            cursor="hand2", command=lambda: vote(1, 1, window)
        )
        disslike_button.image = disslike_image  # Keep a reference to the image.
        disslike_button.place(x=970, y=200, width=97, height=42)

    image2 = PhotoImage(file="assets/article2/article2.png")

    # Use the reference to the image to create the button.
    image2_button = Button(
        window,
        image=image2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=lambda: show_article2(window, "assets/article2/article21.png")
    )
    image2_button.image = image2  # Keep a reference to the image.
    image2_button.place(x=400, y=350, width=400, height=155)
    # ==================== Like And DissLike ====================================
    if globalsVar.itsClick3 == 1:
        text_3 = Label(
            window,
            anchor="nw",
            text="Next Time We Will Do It Better",
            fg="red",
            font=("yu gothic ui Bold", 17 * -1),
            bg="#272A37"
        )
        text_3.place(x=850, y=400)
    elif globalsVar.itsClick4 == 1:
        text_4 = Label(
            window,
            anchor="nw",
            text="Thank You Very Much",
            fg="green",
            font=("yu gothic ui Bold", 17 * -1),
            bg="#272A37"
        )
        text_4.place(x=850, y=400)
    else:
        like_image2 = PhotoImage(file="assets/like4.png")
        like_button2 = Button(
            window,
            image=like_image2,
            borderwidth=0,
            highlightthickness=0,  # Set to the exact color value of the window's background color
            relief="flat",
            activebackground="#272A37",
            cursor="hand2", command=lambda: vote(2, 2, window)
        )
        like_button2.image = like_image2  # Keep a reference to the image.
        like_button2.place(x=850, y=400, width=97, height=42)

        disslike2_image = PhotoImage(file="assets/dislike4.png")
        dlike_button2 = Button(
            window,
            image=disslike2_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            cursor="hand2", command=lambda: vote(2, 1, window)
        )
        dlike_button2.image = disslike2_image  # Keep a reference to the image.
        dlike_button2.place(x=970, y=400, width=97, height=42)


# ================== Show article in Home Screen Inside User Screen =============================
# stay here
def show_article1(window, path_article):
    toplevel = Toplevel(window)
    toplevel.title('Article')
    toplevel_width = 750
    toplevel_height = 735
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#525561")

    article = PhotoImage(file=path_article)
    label = Label(toplevel, width=650, height=735)
    label.image = article
    label.configure(image=article)
    label.pack()
    next_button = PhotoImage(file="assets/next.png")
    next_page11(toplevel, "assets/article1/article11.png", window)


# ================== Article #1 P1 =============================
def next_page11(toplevel, path_page, window):
    toplevel.destroy()
    toplevel2 = Toplevel(window)
    toplevel2.title('Article')
    toplevel2_width = 750
    toplevel2_height = 735
    toplevel2_position_x = int(window.winfo_width() / 2 - toplevel2_width / 2) + window.winfo_x()
    toplevel2_position_y = int(window.winfo_height() / 2 - toplevel2_height / 2) + window.winfo_y()
    toplevel2.geometry(f'{toplevel2_width}x{toplevel2_height}+{toplevel2_position_x}+{toplevel2_position_y}')
    toplevel2.configure(bg="#525561")

    image11 = PhotoImage(file=path_page)
    label = Label(toplevel2, width=650, height=735)
    label.image = image11
    label.configure(image=image11)
    label.pack()

    image2 = PhotoImage(file="assets/next.png")
    image1_button = Button(
        toplevel2,
        image=image2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", bg="#525561", command=lambda: next_page12(toplevel2, "assets/article1/article12.png", window)
    )
    image1_button.image = image2  # Keep a reference to the image.
    image1_button.place(x=710, y=660, width=30, height=30)


# ================== Article #1 P2 =============================
def next_page12(toplevel, path_page, window):
    toplevel.destroy()
    toplevel2 = Toplevel(window)
    toplevel2.title('Article')
    toplevel2_width = 750
    toplevel2_height = 735
    toplevel2_position_x = int(window.winfo_width() / 2 - toplevel2_width / 2) + window.winfo_x()
    toplevel2_position_y = int(window.winfo_height() / 2 - toplevel2_height / 2) + window.winfo_y()
    toplevel2.geometry(f'{toplevel2_width}x{toplevel2_height}+{toplevel2_position_x}+{toplevel2_position_y}')
    toplevel2.configure(bg="#525561")

    image11 = PhotoImage(file=path_page)
    label = Label(toplevel2, width=650, height=735)
    label.image = image11
    label.configure(image=image11)
    label.pack()

    image2 = PhotoImage(file="assets/next.png")
    image1_button = Button(
        toplevel2,
        image=image2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", bg="#525561", command=lambda: next_page13(toplevel2, "assets/article1/article13.png", window)
    )
    image1_button.image = image2  # Keep a reference to the image.
    image1_button.place(x=710, y=660, width=30, height=30)

    prev_image = PhotoImage(file="assets/prev.png")
    prev_button = Button(
        toplevel2,
        image=prev_image,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", bg="#525561",
        command=lambda: next_page11(toplevel2, "assets/article1/article11.png", window)
    )
    prev_button.image = prev_image  # Keep a reference to the image.
    prev_button.place(x=10, y=660, width=30, height=30)


# ================== Article #1 P3 =============================
def next_page13(toplevel2, path_page, window):
    toplevel2.destroy()
    toplevel3 = Toplevel(window)
    toplevel3.title('Article')
    toplevel3_width = 750
    toplevel3_height = 735
    toplevel3_position_x = int(window.winfo_width() / 2 - toplevel3_width / 2) + window.winfo_x()
    toplevel3_position_y = int(window.winfo_height() / 2 - toplevel3_height / 2) + window.winfo_y()
    toplevel3.geometry(f'{toplevel3_width}x{toplevel3_height}+{toplevel3_position_x}+{toplevel3_position_y}')
    toplevel3.configure(bg="#525561")

    image11 = PhotoImage(file=path_page)
    label = Label(toplevel3, width=650, height=735)
    label.image = image11
    label.configure(image=image11)
    label.pack()

    image2 = PhotoImage(file="assets/next.png")
    image1_button = Button(
        toplevel3,
        image=image2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", bg="#525561",
        command=lambda: next_page14(toplevel3, "assets/article1/article14.png", window)
    )
    image1_button.image = image2  # Keep a reference to the image.
    image1_button.place(x=710, y=660, width=30, height=30)

    prev_image = PhotoImage(file="assets/prev.png")
    prev_button = Button(
        toplevel3,
        image=prev_image,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", bg="#525561",
        command=lambda: next_page12(toplevel3, "assets/article1/article12.png", window)
    )
    prev_button.image = prev_image  # Keep a reference to the image.
    prev_button.place(x=10, y=660, width=30, height=30)


# ================== Article #1 P4 =============================

def next_page14(toplevel3, path_page, window):
    toplevel3.destroy()
    toplevel4 = Toplevel(window)
    toplevel4.title('Article')
    toplevel4_width = 750
    toplevel4_height = 735
    toplevel4_position_x = int(window.winfo_width() / 2 - toplevel4_width / 2) + window.winfo_x()
    toplevel4_position_y = int(window.winfo_height() / 2 - toplevel4_height / 2) + window.winfo_y()
    toplevel4.geometry(f'{toplevel4_width}x{toplevel4_height}+{toplevel4_position_x}+{toplevel4_position_y}')
    toplevel4.configure(bg="#525561")

    image11 = PhotoImage(file=path_page)
    label = Label(toplevel4, width=650, height=735)
    label.image = image11
    label.configure(image=image11)
    label.pack()

    prev_image = PhotoImage(file="assets/prev.png")
    prev_button = Button(
        toplevel4,
        image=prev_image,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", bg="#525561",
        command=lambda: next_page13(toplevel4, "assets/article1/article13.png", window)
    )
    prev_button.image = prev_image  # Keep a reference to the image.
    prev_button.place(x=10, y=660, width=30, height=30)


# ================ first page article 2 P1==================

def show_article2(window, path_article):
    toplevel = Toplevel(window)
    toplevel.title('Article')
    toplevel_width = 750
    toplevel_height = 735
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#525561")

    article = PhotoImage(file=path_article)
    label = Label(toplevel, width=650, height=735)
    label.image = article
    label.configure(image=article)
    label.pack()
    next_button = PhotoImage(file="assets/next.png")
    next_page21(toplevel, "assets/article2/article22.png", window)


# ================ article 2 P1==================
def next_page21(toplevel, path_page, window):
    toplevel.destroy()
    toplevel2 = Toplevel(window)
    toplevel2.title('Article')
    toplevel2_width = 750
    toplevel2_height = 735
    toplevel2_position_x = int(window.winfo_width() / 2 - toplevel2_width / 2) + window.winfo_x()
    toplevel2_position_y = int(window.winfo_height() / 2 - toplevel2_height / 2) + window.winfo_y()
    toplevel2.geometry(f'{toplevel2_width}x{toplevel2_height}+{toplevel2_position_x}+{toplevel2_position_y}')
    toplevel2.configure(bg="#525561")

    image11 = PhotoImage(file=path_page)
    label = Label(toplevel2, width=650, height=735)
    label.image = image11
    label.configure(image=image11)
    label.pack()

    image2 = PhotoImage(file="assets/next.png")
    image1_button = Button(
        toplevel2,
        image=image2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", bg="#525561", command=lambda: next_page22(toplevel2, "assets/article2/article22.png", window)
    )
    image1_button.image = image2  # Keep a reference to the image.
    image1_button.place(x=710, y=660, width=30, height=30)


# ================ article 2 P2==================
def next_page22(toplevel, path_page, window):
    toplevel.destroy()
    toplevel2 = Toplevel(window)
    toplevel2.title('Article')
    toplevel2_width = 750
    toplevel2_height = 735
    toplevel2_position_x = int(window.winfo_width() / 2 - toplevel2_width / 2) + window.winfo_x()
    toplevel2_position_y = int(window.winfo_height() / 2 - toplevel2_height / 2) + window.winfo_y()
    toplevel2.geometry(f'{toplevel2_width}x{toplevel2_height}+{toplevel2_position_x}+{toplevel2_position_y}')
    toplevel2.configure(bg="#525561")

    image11 = PhotoImage(file=path_page)
    label = Label(toplevel2, width=650, height=735)
    label.image = image11
    label.configure(image=image11)
    label.pack()

    prev_image = PhotoImage(file="assets/prev.png")
    prev_button = Button(
        toplevel2,
        image=prev_image,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", bg="#525561",
        command=lambda: next_page11(toplevel2, "assets/article2/article21.png", window)
    )
    prev_button.image = prev_image  # Keep a reference to the image.
    prev_button.place(x=10, y=660, width=30, height=30)


"""
i = 1 first article
i = 2 second article
j = 1 disslike pressed
j = 2 like pressed
"""


# ================ this function for like and disslike clicked ==================

def vote(i, j, window):
    global text1, text2
    if i == 1:
        disslike_button.destroy()
        like_button.destroy()
        from UserScreen import bring_back_details
        bring_back_details("Home Page")
        if j == 1:
            str_txt = "Next Time We Will Do It Better"
            color = "red"
            globalsVar.itsClick1 = 1
        else:
            str_txt = "Thank You Very Much"
            color = "green"
            globalsVar.itsClick2 = 1
    else:
        like_button2.destroy()
        dlike_button2.destroy()
        from UserScreen import bring_back_details
        bring_back_details("Home Page")
        if j == 1:
            str_txt = "Next Time We Will Do It Better"
            color = "red"
            globalsVar.itsClick3 = 1
        else:
            str_txt = "Thank You Very Much"
            color = "green"
            globalsVar.itsClick4 = 1

    if i == 1:
        text1 = Label(
            window,
            anchor="nw",
            text=str_txt,
            fg=color,
            font=("yu gothic ui Bold", 17 * -1),
            bg="#272A37"
        )
        text1.place(x=850, y=200)
    else:
        text2 = Label(
            window,
            anchor="nw",
            text=str_txt,
            fg=color,
            font=("yu gothic ui Bold", 17 * -1),
            bg="#272A37"
        )
        text2.place(x=850, y=400)


# ================ this function delete home screen details ==================
def clear_screen():
    if globalsVar.itsClick1 == 1 and 'text_1' in globals():
        text_1.destroy()
    elif globalsVar.itsClick2 == 1 and 'text_2' in globals():
        text_2.destroy()
    else:
        if 'disslike_button' in globals():
            disslike_button.destroy()
        if 'like_button' in globals():
            like_button.destroy()
    if globalsVar.itsClick3 == 1 and 'text_3' in globals():
        text_3.destroy()
    elif globalsVar.itsClick4 == 1 and 'text_4' in globals():
        text_4.destroy()
    else:
        if 'dlike_button2' in globals():
            dlike_button2.destroy()
        if 'like_button2' in globals():
            like_button2.destroy()
    if 'image1_button' in globals():
        image1_button.destroy()
    if 'image2_button' in globals():
        image2_button.destroy()
    if globalsVar.itsClick1 == 1 or globalsVar.itsClick2 == 1:
        text1.destroy()
    if globalsVar.itsClick3 == 1 or globalsVar.itsClick4 == 1:
        text2.destroy()
