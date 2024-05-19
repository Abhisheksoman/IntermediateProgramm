import os
import uuid

if(os.path.exists("aware.txt")):
    old_doctor= input("enter the old doctor name")
    new_doctor= input("enter the new doctor name")
    if(old_doctor==new_doctor):
        print("prescription cannot change")
    else:
        old_ps= input("enter the old prescreption")
        new_ps= input("enter the  new prescreption")
        if old_ps==new_ps:
            print("continue to that medicine")
        else:
            f = open("aware.txt","w")
            f.write(f"the new prescreption is {new_ps} and new doctor is {new_doctor}")
else:
    f = open("aware.txt",'x')
    name= input("enter the patient name")
    age = int(input("enter the patient age"))
    birthday= int(input("enter the year of birth"))
    address= input("enter the patient residental area")
    fees= int(input("enter the amount to be pay by patient"))
    fever= input("enter the current patient situation")
    doctor=input("enter the patient doctor refernce")
    token= uuid.uuid4()
    asd = "--------------------------------------------------------------"
    f.write(f"{name} \n {asd} \n {str(age)}                  {str(birthday)} \n {address}                     {str(fees)} \n {fever}              {str(token)} \n {doctor}")
