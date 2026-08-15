import string 
import random

def generate_special(limit):
    charecters = string.ascii_letters + string.punctuation + string.digits
    password = ""
    for i in range(limit):
        password += random.choice(charecters)
    return password

def generate_no_special(limit):
    charecters = string.ascii_letters + string.digits
    password = ""
    for i in range(limit):
        password += random.choice(charecters)
    return password
