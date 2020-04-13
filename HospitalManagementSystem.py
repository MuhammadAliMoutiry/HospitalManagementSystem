import patients
import doctors
import appointments

def select_mode():
    print('-------------------------')
    print('Select your mode :')
    print('-------------------------')
    print(' For Admin mode press 1 ')
    print(' For User mode press  2 ')
    x = int(input(' Your Mode  is ?  '))
    while x>2:
        print(' Wrong Mode , Please reselect your mode')
        print('-------------------------')
        print('Select your mode :')
        print('-------------------------')
        print(' For Admin mode press 1 ')
        print(' For User mode press  2 ')
        x = int(input(' Your Mode  is ?  '))
    return x;

def password_check():
    password = '1234'
    num_of_times = 3
    result = False
    print('Please Enter Your Password')
    while num_of_times > 0 and result == False:
        y = input()
        if y == password:
            result = True
        else:
            result = False
            num_of_times = num_of_times - 1
        if not result:
            if num_of_times > 0:
                print("You Entered Password Wrong, Please enter the Correct password: ")
            else:
                print("You Entered a Wrong Password 3 Times")
                print('SYSTEM EXIT')

        else:
            print(" WELCOME ADMIN ")
    return result



def admin_mode():
    password_check_result =password_check()
    if not password_check_result:
        select_mode()





# hospital_management_system():






while True:
    appointments.manage_appointments()
