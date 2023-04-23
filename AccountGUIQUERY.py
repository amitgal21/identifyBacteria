from tkinter import messagebox
import mysql.connector
import globalsVar
import accountGUI

global mycursor, mydb


# check if the details are illegal and then if its legal he goes to the next view
def login_check(Login_emailName_entry, Login_passwordName_entry):
    mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!", database="final_project_db")
    # Check login field
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE mail = %s AND password = %s",
                     (Login_emailName_entry, Login_passwordName_entry))
    result = mycursor.fetchone()
    if result:
        globalsVar.mail_from_login = Login_emailName_entry
        globalsVar.password_global = Login_passwordName_entry
        globalsVar.country_global = result[4]
        globalsVar.city_global = result[5]
        globalsVar.age_global = result[6]
        globalsVar.field_global = result[7]
        return True
    else:
        return False


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


def sign_up_query(firstName, lastName, mail, password):
    global mycursor, mydb
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!", database="final_project_db")
        mycursor = mydb.cursor()
        # Update password
        query = "INSERT INTO final_project_db.users (mail, password, name, lastname) VALUES (%s, %s, %s, %s)"
        mycursor.execute(query, (mail, password, firstName, lastName))
        mydb.commit()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", "Failed to update password: {error}")
    finally:
        mycursor.close()
        mydb.close()
