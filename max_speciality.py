#Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
#{
#"P":"Pediatrics",
#"O":"Orthopedics",
#"E":"ENT
#} 

#Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    speciality=''
    check=''
    count_p=0
    count_e=0
    count_o=0
    for i in range(1,len(patient_medical_speciality_list),2):
        if patient_medical_speciality_list[i]=='P':
           count_p+=1
        elif patient_medical_speciality_list[i]=='O':
           count_o+=1
        else:
           count_e+=1
    
    
    dict={count_o:'O', count_p:'P', count_e:'E'}
    max_spec=dict.get(max(dict))

    speciality=medical_speciality.get(max_spec)
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[101,'O',102,'O',302,'P',305,'E',401,'O',656,'P']
medical_speciality={'E': 'ENT', 'O': 'Orthopedics', 'P': 'Pediatrics'}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
