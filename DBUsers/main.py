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

def change_role():
    user_id = int(input("Enter user ID: "))
    role = input("Enter a new role: ")

    user = User.objects.get(id=user_id)
    user.role = role
    user.save()

def delete_user():
    user_id = int(input("Enter user ID: "))

    User.objects.get(id = user_id).delete()

while True:
    choice = int(input("Select an option:\n1.Add user\n2.Change role\n3.Delete user\n4.Exit\n"))
    if choice == 1:
        add_user()
    elif choice == 2:
        change_role()
    elif choice == 3:
        delete_user()
    elif choice == 4:
        break