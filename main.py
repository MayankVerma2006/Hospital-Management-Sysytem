import pandas as pd
import numpy as np

df = pd.read_csv("hospital_data.csv")

if df.empty:
    print("Sorry No Data Found !!!")
else:
    print("Hospital Data Loaded Successfully !")
    print()
    print(f"Total Patients : {len(df["Name"])}")
    print(f"Total Columns : {len(df.columns)}")
    
print()
print("========== HOSPITAL MANAGEMENT SYSTEM ==========")
print()
print("1. Display All Patients")
print("2. Add New Patient")
print("3. Search Patient")
print("4. Update Patient")
print("5. Delete Patient")
print("6. Department-wise Patient Count")
print("7. Disease-wise Analysis")
print("8. Highest Hospital Bill")
print("9. Average Hospital Bill")
print("10. Show Pending Payments")
print("11. Sort Patients by Bill")
print("12. Save Data")
print("13. Exit")
print()
    

while True:
    try:
        
        mkv = int(input("Choose the option :"))
        
        if mkv == 1:
            print(df)
            
        elif mkv == 2:
            npi = input("Enter patient ID :")
            nn = input("Enter Name :")
            na = int(input("Enter the Age :"))
            ng = input("Enter Gender :")
            nd = input("Enter Department :")
            ndi = input("Enter Disease :")
            ndoc = input("Enter Doctor :")
            nda = input("Enter Admission Date :")
            ndd = input("Enter Dischage Date :")
            nb = input ("Enter Bill :")
            nps = input("Enter Payment Status :")

            df.loc[len(df)] = [npi,nn,na,ng,nd,ndi,ndoc,nda,ndd,nb,nps]
            print("Patient Added Successfully !!!")


        elif mkv==3:
            print("\n====== SEARCH PATIENT ======\n")
            pid = input("Enter Patient ID :")
            find = df[df["Patient_ID"].str.lower()==pid.lower()]
            if find.empty:
                print("Sorry,Patient not Found !!!")
            else:
                print("\n patient Found !!!\n")
                print(find.T.to_string(header=False))
                
                
        elif mkv == 4:
            print("\n======== UPDATE PATIENT =========\n") 
            patient = input("Enter Patient ID :")
            patient_data = df[df["Patient_ID"].str.lower()==patient.lower()]
            if patient_data.empty:
                print("Sorry,Patient not Found !!!")
            else:
                print("\nPatient Found !!!\n")
                
                print("What Do You Want To Update ???\n")
                print("1.Name")
                print("2.Age")
                print("3.Department")
                print("4.Disease")
                print("5.Doctor")
                print("6.Bill")
                print("7.Payment Status")
                
                choice_4 = int(input("Enter the Choice :"))
                if choice_4 == 1:
                    new_name = input("Enter New Name :")
                    df.loc[patient_data.index,"Name"]=new_name
                    print("Name Update Successfully... ")
                    
                elif choice_4 == 2:
                    new_age = int(input("Enter New Age :"))
                    df.loc[patient_data.index,"Age"]=new_age
                    print("Age Update Successfully... ")
                    
                elif choice_4 == 3:
                    new_department = input("Enter New Department :")
                    df.loc[patient_data.index,"Department"]=new_department
                    print("Department Update Successfully... ")
                    
                elif choice_4 == 4:
                    new_disease = input("Enter New Disease :")
                    df.loc[patient_data.index,"Disease"]=new_disease
                    print("Disease Update Successfully... ")
                    
                elif choice_4 == 5:
                    new_doctor = input("Enter New Doctor :")
                    df.loc[patient_data.index,"Doctor"]=new_doctor
                    print("Doctor Update Successfully... ")
                    
                elif choice_4 == 6:
                    new_bill = input("Enter New Bill :")
                    df.loc[patient_data.index,"Bill"]=new_bill
                    print("Bill Update Successfully... ")
                    
                elif choice_4 == 7:
                    new_Payment = input("Enter New Payment :")
                    df.loc[patient_data.index,"Payment"]=new_Payment
                    print("Payment Update Successfully... ")
                else:
                    print("Plz Enter btw 1 to 7")
                        
        elif mkv == 5:
            print("\n======== DELETE PATIENT =========\n")
            patient = input("Enter Patient ID :")
            patient_data = df[df["Patient_ID"].str.lower()==patient.lower()]
            if patient_data.empty:
                print("Sorry,Patient data not Found !!!")
            else:
                print("\nPatient Found !!!\n")
                print(patient_data.T.to_string(header=False))
                print()
                confirm = input("\nAre you Sure You Want to Delete This Patient ???? (yes/no) :")
                if confirm.lower()=="yes":
                    # df = df[df["Patient_ID"].str.lower() != patient.lower()]
                    df = df.drop(patient_data.index)
                    print("\nPatient Data Delete successfully... ")
                    print(df)
                else:
                    print("\nDeletion Cancellation")
        
        elif mkv == 6:
            print("\n======== DEPARTMENT-WISE PATIENT COUNT =========\n")  
            cc = df["Department"].value_counts()
            print(cc.to_string(header=False))
            print(f"\nTotal Patients :{cc.sum().sum()}")
                    
        elif mkv == 7:
            print("\n======== DISEASE-WISE PATIENT COUNT =========\n")  
            dis = df["Disease"].value_counts()
            print(dis.to_string(header=False))
            # print(f"\nTotal Patients :{dis.sum().sum()}")    
                
        elif mkv == 8:
            print("\n======== HIGHEST HOSPITAL BILL =========\n")  
            highest_bill = df[df["Bill"] == df["Bill"].max()]
            print(highest_bill.T.to_string(header=False))
            print(f"\nHighest Bill Found")
            
            
        elif mkv == 9:
            print("\n======== AVERAGE HOSPITAL BILL =========\n")  
            bill_cot = df["Bill"].value_counts()
            average_bill = df['Bill'].mean()
            print(f"Total Patients :{bill_cot.sum().sum()}")
            print(f"Average Bill : ₹{average_bill:.2f}")
            
            
        elif mkv == 10:
            print("\n======== PENDING PAYMENTS =========\n")  
            pending = df[df["Payment"]=="Pending"][["Patient_ID","Name","Department","Bill","Payment"]]
            t_p = pending["Bill"].sum()
            t_p = pd.to_numeric(pending["Bill"]).sum()
            
            print(pending.to_string(index=False))

            print(f"\nTotal Pending Payment :{len(pending)}")
            print(f"\nTotal Pending Amount :₹{t_p:.2f}\n")
                  
                  
        elif mkv == 11:
            print("\n======== SORTING PATIENT BY HOSPITAL BILLS  =========\n")  
            print("1. Lowest to Highest")
            print("2. Highest to lowest")

            choose = int(input("Enter choose :"))
            if choose == 1 :
                print("\n-----Sort Data Lowest to Highest-----\n")
                
                ass = df.sort_values(by="Bill",ascending=True)
                print(ass[["Patient_ID","Name","Bill","Payment"]].to_string(index=False))
            elif choose == 2:
                print("\n-----Sort Data Highest to Lowest-----\n")

                sss = df.sort_values(by="Bill",ascending=False)
                print(sss[["Patient_ID","Name","Bill","Payment"]].to_string(index=False))
                
            else:
                print("Sorry choose from 1 OR 2 ")
                
                
        elif mkv == 12 :
            print("\n======== SAVE DATA =========\n")
            if "Unnamed: 0" in df.columns:
                df = df.drop(columns=["Unnames: 0"])
                
            
            df.to_csv("hospital_data.csv",index=False)

            print("Saving Hospital Records...\n")
            print("Data Saved Successfully !\n")
            print("File: hospital_data.csv\n")
            print(f"Total Records Saved :{len(df)}")

        elif mkv == 13:
            print(f"==================================\n")
            print("Thank You For Using ")
            print("Hospital Management System")
            print(f"\n==================================")
            print("\nProgram Ended Successfully ")
            break
        
        else:
            print("Sorry please Choose btw 1 to 13 ")
            
    except Exception as e:
        print(e)