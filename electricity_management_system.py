print('Choose your user type: \n 1. Customer \n 2. Admin')
user_type = int(input('User type: '))
if user_type == 1:
    username1 = input('enter username:  ')
    password1 = input('enter password: ')
    print('Account created successfully.')
    print('Login to account')
elif user_type == 2:
    username2 = input('enter username:  ')
    password2 = input('enter password: ')
    print('Account created successfully.')
    print('Loginn to account')
else:
    print('INVALID')


import json

user = []

def add_user():
   print('You must sign in as an admin')
   username2 = input('enter username: ')
   password2 = input('enter password:  ')
   if username2 == username2 and password2 == password2:
        print('Log in successful')
   else:
        print('invalid credentials')
   cus_name  = input('Enter customer name: ')
   address = input('Enter customer address: ')
   contact = input('Enter customer contact: ')
   email = input('Enter customer email: ')
   connection_details = input('Enter meter number: ')
   user = {
        
        "cus_name": cus_name,
        "address": address,
        "contact": contact,
        "email": email,
        "connection_details" : connection_details
    }
user.append(user)
print("User added successfully!")

def view_user():
    print('You must sign in as an admin')
    username2 = input('enter username: ')
    password2 = input('enter password:  ')
    if username2 == username2 and password2 == password2:
        print('Log in successful')
    else:
        print('invalid credentials')
    if len(user) == 0:
        print("No user found.")
    else:
        for users in user:
            print("user name: ", user["user name"])
            print("address: ", user["address"])
            print("contact: ", user["contact"])
            print("email: ", user["email"])
            print("connection_details: ", user["connection_details"])


def tarif():
    print('You must sign in as an admin')
    username2 = input('enter username: ')
    password2 = input('enter password:  ')
    if username2 == username2 and password2 == password2:
        print('Log in successful')
    else:
        print('invalid credentials')
    reading = int(input('Input meter reading: '))
    date = input('Date of today is: ')
    choice = print('Choose your meter type: \n 1. Industrial \n 2. Residential')
    num = int(input('choice: '))
    if num == 1:
        if reading <= 110:
            bill = reading * 50
            VAT = bill * 19.25/100
            net_price = bill + VAT + 1000
            print('The industrial bill is', net_price)
        elif reading <= 400:
            bill = reading * 79
            VAT = bill * 19.25/100
            net_price = bill + VAT + 1000
            print('The industrial bill is', net_price)
        elif reading <= 800:
            bill = reading * 94
            VAT = bill * 19.25/100
            net_price = bill + VAT + 1000
            print('The industrial bill is', net_price)
        elif reading <= 801:
            bill = reading * 99
            VAT = bill * 19.25/100
            net_price = bill + VAT + 1000
            print('The industrial bill is', net_price)
        else:
            print('PLEASE REPORT TO THE OFFICE. YOU HAVE EXCEEDED YOUR MONTHLY CONSUMPTION...!')
    if num == 2: 
        if reading <= 110:
            bill = reading * 84
            VAT = bill * 19.25/100
            net_price = bill + VAT + 1000
            print('The industrial bill is', net_price)
        elif reading <= 400:
            bill = reading * 92
            VAT = bill * 19.25/100
            net_price = bill + VAT + 1000
            print('The industrial bill is', net_price)
        elif reading <= 800:
            bill = reading * 99
            VAT = bill * 19.25/100
            net_price = bill + VAT + 1000
            print('The industrial bill is', net_price)
        else:
            print('YOUR BILL IS EXCEEDINGLY HIGH. PLEASE REPORT TO THE OFFICE AT ONE...!')
            

def pay_bill():
    print('You must sign in as an customer')
    username1 = input('enter username: ')
    password1 = input('enter password:  ')
    if username1 == username1 and password1 == password1:
        print('Log in successful')
    else:
        print('invalid credentials')
    
    print("Your bill is: ", pay_bill)
    
def main():
    while True:
        print("----- Electricity Management System -----")
        print("1. Add a new user")
        print("2. View all users")
        print("3. What is your tarif")
        print("4. Pay My bill")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            view_user()
        elif choice == "3":
            tarif()
        elif choice == "4":
            pay_bill()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
if __name__ == "__add_user__":
    add_user()















    
