from tkinter import messagebox
import mysql.connector

import globalsVar


def user_name_details(mail):
    mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!", database="final_project_db")
    # Check login field
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE mail = %s",
                     (mail,))
    result = mycursor.fetchone()
    if result:
        globalsVar.password_global = result[1]
        return True
    else:
        return False


def send_to_db(mail,password,firstname,lastname,country,city,age,field):
    mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!", database="final_project_db")
    # Check login field
    mycursor = mydb.cursor()
    query = "UPDATE users SET password = %s, name = %s, lastname = %s, country = %s, city = %s, age = %s, field = %s " \
            "WHERE mail = %s;"
    values = (password, firstname, lastname, country, city, age, field, mail)
    mycursor.execute(query, values)
    mydb.commit()

