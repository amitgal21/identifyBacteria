from tkinter import messagebox
import mysql.connector

import accountGUI

global mycursor, mydb

# check if the details are illegal and then if its legal he goes to the next view
def login_check(Login_emailName_entry, Login_passwordName_entry):
    if Login_emailName_entry == "" or Login_passwordName_entry == "":
        messagebox.showerror('Error', 'All Fields Required')
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!",
                                       database="final_project_db")

        # Check login field
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users WHERE mail = %s AND password = %s",
                         (Login_emailName_entry, Login_passwordName_entry))
        result = mycursor.fetchone()
        if result:
            messagebox.showinfo('Successful', 'Login is successful')
        else:
            messagebox.showerror('Error', "Invalid email or password")

# forgot password QUERY to update the new password
def update_password_query(mail, new_password):
    global mycursor, mydb
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!", database="final_project_db")
        mycursor = mydb.cursor()
        # Update password
        mycursor.execute("UPDATE final_project_db.users SET password = %s WHERE mail = %s", (new_password, mail))
        mydb.commit()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", "Failed to update password: {error}")
    finally:
        mycursor.close()
        mydb.close()

# this for forgot password to check if the details are legal
def check_exist(mail):
    global mycursor, mydb
    mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!",
                                   database="final_project_db")

    # Check login field
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM final_project_db.users WHERE mail = %s", (mail,))
    result = mycursor.fetchone()
    if result:
        return True
    return False


