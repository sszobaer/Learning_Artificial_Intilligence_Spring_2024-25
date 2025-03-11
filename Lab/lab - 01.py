import numpy as np

username_SignUp = input("Enter the username: ")
password_SignUp = input("Enter the password: ")
confirmPassword = input("Enter the password again: ")

if password_SignUp != confirmPassword:
    print("Password does not match. Try again...")
    exit()
else:
    print("Sign up successful. You can login to your account.")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username_SignUp==username and password_SignUp==password:
    x = np.random.randint(100000, 999999)
    print("Your OTP is", x)
    OTP = int(input ("Enter the otp: "))
    if OTP == x:
        print("Login Successful.")
else:
    print("Credentials error. Try again.")