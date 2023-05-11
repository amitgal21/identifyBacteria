from tkinter import *
from tkinter import messagebox

global text1, text2, text3, text4, text5, text6, image1_button


# ==================== initialize the diagnose screen in user screen ==================
def start_Screen(window):
    global text1, text2, text3, text4, text5, text6, image1_button
    text1 = Label(
        window,
        anchor="nw",
        text="On our diagnose page, simply upload a photo of your Gram-stained bacterial sample and our software will ",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37"
    )
    text1.place(x=350, y=200)
    text2 = Label(
        window,
        anchor="nw",
        text="quickly and accurately identify the bacteria present.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37"
    )
    text2.place(x=350, y=230)
    text3 = Label(
        window,
        anchor="nw",
        text="Our state-of-the-art technology is designed to provide healthcare professionals with a fast and "
             "efficient",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37"
    )
    text3.place(x=350, y=260)
    text4 = Label(
        window,
        anchor="nw",
        text="diagnostic tool, helping to ensure accurate diagnoses and better patient outcomes.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37"
    )
    text4.place(x=350, y=290)
    text5 = Label(
        window,
        anchor="nw",
        text="With our user-friendly interface and advanced image recognition capabilities, you can trust that your "
             "bacterial ",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37"
    )
    text5.place(x=350, y=320)
    text6 = Label(
        window,
        anchor="nw",
        text="identification needs will be met with ease and precision.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37"
    )
    text6.place(x=350, y=350)

    image1 = PhotoImage(file="assets/lets_go_button.png")

    # Use the reference to the image to create the button.
    image1_button = Button(
        window,
        image=image1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=lambda: func1(window)
    )
    image1_button.image = image1  # Keep a reference to the image.
    image1_button.place(x=500, y=470, width=333, height=65)

# ==================== are you sure screen for button in diagnose screen in user ==================
def func1(window):
    from areUsure import areUsurefunc
    areUsurefunc(window)


# ==================== function for clear the diagnose screen in user screen ==================
def clDscr():
    text1.destroy()
    text2.destroy()
    text3.destroy()
    text4.destroy()
    text5.destroy()
    text6.destroy()
    image1_button.destroy()
