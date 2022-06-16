# Enters phone number and email until valid input is entered

from pyisemail import is_email
import phonenumbers


class Validator:

    @staticmethod
    def validate_email(email):
        if not is_email(email):
            raise ValueError("Email is invalid")

    @staticmethod
    def validate_phone_number(phone_number):
        my_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(my_number):
            raise ValueError("Phone number must contain only digits")

    @staticmethod
    def input_email():
        while True:
            print("Email: ", end='')
            email = input()
            try:
                Validator.validate_email(email)
            except ValueError as e:
                print(e)
                continue
            return email

    @staticmethod
    def input_phone_number():
        while True:
            print("Phone number: ", end='')
            phone_number = input()
            try:
                Validator.validate_phone_number(phone_number)
            except phonenumbers.NumberParseException as e:
                print(e)
                continue
            return phone_number
