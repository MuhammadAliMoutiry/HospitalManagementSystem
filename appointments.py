import pickle

def search_for_id(patient_id):
    result = False
    appointment_database = open('appointment_database.txt', 'r')
    temp = appointment_database.readline()
    appointment_database.close()
    if temp:
        appointment_database = open('appointment_database.txt', 'rb')
        appointment_info = pickle.load(appointment_database)
        while appointment_info:
            try:
                if appointment_info['Patient_ID'] == patient_id:
                    result = True
                    appointment_database.close()
                    break
                appointment_info = pickle.load(appointment_database)
            except EOFError:
                appointment_database.close()
                break
    return result

def book_appointment():
    appointment_database = open('appointment_database.txt', 'ab')
    appointment_info = dict()
    print('Add a New Appointment :')
    appointment_info['Department_Name'] = input('Enter Department Name :')
    appointment_info['Doctor_Name'] = input('Enter Doctor Name :')
    appointment_info['Patient_Name'] = input('Enter Patient Name :')
    appointment_info['Patient_Age'] = input('Enter Patient Age :')
    appointment_info['Patient_Gender'] = input('Enter Patient Gender :')
    appointment_info['Patient_ID'] = input('Enter Patient ID :')
    appointment_id = search_for_id(appointment_info['Patient_ID'])
    while appointment_id:
        print('Redundant Patient ID ,Please Enter a unique ID : ')
        appointment_info['Patient_ID'] = input('Enter Patient ID :')
        appointment_id = search_for_id(appointment_info['Patient_ID'])
    if not appointment_id:
        pickle.dump(appointment_info, appointment_database)
        appointment_database.close()

def cancel_appointment(patient_id):
    appointment_database = open('appointment_database.txt', 'rb')
    temp_file = open('temp_file.txt', 'wb')
    appointment_info = pickle.load(appointment_database)
    while appointment_info:
        try:
            if appointment_info['Patient_ID'] == patient_id:
                appointment_info = pickle.load(appointment_database)
                continue
            else:
                pickle.dump(appointment_info, temp_file)
            appointment_info = pickle.load(appointment_database)
        except EOFError:
            break
    temp_file.close()
    appointment_database.close()
    appointment_database = open('appointment_database.txt', 'wb')
    temp_file = open('temp_file.txt', 'rb')
    appointment_info = pickle.load(temp_file)
    while appointment_info:
        try:
            pickle.dump(appointment_info, appointment_database)
            appointment_info = pickle.load(temp_file)
        except EOFError:
            break
    temp_file.close()
    appointment_database.close()

def edit_appointment(appointment_id):
    appointment_database = open('appointment_database.txt', 'rb')
    temp_file = open('temp_file.txt', 'wb')
    appointment_info = pickle.load(appointment_database)
    while appointment_info:
        try:
            if appointment_info['Patient_ID'] == appointment_id:
                appointment_info['Department_Name'] = input('Edit Department Name :')
                appointment_info['Doctor_Name'] = input('Edit Doctor Name :')
                appointment_info['Patient_Name'] = input('Edit Patient Name :')
                appointment_info['Patient_Age'] = input('Edit Patient Age :')
                appointment_info['Patient_Gender'] = input('Edit Patient Gender :')
                appointment_info['Patient_ID'] = input('Edit Patient ID :')
                appointment_id = search_for_id(appointment_info['Patient_ID'])
                while appointment_id :
                    print('Redundant Patient ID ,Please Enter a unique ID : ')
                    appointment_info['Patient_ID'] = input('Enter Patient ID :')
                    appointment_id = search_for_id(appointment_info['Patient_ID'])
                if not appointment_id:
                    pickle.dump(appointment_info, temp_file)
                continue
            else:
                pickle.dump(appointment_info, temp_file)
            appointment_info = pickle.load(appointment_database)
        except EOFError:
            break
    temp_file.close()
    appointment_database.close()
    appointment_database = open('appointment_database.txt', 'wb')
    temp_file = open('temp_file.txt', 'rb')
    appointment_info = pickle.load(temp_file)
    while appointment_info:
        try:
            pickle.dump(appointment_info, appointment_database)
            appointment_info = pickle.load(temp_file)
        except EOFError:
            break
    temp_file.close()
    appointment_database.close()

def display_appointments():
    appointment_database = open('appointment_database.txt', 'rb')
    appointment_info = pickle.load(appointment_database)
    while appointment_info:
        try:
            print(appointment_info)
            appointment_info = pickle.load(appointment_database)

        except EOFError:
            break

def display_appointment(patient_id):
    state = search_for_id(patient_id)
    appointment_database = open('appointment_database.txt', 'rb')
    appointment_info = pickle.load(appointment_database)
    if state:
        while appointment_info:
            try:
                if appointment_info['Patient_ID'] == patient_id:
                    print(appointment_info)
                    break
                appointment_info = pickle.load(appointment_database)

            except EOFError:
                break
    else:
        print('There is no appointments with this ID .')

def manage_appointments():
    check = True
    while check:
        print('--------------------------------------------------------------')
        print('---------------------- Welcome Admin -------------------------')
        print('******************** MANAGE APPOINTMENTS *********************')
        print('--------------------------------------------------------------')
        print('1 - Add a New Appointment')
        print('--------------------------------------------------------------')
        print('2 - Cancel an Existing Appointment')
        print('--------------------------------------------------------------')
        print('3 - Edit an Existing Appointment')
        print('--------------------------------------------------------------')
        print('4 - Display an Existing Appointment')
        print('--------------------------------------------------------------')
        print('5 - Display Appointments Details')
        print('--------------------------------------------------------------')
        print('6 - Search For an Appointment ')
        print('--------------------------------------------------------------')
        print('Press E or e to Exit ... ... ... ')
        print('--------------------------------------------------------------')
        print('Press The Number of Your Choice  :   ')
        print('--------------------------------------------------------------')
        choice = input()
        if choice == '1':
            book_appointment()
        elif choice == '2':
            appointment_id = input('Enter Patient ID to cancel appointment_id ......')
            cancel_appointment(appointment_id)
        elif choice == '3':
            appointment_id = input('Enter Patient ID to Edit appointment ......')
            edit_appointment(appointment_id)
        elif choice == '4':
            appointment_id = input('Enter Patient ID to Display appointment ......')
            display_appointment(appointment_id)
        elif choice == '5':
            display_appointments()
        elif choice == '6':
            appointment_id = input('Enter Patient ID to Search for appointment......')
            if search_for_id(appointment_id):
                print('Appointment exists in the database')
            else:
                print('Appointment does not exist in the database')
        elif choice == 'E':
            check = False
        elif check == 'e':
            check = False
        else:
            print('#############################################')
            print('Wrong Entry ....')
            print('#############################################')




