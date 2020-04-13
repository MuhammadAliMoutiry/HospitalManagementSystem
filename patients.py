import pickle
"""
This project is an application of using files in python
    This File contains all functions for managing patients including
    Adding a new patient
    Deleting an existing patient
    Display an existing patient
    Edit an existing patient
    Display all patients
    search a patient by its ID
    
"""
#This function searches for an ID if the ID exists in the patient_database file
# it returns True  -- else It returns False
def search_for_id(patient_id):
    result = False
    patient_database = open('patient_database.txt', 'r')
    temp = patient_database.readline()
    patient_database.close()
    if temp:
        patient_database = open('patient_database.txt', 'rb')
        patient_info = pickle.load(patient_database)
        while patient_info:
            try:
                if patient_info['Patient_ID'] == patient_id:
                    result = True
                    patient_database.close()
                    break
                patient_info = pickle.load(patient_database)
            except EOFError:
                patient_database.close()
                break
    return result


# add a new patient to the database
def add_patient():
    patient_database = open('patient_database.txt', 'ab')
    patient_info = dict()
    print('Add a New Patient :')
    patient_info['Department_Name']= input('Enter Department Name :')
    patient_info['Doctor_Name']=input('Enter Doctor Name :')
    patient_info['Patient_Name']=input('Enter Patient Name :')
    patient_info['Patient_Age']= input('Enter Patient Age :')
    patient_info['Patient_Gender']=input('Enter Patient Gender :')
    patient_info['Patient_Address']=input('Enter Patient Address :')
    patient_info['Patient_Phone_Number']=input('Enter Patient Phone Number :')
    patient_info['Patient_Room_Number']=input('Enter Patient Room Number :')
    patient_info['Patient_Condition']=input('Enter Patient Condition :')
    patient_info['Patient_ID']=input('Enter Patient ID :')
    patient_id = search_for_id(patient_info['Patient_ID'])
    while  patient_id:
        print('Redundant Patient ID ,Please Enter a unique ID : ')
        patient_info['Patient_ID'] = input('Enter Patient ID :')
        patient_id = search_for_id(patient_info['Patient_ID'])
    if not patient_id:
        pickle.dump(patient_info,patient_database)
        patient_database.close()

#delete a patient from the database
def delete_patient(patient_id):
    patient_database = open('patient_database.txt', 'rb')
    temp_file = open('temp_file.txt', 'wb')
    patient_info = pickle.load(patient_database)
    while patient_info:
        try:
            if patient_info['Patient_ID'] == patient_id:
                patient_info = pickle.load(patient_database)
                continue
            else:
                pickle.dump(patient_info,temp_file)
            patient_info = pickle.load(patient_database)
        except EOFError:
            break
    temp_file.close()
    patient_database.close()
    patient_database = open('patient_database.txt', 'wb')
    temp_file = open('temp_file.txt', 'rb')
    patient_info = pickle.load(temp_file)
    while patient_info:
        try:
            pickle.dump(patient_info,patient_database)
            patient_info = pickle.load(temp_file)
        except EOFError:
            break
    temp_file.close()
    patient_database.close()

# edit an existing patient using patient ID
def edit_patient(patient_id):
    patient_database = open('patient_database.txt', 'rb')
    temp_file = open('temp_file.txt', 'wb')
    patient_info = pickle.load(patient_database)
    while patient_info:
        try:
            if patient_info['Patient_ID'] == patient_id:
                patient_info['Department_Name'] = input('Edit Department Name :')
                patient_info['Doctor_Name'] = input('Edit Doctor Name :')
                patient_info['Patient_Name'] = input('Edit Patient Name :')
                patient_info['Patient_Age'] = input('Edit Patient Age :')
                patient_info['Patient_Gender'] = input('Edit Patient Gender :')
                patient_info['Patient_Address'] = input('Edit Patient Address :')
                patient_info['Patient_Phone_Number'] = input('Edit Patient Phone Number :')
                patient_info['Patient_Room_Number'] = input('Edit Patient Room Number :')
                patient_info['Patient_Condition'] = input('Edit Patient Condition :')
                patient_info['Patient_ID'] = input('Edit Patient ID :')
                patient_id = search_for_id(patient_info['Patient_ID'])
                while  patient_id:
                    print('Redundant Patient ID ,Please Enter a unique ID : ')
                    patient_info['Patient_ID'] = input('Enter Patient ID :')
                    patient_id = search_for_id(patient_info['Patient_ID'])
                if not patient_id:
                    pickle.dump(patient_info, temp_file)
                continue
            else:
                pickle.dump(patient_info, temp_file)
            patient_info = pickle.load(patient_database)
        except EOFError:
            break
    temp_file.close()
    patient_database.close()
    patient_database = open('patient_database.txt', 'wb')
    temp_file = open('temp_file.txt', 'rb')
    patient_info = pickle.load(temp_file)
    while patient_info:
        try:
            pickle.dump(patient_info, patient_database)
            patient_info = pickle.load(temp_file)
        except EOFError:
            break
    temp_file.close()
    patient_database.close()

# Display all the patients in the database
def display_patients():
    patient_database = open('patient_database.txt', 'rb')
    patient_info = pickle.load(patient_database)
    while patient_info:
        try:
            print(patient_info)
            patient_info = pickle.load(patient_database)
        except EOFError:
            break

#display a single patient according to ID
def display_patient(patient_id):
    state = search_for_id(patient_id)
    patient_database = open('patient_database.txt', 'rb')
    patient_info = pickle.load(patient_database)
    if state:
        while patient_info:
            try:
                if patient_info['Patient_ID'] == patient_id:
                    print(patient_info)
                    break
                patient_info = pickle.load(patient_database)
            except EOFError:
                break
    else :
        print('There is no patients with this ID .')

def manage_patients():
    print('--------------------------------------------------------------')
    print('---------------------- Welcome Admin -------------------------')
    print('********************* MANAGE PATIENTS ************************')
    print('--------------------------------------------------------------')
    print('1 - Add a New Patient')
    print('--------------------------------------------------------------')
    print('2 - Delete an Existing Patient')
    print('--------------------------------------------------------------')
    print('3 - Edit an Existing Patient')
    print('--------------------------------------------------------------')
    print('4 - Display an Existing Patient')
    print('--------------------------------------------------------------')
    print('5 - Display Patients Details')
    print('--------------------------------------------------------------')
    print('6 - Search For a Patient ID')
    print('--------------------------------------------------------------')
    print('Press The Number of Your Choice  :   ')
    print('--------------------------------------------------------------')
    choice = input()
    if choice == '1':
        add_patient()
    elif choice == '2':
        patient_id = input('Enter Patient ID to delete ......')
        delete_patient(patient_id)
    elif choice == '3':
        patient_id = input('Enter Patient ID to Edit ......')
        edit_patient(patient_id)
    elif choice == '4':
        patient_id = input('Enter Patient ID to Display ......')
        display_patient(patient_id)
    elif choice == '5':
        display_patients()
    elif choice == '6':
        patient_id = input('Enter Patient ID to Search for......')
        search_for_id(patient_id)

