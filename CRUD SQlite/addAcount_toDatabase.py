import sqlite3
import re 

#connect to a database

connection=sqlite3.connect("users.db")

#create a cursor

c= connection.cursor() 

validity_name=False
validity_email=False
validity_password=False

def is_valid_email(email):
    # Define the regular expression pattern for a basic email validation
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use re.match to check if the email matches the pattern
    match = re.match(email_pattern, email)

    # If there's a match, the email is valid; otherwise, it's not valid
    return bool(match)



def create_acount(user_name,email,password):
    if len(user_name)<3:
        print("Invalid Username")      
        main()
    else:
        validity_name=True
        
    if not is_valid_email(email):
        print("Invalid Email")
        main()
    else:
        validity_email=True    
    if len(password)<7:
        print("Invalid password (the password must contains at least 7 characteres)")
        main()
    else:
        validity_password=True
    
    if validity_name and validity_email and validity_password:
        c.execute("INSERT INTO accounts(username, email, password) VALUES (?, ?, ?)", (user_name, email, password))
        connection.commit()  # Commit the changes to the database
        print("Your account has been created successfully")

# commit the command

def main():
    if validity_name == False:
        user_name=input("Username : ")
    if validity_email==False:
        email=input("Email : ")
    if validity_password ==False: 
        password=input("Password : ")
    
    
    create_acount(user_name,email,password)

main()

connection.close()
#close the connection



