#!/bin/python

import time
from checkUsersLogin import *

user_login = CheckLogin()

name = input("Enter a user name: ")
password = input("Enter a password: ")
print("Chacking user name and password .....")
time.sleep(3)

if user_login.check_data(name, password):
  email = input("Enter your email: ")
  print("Check the email .....")
  time.sleep(3)

  if user_login.is_email_valid(email):
    print("Welcome back!")
  else:
    print("Invalid email format?")
else:
  print("Your name or password is invalid?")
