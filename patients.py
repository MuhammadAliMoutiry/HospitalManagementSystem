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
    record = get_num_records()
    patient_database = open('patient_database.txt', 'rb')
    for i in range(0, record):
        try:
            patient_info = pickle.load(patient_database)
            if patient_info['Patient_ID'] == patient_id:
                result = True
                break
        except EOFError:
            break
    return result
#this function sets the number of records that is installed in patient_records_database
#file to use this in the various operations , when called it increments the record
# by 1
def set_num_records(record):
    num_records = open('patient_records_database.txt','w')
    record +=1
    num_records.write(str(record))
    num_records.close()
# It retrieves the num of records from patient_recorsa_database.txt file
def get_num_records():
    num_records = open('patient_records_database.txt', 'r')
    record = num_records.readline()
    num_records.close()
    return int(record)

# add a new patient to the database
def add_patient():
    record = get_num_records()
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
        set_num_records(record)

#delete a patient from the database
def delete_patient(patient_id):
    record = get_num_records()
    patient_database = open('patient_database.txt', 'rb')
    temp_file = open('temp_file.txt', 'wb')
    for i in range(0, record):
        try:
            patient_info = pickle.load(patient_database)
            if patient_info['Patient_ID'] == patient_id:
                set_num_records(record - 1)
                continue
            else:
                pickle.dump(patient_info,temp_file)
        except EOFError:
            break
    temp_file.close()
    patient_database.close()
    record = get_num_records()
    patient_database = open('patient_database.txt', 'wb')
    temp_file = open('temp_file.txt', 'rb')
    for i in range(0, record):
        try:
            patient_info = pickle.load(temp_file)
            pickle.dump(patient_info,patient_database)
        except EOFError:
            break
    temp_file.close()
    patient_database.close()

# edit an existing patient using patient ID
def edit_patient(patient_id):
    record = get_num_records()
    patient_database = open('patient_database.txt', 'rb')
    temp_file = open('temp_file.txt', 'wb')
    for i in range(0, record):
        try:
            patient_info = pickle.load(patient_database)
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
        except EOFError:
            break
    temp_file.close()
    patient_database.close()
    record = get_num_records()
    patient_database = open('patient_database.txt', 'wb')
    temp_file = open('temp_file.txt', 'rb')
    for i in range(0, record):
        try:
            patient_info = pickle.load(temp_file)
            pickle.dump(patient_info, patient_database)
        except EOFError:
            break
    temp_file.close()
    patient_database.close()

# Display all the patients in the database
def display_patients():
    record = get_num_records()
    patient_database = open('patient_database.txt', 'rb')
    for i in range (0,record):
        try:
            patient_info = pickle.load(patient_database)
            print(patient_info)
        except EOFError:
            break

#display a single patient according to ID
def display_patient(patient_id):
    state = search_for_id(patient_id)
    record = get_num_records()
    patient_database = open('patient_database.txt', 'rb')
    if state:
        for i in range(0, record):
            try:
                patient_info = pickle.load(patient_database)
                if patient_info['Patient_ID'] == patient_id:
                    print(patient_info)
                    break
            except EOFError:
                break
    else :
        print('There is no patients with this ID .')

def display_temp():
    record = get_num_records()
    temp_file = open('temp_file.txt', 'rb')
    for i in range (0,record):
        patient_info = pickle.load(temp_file)
        print(patient_info)

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

