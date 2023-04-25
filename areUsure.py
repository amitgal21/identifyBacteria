from tkinter import *
from tkinter import messagebox


def yes_func(toplevel, window):
    toplevel.destroy()
    messagebox.showinfo("Diagnose Page", "Lets Begin")
    window.destroy()
    import dignoseSecondScreen



def no_func(toplevel):
    toplevel.destroy()


def areUsurefunc(window):
    toplevel = Toplevel(window)
    toplevel.title('Diagnose Page')
    toplevel_width = 400
    toplevel_height = 200
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#272A37")

    are_u_sure = Label(toplevel, text='Are You Sure?', fg="#FFFFFF", bg='#272A37',
                       font=("yu gothic ui", 24, 'bold'))
    are_u_sure.place(x=100, y=30)

    # ====================== YES BUTTON =====================
    yesButton = Button(toplevel, fg='#f8f8f8', text=' Yes ', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                       cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                       command=lambda: yes_func(toplevel, window))
    yesButton.place(x=60, y=130, width=100, height=45)

    # ==================yes_buttonBUTTON =====================
    noButton = Button(toplevel, fg='#f8f8f8', text=' No ', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                      cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                      command=lambda: no_func(toplevel))
    noButton.place(x=260, y=130, width=100, height=45)