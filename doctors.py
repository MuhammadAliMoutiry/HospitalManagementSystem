import pickle

# This function searches for an ID if the ID exists in the patient_database file
# it returns True  -- else It returns False
def search_for_id(doctor_id):
    result = False
    doctor_database = open('doctor_database.txt', 'r')
    temp = doctor_database.readline()
    doctor_database.close()
    if temp:
        doctor_database = open('doctor_database.txt', 'rb')
        doctor_info = pickle.load(doctor_database)
        while doctor_info:
            try:
                if doctor_info['Doctor_ID'] == doctor_id:
                    result = True
                    doctor_database.close()
                    break
                doctor_info = pickle.load(doctor_database)
            except EOFError:
                doctor_database.close()
                break
    return result

def add_doctor():
    doctor_database = open('doctor_database.txt', 'ab')
    doctor_info = dict()
    print('Add a New Doctor :')
    doctor_info['Department_Name'] = input('Enter Department Name :')
    doctor_info['Doctor_Name'] = input('Enter Doctor Name :')
    doctor_info['Doctor_Address'] = input('Enter Doctor Address :')
    doctor_info['Doctor_Phone_Number'] = input('Enter Doctor Phone Number :')
    doctor_info['Doctor_ID'] = input('Enter Doctor ID :')
    doctor_id = search_for_id(doctor_info['Doctor_ID'])
    while doctor_id:
        print('Redundant Doctor ID ,Please Enter a unique ID : ')
        doctor_info['Doctor_ID'] = input('Enter Doctor ID :')
        doctor_id = search_for_id(doctor_info['Doctor_ID'])
    if not doctor_id:
        pickle.dump(doctor_info, doctor_database)
        doctor_database.close()

# delete a doctor from the database
def delete_doctor(doctor_id):
    doctor_database = open('doctor_database.txt', 'rb')
    temp_file = open('temp_file.txt', 'wb')
    doctor_info = pickle.load(doctor_database)
    while doctor_info:
        try:
            if doctor_info['Doctor_ID'] == doctor_id:
                doctor_info = pickle.load(doctor_database)
                continue
            else:
                pickle.dump(doctor_info, temp_file)
            doctor_info = pickle.load(doctor_database)
        except EOFError:
            break
    temp_file.close()
    doctor_database.close()
    doctor_database = open('doctor_database.txt', 'wb')
    temp_file = open('temp_file.txt', 'rb')
    doctor_info = pickle.load(temp_file)
    while doctor_info:
        try:
            pickle.dump(doctor_info, doctor_database)
            doctor_info = pickle.load(temp_file)
        except EOFError:
            break
    temp_file.close()
    doctor_database.close()


# edit an existing doctor using doctor ID
def edit_doctor(doctor_id):
    doctor_database = open('doctor_database.txt', 'rb')
    temp_file = open('temp_file.txt', 'wb')
    doctor_info = pickle.load(doctor_database)
    while doctor_info:
        try:
            if doctor_info['Doctor_ID'] == doctor_id:
                doctor_info['Department_Name'] = input('Edit Department Name :')
                doctor_info['Doctor_Name'] = input('Edit Doctor Name :')
                doctor_info['Doctor_Address'] = input('Edit Doctor Address :')
                doctor_info['Doctor_Phone_Number'] = input('Edit Doctor Phone Number :')
                doctor_info['Doctor_ID'] = input('Edit Doctor ID :')
                doctor_id = search_for_id(doctor_info['Doctor_ID'])
                while doctor_id :
                    print('Redundant Doctor ID ,Please Enter a unique ID : ')
                    doctor_info['Doctor_ID'] = input('Enter Doctor ID :')
                    doctor_id = search_for_id(doctor_info['Doctor_ID'])
                if not doctor_id:
                    pickle.dump(doctor_info, temp_file)
                continue
            else:
                pickle.dump(doctor_info, temp_file)
            doctor_info = pickle.load(doctor_database)
        except EOFError:
            break
    temp_file.close()
    doctor_database.close()
    doctor_database = open('doctor_database.txt', 'wb')
    temp_file = open('temp_file.txt', 'rb')
    doctor_info = pickle.load(temp_file)
    while doctor_info:
        try:
            pickle.dump(doctor_info, doctor_database)
            doctor_info = pickle.load(temp_file)
        except EOFError:
            break
    temp_file.close()
    doctor_database.close()


# Display all the doctors in the database
def display_doctors():
    doctor_database = open('doctor_database.txt', 'rb')
    doctor_info = pickle.load(doctor_database)
    while doctor_info:
        try:
            print(doctor_info)
            doctor_info = pickle.load(doctor_database)

        except EOFError:
            break


# display a single doctor according to ID
def display_doctor(doctor_id):
    state = search_for_id(doctor_id)
    doctor_database = open('doctor_database.txt', 'rb')
    doctor_info = pickle.load(doctor_database)
    if state:
        while doctor_info:
            try:
                if doctor_info['Doctor_ID'] == doctor_id:
                    print(doctor_info)
                    break
                doctor_info = pickle.load(doctor_database)

            except EOFError:
                break
    else:
        print('There is no doctors with this ID .')

def manage_doctors():
    print('--------------------------------------------------------------')
    print('---------------------- Welcome Admin -------------------------')
    print('********************** MANAGE DOCTORS ************************')
    print('--------------------------------------------------------------')
    print('1 - Add a New Doctor')
    print('--------------------------------------------------------------')
    print('2 - Delete an Existing Doctor')
    print('--------------------------------------------------------------')
    print('3 - Edit an Existing Doctor')
    print('--------------------------------------------------------------')
    print('4 - Display an Existing Doctor')
    print('--------------------------------------------------------------')
    print('5 - Display Doctor Details')
    print('--------------------------------------------------------------')
    print('6 - Search For a Doctor ID')
    print('--------------------------------------------------------------')
    print('Press The Number of Your Choice  :   ')
    print('--------------------------------------------------------------')
    choice = input()
    if choice == '1':
        add_doctor()
    elif choice == '2':
        doctor_id = input('Enter Doctor ID to delete ......')
        delete_doctor(doctor_id)
    elif choice == '3':
        doctor_id = input('Enter Doctor ID to Edit ......')
        edit_doctor(doctor_id)
    elif choice == '4':
        doctor_id = input('Enter Doctor ID to Display ......')
        display_doctor(doctor_id)
    elif choice == '5':
        display_doctors()
    elif choice == '6':
        doctor_id = input('Enter Doctor ID to Search for......')
        if search_for_id(doctor_id):
            print('ID exists in the database')
        else:
            print('ID does not exist in the database')



