#6. Create user = {'username': 'admin', 'password': '1234'}. Check whether both values are correct. Print Login successful or Invalid login.

email = input("Enter Email: ")
password = input("Pass: ")

if email == "ssrahman2002@gmail.com" and password == "2002":
    print("WELCOME")
else: 
    print("invalid")



# try this also

user = {'username': 'admin', 'password': '1234'}

if user['username'] == 'admin' and user['password'] == '1234':
    print("Login successful")
else:
    print("Invalid login")
