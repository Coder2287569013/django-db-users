import d_setup
from Users.models import User

def add_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    role = input("Enter your role: ")

    User.objects.create(
        name = name,
        email = email,
        role = role
    )

add_user()