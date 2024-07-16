#!/bin/python

from usersData import *

class CheckLogin:
  def __init__(self):
    pass

  def check_data(self, name:str, password:str) -> bool:
    if name in users_data and users_data[name] == password:
      return True
    else:
      return False

  def is_email_valid(self, email:str) -> bool:
    divid_email = email.split("@") + email.split(".com")

    if len(divid_email) != 4 or divid_email[0] == "":
      return False
    return True
