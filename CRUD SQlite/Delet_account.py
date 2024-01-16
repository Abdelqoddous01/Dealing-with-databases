import sqlite3

connection=sqlite3.connect('users.db')

c=connection.cursor()

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
    
def delet_account(email):
    c.execute("DELETE FROM accounts WHERE email=?",[email])
    print("Account deleted")
    connection.commit()
    
    

print("Delete account\n")
email=input("Enter email >>")
if account_is_found(email):
    command1=input("Are you sure (y/n)")
    if command1=="y" or command1=="Y":
        password=input("Enter your password >> ")
        if check_info(password,email):
            delet_account(email)
        else:
            print("Incorrect password")
    elif command1=="n" or command1=="N":
        print("Exit")
else:
    print("Their is no matching account")

