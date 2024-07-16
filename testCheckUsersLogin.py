#!/bin/python

from checkUsersLogin import *
from pytest import fixture

@fixture
def user_login():
  user_login = CheckLogin()
  return user_login

def test_check_data_with_correct_data(user_login):
  assert user_login.check_data("Abdulrhman", "1234")

def test_check_data_with_incorrect_name(user_login):
  assert user_login.check_data("John", "1234") == False

def test_check_data_with_incorrect_password(user_login):
  assert user_login.check_data("Abdulrhman", "12345") == False

def test_is_email_valid_with_valid_email(user_login):
  assert user_login.is_email_valid("Abdulrhman@gmail.com")

def test_is_email_valid_with_invalid_email(user_login):
  assert user_login.is_email_valid("Abdulrhmangmail.com") == False
  assert user_login.is_email_valid("Abdulrhman@gmailcom") == False
  assert user_login.is_email_valid("@gmail.com") == False
  assert user_login.is_email_valid("Abdulrhman@gmail.") == False
  assert user_login.is_email_valid("@gmail.") == False
  assert user_login.is_email_valid("Abdulrhman@.com")
