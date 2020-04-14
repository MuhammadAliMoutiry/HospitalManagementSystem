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
    password_check_result = password_check()
    if not password_check_result:
        select_mode()
    else:
        check = True
        while check:
            print('------------------------------------------')
            print('-------------WELCOME ADMIN----------------')
            print('------------------------------------------')
            print('1 - MANAGE PATIENTS                      |')
            print('------------------------------------------')
            print('2 - MANAGE DOCTORS')
            print('------------------------------------------')
            print('3 - MANAGE APPOINTMENTS')
            print('------------------------------------------')
            print('Press E or e to exit ... .... ...  ')
            print('------------------------------------------')
            choice = input('Enter the number of your choice : ')
            if choice == '1':
                patients.manage_patients()
            elif choice == '2':
                doctors.manage_doctors()
            elif choice == '3':
                appointments.manage_appointments()
            elif choice == 'E':
                check = False
            elif choice == 'e':
                check = False
            else:
                print('#############################################')
                print('Wrong Entry ....')
                print('#############################################')

def user_mode():
    check = True
    while check:
        print('------------------------------------------')
        print('-------------WELCOME USER-----------------')
        print('------------------------------------------')
        print('1 - VIEW ALL DEPARTMENTS                 |')
        print('------------------------------------------')
        print('2 - VIEW ALL DOCTORS')
        print('------------------------------------------')
        print('3 - VIEW ALL PATIENTS')
        print('------------------------------------------')
        print('4 - VIEW PATIENT WITH ID')
        print('------------------------------------------')
        print('5 - VIEW DOCTOR WITH ID')
        print('------------------------------------------')
        print('Press E or e to exit ... .... ...  ')
        print('------------------------------------------')
        choice = input('Enter the number of your choice : ')
        if choice == '1':
            doctors.display_departments()
        elif choice == '2':
            doctors.display_doctors()
        elif choice == '3':
            patients.display_patients()
        elif choice == '4':
            patient_id = input('Enter Patient ID :: ')
            patients.display_patient(patient_id)
        elif choice == '5':
            doctor_id = input('Enter Doctor ID :: ')
            doctors.display_doctor(doctor_id)
        elif choice == 'E':
            check = False
        elif choice == 'e':
            check = False
        else:
            print('#############################################')
            print('Wrong Entry ....')
            print('#############################################')

def hospital_management_system():
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
    print('               WELCOME TO HOSPITAL MANAGEMENT SYSTEM\n')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
    check = True
    while check:
        mode = select_mode()
        if mode == 1:
            admin_mode()
        elif mode == 2:
            user_mode()
        print('--------------------------------------')
        print('Press E or e to exit program or any key to continue... ')
        print('--------------------------------------')
        choice = input('Your choice is')
        if choice == 'E':
            check = False
        elif choice == 'e':
            check = False



hospital_management_system()




