print('ELECTICITY MANAGEMENT SYSTTEM')
print()
cus_name  = input('Enter customer name: ')
address = input('Enter customer address: ')
contact = input('Enter customer contact: ')
email = input('Enter customer email: ')
connection_details = input('Enter meter number: ')
reading = int(input('Input meter reading: '))
date = input('date of today is: ')
choice = print('Choose your meter type: \n 1. Industrial \n 2. Residential')
num = int(input('choice: '))
if num == 1:
    if reading <= 110:
        bill = reading * 50
        print('Your residential bill is', bill)
    elif reading <= 400:
        bill = reading * 79
        print('Your residential bill is', bill)
    elif reading <= 800:
        bill = reading * 94
        print('Your residential bill is', bill)
    elif reading <= 801:
        bill = reading * 99
        print('Your residential bill is', bill)
    else:
        print('PLEASE REPORT TO THE OFFICE. YOU HAVE EXCEEDED YOUR MONTHLY CONSUMPTION...!')
if num == 2: 
    if reading <= 110:
        bill = reading * 84
        print('The industrial bill is', bill)
    elif reading <= 400:
        bill = reading * 92
        print('The industrial bill is', bill)
    elif reading <= 800:
        bill = reading * 99
        print('The industrial bill is', bill)
    else:
        print('YOUR BILL IS EXCEEDINGLY HIGH. PLEASE REPORT TO THE OFFICE AT ONE...!')
    
