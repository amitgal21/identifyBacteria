from tkinter import *
from queryFiles.UserScreenQuery import *

global aboutusPage_header, det_header, home_header, diagHeader


# ================================================================
# =========================Functional Part========================
# ================================================================

# bring The Name And Last Name of The User
def user_details():
    details_of_user_query(globalsVar.mail_from_login)


user_details()
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
    text="Home Page",
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
""""""
Home.place(x=130, y=200, width=200, height=50)

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

# ================= Log Out ====================
logout = Button(text="Logout", fg="#3D404B",
                font=("yu gothic ui Bold", 20 * -1),
                bg="#272A37",
                bd=0,
                activebackground="#272A37",
                activeforeground="#ffffff",
                cursor="hand2", command=lambda: logout_func())
logout.place(x=130, y=404, width=200, height=50)

# ===================under Line=========================
underline = Frame(window, bg="white", highlightthickness=0)
underline.place(x=130, y=454, height=1, width=200)


# ==========================================================================================
# ================================ Functional Part =========================================
# ==========================================================================================

# This function synchronized between the screens delete the old screens and out
def synchronized_screens(new_page):
    old_page = globalsVar.Current_User_Screen
    Change_Page_Color(old_page)
    delete_old_page(old_page, new_page)

    globalsVar.Current_User_Screen = new_page


# Change The Title of button from blue to white when change the screen
def Change_Page_Color(old_page):
    if old_page == 'Home Page':
        Home.config(fg="#3D404B")
    elif old_page == "Diagnosis Page":
        diag.config(fg="#3D404B")
    elif old_page == 'Your Details':
        details.config(fg="#3D404B")
    elif old_page == "About Us":
        aboutus.config(fg="#3D404B")
    else:
        logout.config(fg="#3D404B")


# ============================ Delete old screen =============================
def delete_old_page(old_page, new_page):
    if old_page == 'Home Page':
        if globalsVar.first_time_2:
            createAccount_header.destroy()
            globalsVar.first_time_2 = False
            home_clean_func()
        else:
            home_header.destroy()
            bring_back_details(new_page)
            home_clean_func()
    elif old_page == "Diagnosis Page":
        diag_clean_screen()
        bring_back_details(new_page)
    elif old_page == 'Your Details':
        Details_screen_delete()
        bring_back_details(new_page)
    elif old_page == "About Us":
        About_us_screen_delete()
        bring_back_details(new_page)


# ==================== Home screen part ============================================
def home_func():
    global home_header
    synchronized_screens('Home Page')
    createAccount_header.destroy()
    Home.config(fg="#2596be")
    home_header = Label(
        bg_image,
        text="Home Page",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 24 * -1),
        bg="#272A37"
    )
    home_header.place(x=75, y=100)
    from Home_Screen import init_home_page
    init_home_page(window)


def home_clean_func():
    from Home_Screen import clear_screen
    clear_screen()


# ==================== diagnose screen part ============================================

def diag_func():
    global diagHeader
    synchronized_screens('Diagnosis Page')
    diag.config(fg="#2596be")
    createAccount_header.destroy()
    # create a new label for the "HOME PAGE" header
    diagHeader = Label(
        bg_image,
        text="Diagnoses Page",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 24 * -1),
        bg="#272A37"
    )
    diagHeader.place(x=75, y=100)
    from Diag_screen import start_Screen
    start_Screen(window)


def diag_clean_screen():
    # diagHeader.destroy()
    from Diag_screen import clDscr
    clDscr()
    diagHeader.destroy()


# ==================== your details screen part ============================================
def details_func():
    global det_header
    synchronized_screens('Your Details')
    details.config(fg="#2596be")
    # destroy the old "What You Want To Do" header label
    createAccount_header.destroy()
    # create a new label for the "HOME PAGE" header
    det_header = Label(
        bg_image,
        text="Your Private Details",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 24 * -1),
        bg="#272A37"
    )
    det_header.place(x=75, y=100)
    from YourDetailsScreen import put_details_on_screen
    put_details_on_screen(window)


def Details_screen_delete():
    det_header.destroy()
    from YourDetailsScreen import clear_details_screen
    clear_details_screen()


# ==================== about us part =========================================
def aboutus_func():
    global aboutusPage_header
    synchronized_screens('About Us')
    aboutus.config(fg="#2596be")
    # destroy the old "What You Want To Do" header label
    createAccount_header.destroy()
    # create a new label for the "HOME PAGE" header
    aboutusPage_header = Label(
        bg_image,
        text="ABOUT US",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 24 * -1),
        bg="#272A37"
    )
    aboutusPage_header.place(x=75, y=100)
    from aboutus_Func import put_text_on_screen
    put_text_on_screen(window)


def About_us_screen_delete():
    from aboutus_Func import clear_screen
    clear_screen()
    aboutusPage_header.destroy()


# ==================== logout part =========================================

def logout_func():
    synchronized_screens('Logout')
    logout.config(fg="#2596be")
    from logout_screen import shut_down
    shut_down(window)
    logout.config(fg="#3D404B")
    globalsVar.Current_User_Screen = 'Home Page'


def bring_back_details(new_page):
    headerText_image_lef2 = PhotoImage(file="assets\\headerText_image.png")
    headerText_image_label3 = Label(
        bg_image,
        image=headerText_image_left,
        bg="#272A37"
    )
    headerText_image_label3.place(x=60, y=45)

    headerText6 = Label(
        bg_image,
        text="Its Nice To See You " + globalsVar.last_name_global + " " + globalsVar.private_Name_global,
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    headerText6.place(x=110, y=45)

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


if globalsVar.first_time:
    home_func()
    globalsVar.first_time = False
window.resizable(False, False)
window.mainloop()
