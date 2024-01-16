import sqlite3
import re

connection=sqlite3.connect('users.db')

c=connection.cursor()

def is_valid_email(email):
    # Define the regular expression pattern for a basic email validation
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use re.match to check if the email matches the pattern
    match = re.match(email_pattern, email)

    # If there's a match, the email is valid; otherwise, it's not valid
    return bool(match)


def account_is_found(email):
    c.execute("SELECT * FROM accounts WHERE email=?",[email])
    results=c.fetchall()
    connection.commit()
    if len(results)==0:
        return 0
    else:
        return 1

def check_info(password,email):
    c.execute("SELECT password FROM accounts WHERE email=?",[email])
    results=c.fetchone()
    connection.commit()
    if password==results[0]:
        return 1
    else:
        return 0
    
    
def change_password(new_password,email):
    c.execute("UPDATE accounts set password=? where email=?",[new_password,email])
    print(f"Password changed to {new_password}")
    connection.commit()

def change_email(email,new_email):
    if is_valid_email(new_email):
        c.execute("UPDATE accounts set email=? where email=?",[new_email,email])
        print(f"Email changed to {new_email}")
        connection.commit()
    else:
        print("The email is not valid")
        




print("Update account")
email=input("Enter the email of account >> ")
if(account_is_found(email)):
    password=input("Password >> ")
    if check_info(password,email):
        print("Options :")
        print("\t1-Change email\n\t2-Change Password\n\t3-change both\n\t4-Exit")
        option=input("Choose option >> ")
        option=int(option)
        if option==1:
            new_email=input("New Email : ")
            change_email(email,new_email)
        elif option==2:
            new_password=input("New password : ")
            change_password(new_password,email)
        elif option==3:
            new_email=input("New Email : ")
            new_password=input("New password : ")
            change_email(email,new_email)
            change_password(new_password,email)
        elif option==4:
            print("You Exited")
        else:
            print("Invalid option")
    else:
        print("Incorrect Password")
else:
    print("Their is no matching account!")
    
connection.close()
