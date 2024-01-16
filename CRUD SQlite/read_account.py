import sqlite3


connection = sqlite3.connect('users.db')

c=connection.cursor()

def account_is_found(email):
    c.execute("SELECT * FROM accounts WHERE email=?",[email])
    results=c.fetchall()
    if len(results)==0:
        print("Their is no matching account")
    else:
        print("Account found")
        for item in results:
            print(f"Acount ID :{item[0]}")
            print(f"\tusername : {item[1]}")
            print(f"\temail : {item[2]}")
            print(f"\tpassword : {item[3]}")
    

#take the wanted email to search
def main():
    email=input("Enter the email for search >> ")
    account_is_found(email)
    
main()