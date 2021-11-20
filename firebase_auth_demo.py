import credentials as creds


auth = creds.firebase.auth()

def signup():
    email = input("Enter the email : ")
    password = input("Enter the password : ")
    
    try:
        user = auth.create_user_with_email_and_password(email,password)
        print("Successfully signup")
        print(user)
    except:
        print("email already exist")   
        
def login():
    email = input("Enter the email : ")
    password = input("Enter the password : ")
    
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        print("Successfully login")
        print(login)  
    except:
        print("Invalid email or password")
    
ans = input("Are you new user? [y/n] : ")
if ans == 'y':
    signup()
elif ans == 'n':
    login()

    