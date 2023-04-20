import globalsVar
from tkinter import *
from tkinter import messagebox
from UserScreenQuery import *


# ================================================================
# =========================Functional Part========================
# ================================================================

# bring The Name And Last Name of The User
def user_details():
    details_of_user_query(globalsVar.mail_from_login)


def About_us_screen_delete():
    from aboutus_Func import clear_screen
    clear_screen()
    # ================ Header Text Left ====================
    headerText_image_lef2 = PhotoImage(file="assets\\headerText_image.png")
    headerText_image_label3 = Label(
        bg_image,
        image=headerText_image_left,
        bg="#272A37"
    )
    headerText_image_label3.place(x=60, y=45)

    headerText2 = Label(
        bg_image,
        text="Its Nice To See You " + globalsVar.last_name_global + " " + globalsVar.private_Name_global,
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    headerText2.place(x=110, y=45)

    # ================ Header Text Right ====================
    headerText_image_right4 = PhotoImage(file="assets\\headerText_image.png")
    headerText_image_label4 = Label(
        bg_image,
        image=headerText_image_right,
        bg="#272A37"
    )
    headerText_image_label4.place(x=500, y=45)

    headerText2 = Label(
        bg_image,
        anchor="nw",
        text="BactiVision",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 20 * -1),
        bg="#272A37"
    )
    headerText2.place(x=550, y=45)

    # ================ CREATE #3 HEADER ====================
    createAccount_header2 = Label(
        bg_image,
        text="What You Want To Do",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 24 * -1),
        bg="#272A37"
    )
    createAccount_header2.place(x=75, y=100)


# Change The Title of Page from white To Blue
def Change_Page_Color(page):
    temp = globalsVar.Current_User_Screen
    if temp == 'Home Page':
        Home.config(fg="#3D404B")
    elif temp == "Diagnosis Page":
        diag.config(fg="#3D404B")
    elif temp == 'Your Details':
        details.config(fg="#3D404B")
    elif temp == "About Us":
        aboutus.config(fg="#3D404B")
    else:
        logout.config(fg="#3D404B")
    globalsVar.Current_User_Screen = page


# user_details()
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

# ================ Header Text Left ====================
headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label1 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#272A37"
)
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(
    bg_image,
    text="Its Nice To See You " + globalsVar.last_name_global + " " + globalsVar.private_Name_global,
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
headerText1.place(x=110, y=45)

# ================ Header Text Right ====================
headerText_image_right = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label2 = Label(
    bg_image,
    image=headerText_image_right,
    bg="#272A37"
)
headerText_image_label2.place(x=500, y=45)

headerText2 = Label(
    bg_image,
    anchor="nw",
    text="BactiVision",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 20 * -1),
    bg="#272A37"
)
headerText2.place(x=550, y=45)

# ================ CREATE #3 HEADER ====================
createAccount_header = Label(
    bg_image,
    text="What You Want To Do",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 24 * -1),
    bg="#272A37"
)
createAccount_header.place(x=75, y=100)
# ================= Toggle Button ===============

toggle_menu = Frame(window, bg="#3D404B", highlightthickness=0)
toggle_menu.place(x=130, y=200, height=200, width=200)
# ================= Home Page ====================
Home = Button(text="Home Page", fg="#3D404B",
              font=("yu gothic ui Bold", 20 * -1),
              bg="#272A37",
              bd=0,
              activebackground="#272A37",
              activeforeground="#ffffff",
              cursor="hand2", command=lambda: home_func())
Home.place(x=130, y=200, width=200, height=50)


def home_func():
    Change_Page_Color('Home Page')
    Home.config(fg="#2596be")
    About_us_screen_delete()
    # ================= Toggle Button ===============


# ===================under Line=========================
underline = Frame(window, bg="white", highlightthickness=0)
underline.place(x=130, y=251, height=2, width=200)
# ================= diagnosis Page ====================
diag = Button(text="Diagnosis Page", fg="#3D404B",
              font=("yu gothic ui Bold", 20 * -1),
              bg="#272A37",
              bd=0,
              activebackground="#272A37",
              activeforeground="#ffffff",
              cursor="hand2", command=lambda: diag_func())
diag.place(x=130, y=252, width=200, height=50)


def diag_func():
    Change_Page_Color('Diagnosis Page')
    diag.config(fg="#2596be")
    print(globalsVar.Current_User_Screen)


# ===================under Line=========================
underline = Frame(window, bg="white", highlightthickness=0)
underline.place(x=130, y=300, height=2, width=200)
# ================= Your Details ====================
details = Button(text="Your Details", fg="#3D404B",
                 font=("yu gothic ui Bold", 20 * -1),
                 bg="#272A37",
                 bd=0,
                 activebackground="#272A37",
                 activeforeground="#ffffff",
                 cursor="hand2", command=lambda: details_func())
details.place(x=130, y=301, width=200, height=50)


def details_func():
    Change_Page_Color('Your Details')
    details.config(fg="#2596be")


# ===================under Line=========================
underline = Frame(window, bg="white", highlightthickness=0)
underline.place(x=130, y=351, height=2, width=200)

# ================= About Us ====================
aboutus = Button(text="About Us", fg="#3D404B",
                 font=("yu gothic ui Bold", 20 * -1),
                 bg="#272A37",
                 bd=0,
                 activebackground="#272A37",
                 activeforeground="#ffffff",
                 cursor="hand2", command=lambda: aboutus_func())
aboutus.place(x=130, y=352, width=200, height=50)
# ===================under Line=========================
underline = Frame(window, bg="white", highlightthickness=0)
underline.place(x=130, y=403, height=1, width=200)


def aboutus_func():
    Change_Page_Color('About Us')
    aboutus.config(fg="#2596be")
    from aboutus_Func import put_text_on_screen
    put_text_on_screen(window)


# ================= Log Out ====================
logout = Button(text="Logout", fg="#3D404B",
                font=("yu gothic ui Bold", 20 * -1),
                bg="#272A37",
                bd=0,
                activebackground="#272A37",
                activeforeground="#ffffff",
                cursor="hand2", command=lambda: logout_func())
logout.place(x=130, y=404, width=200, height=50)


def logout_func():
    Change_Page_Color('Logout')
    logout.config(fg="#2596be")


# ===================under Line=========================
underline = Frame(window, bg="white", highlightthickness=0)
underline.place(x=130, y=454, height=1, width=200)

window.resizable(False, False)
window.mainloop()
