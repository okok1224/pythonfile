

import os.path
from os import path
import datetime


def login(): #login function
    print("\n"+">"*30+"LOGIN PAGE"+"<"*30+"\n")
    n = 0
    while n < 2:# while loop
         n = n+1
         login_name = input("\nEnter your user name:")
         login_password = input("\nEnter your password:")
         found_user=False
         f = open("User.txt","r")
         for line in f: #checking if username and password are in the file and are correct
                 username,password = line.strip().split(" ")
                 if login_name == username:
                         found_user=True
                         if login_password == password:
                            print("\nLogin successful!!!\n")
                            WelcomePage()
                         else:
                             print("\nWrong password...\n"+"Please try it again!!\n")
         if found_user == False: # if username is not found then it prints invalid username
           print("\nInvalid username!!\n","\nPlease try it again!!\n")
    if n == 2:
       print('\n Invalid option entered too many times, process will be terminated')
       print('='*68)
       exit()
                           
                                   
def Twochoices(): # choice function which gives user the uption to continue or to exit the program
        print("\n"+"="*27)
        print("What do you want to do ?","1.Back to the Welcome page","2.Exit",sep = '\n')
        print("="*27)
        n = 0
        while n < 2:
              n = n+1
              select=str(input("\n"+"Plese enter your choice 1 or 2: "))    
              if select == "1":
                WelcomePage()
              elif select == "2":
                    exit()
              else:
                   print("\ninvalid value try it again!!\n")                
        if n == 2:
           print('\n Invalid option entered too many times, process will be terminated')
           print('='*68)
           exit()
                  
                        
def supplier_info(): # function which stores supplier information
            f = open("supplier.txt","w")
            f.close()
            n=0
            while n < 4:
                n = n + 1
                f = open("supplier.txt", "a") #appending the file
                SupplierName=input('\nEnter supplier ' + str(n) + "'s name: ")
                SuppierItem=input('Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')
                SupplierEmail = (input('Enter suppliers email:')).upper()
                SupplierLocation =input('Enter location of supplier: ')
                SecChoice=input("Does this supplier supply any other eqipment? Enter '1' for yes,'0' for No: " )
                if SecChoice=='1': #if choice is 1 then supplier can provide 2 items
                    SuppierItem2=input('Enter second item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')
                    f.write('Supplier code: ' +"S"+ str(n)+ "\n")
                    f.write('Supplier item: ' +SuppierItem.upper()+","+SuppierItem2.upper()+"\n")
                    f.write('Supplier name: ' +SupplierName.upper()+"\n")
                    f.write('Supplier Email: '+SupplierEmail+"\n")
                    f.write('Supplier Location: '+SupplierLocation.upper()+"\n")
                    f.write('Supplier Registration Date: '+ str(datetime.datetime.now())+ "\n")
                    f.write('==================================================================\n')
                elif SecChoice=='0': #if choice is 0 then the supplier can provide 1 item
                    f.write('Supplier code: ' +"S"+ str(n)+ "\n")
                    f.write('Supplier item: ' +SuppierItem.upper()+"\n")
                    f.write('Supplier name: ' +SupplierName.upper()+"\n")
                    f.write('Supplier Email: '+SupplierEmail+"\n")
                    f.write('Supplier Location: '+SupplierLocation.upper()+"\n")
                    f.write('Supplier Registration Date: '+ str(datetime.datetime.now())+ "\n")
                    f.write('==================================================================\n')   
                if n == 4:
                    f.close()
                    Twochoices()

                    
def hospital_info(): # function which stores hospital information
            f = open("hospital.txt","w") #opening the file to write
            f.close()
            n=0
            while n < 4:
                n = n + 1
                f = open("hospital.txt", "a") #user inputs the information of the hospital
                HospitalName=input('\nEnter hospital ' + str(n) + "'s name: ")
                HospitalEmail = (input('Enter hospital email: ')).upper()
                HospitalLocation =input('Enter location of hospital: ')
                f.write('Hospital code: ' +"H"+ str(n)+ "\n")
                f.write('Hospital name: ' +HospitalName.upper()+"\n")
                f.write('Hospital Email: '+HospitalEmail+"\n")
                f.write('Hospital Location: '+HospitalLocation.upper()+"\n")
                f.write('Hospital Registration Date: '+ str(datetime.datetime.now())+ "\n")
                f.write('==================================================================\n')
                if n == 4:
                    f.close()
                    Twochoices()


def initial_amount_of_inventory(): #funtion to write the initial amount of the inventory
    if path.exists("ppe.txt"): #if the file already exisit it will exit the funtion
        print("\nInitial Inventory already exists.\n")
        Twochoices()
    else:    # if the file does not exisit then it will create the file and the user will have to enter the initial amounts
        f = open('ppe.txt','w')
        contChoice='1'
        n=0
        while n < 6:
            n = n + 1
            ItemCode=(input("\n"+"="*99+"\n"+'Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')).upper()
            if not ItemCode == "HC"and not ItemCode == "FS" and not ItemCode == "MS" and not ItemCode == "GL" and not ItemCode == "GW" and not ItemCode == "SC":
                 print("\n"+"Item code must be from 'HC','FS','MS','GL','GW','SC'"+"\n"+"\nPlease try it again!!"+"\n")
                 ItemCode = (input('Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')).upper()
                 if not ItemCode == "HC"and not ItemCode == "FS" and not ItemCode == "MS" and not ItemCode == "GL" and not ItemCode == "GW" and not ItemCode == "SC":
                         print('\n Invalid option entered too many times, process will be terminated')
                         print('='*68)
                         exit()
            SupplierCode=(input('Enter supplier code from S1, S2, S3, S4: ')).upper()
            if not SupplierCode == "S1" and not SupplierCode == "S2" and not SupplierCode == "S3" and not SupplierCode == "S4":
                 print("\n"+"Supplier Code must be from S1, S2, S3, S4"+"\n"+"\nPlease try it again!!"+"\n")
                 SupplierCode = (input('Enter supplier code from S1, S2, S3, S4: ')).upper()
                 if not SupplierCode == "S1" and not SupplierCode == "S2" and not SupplierCode == "S3" and not SupplierCode == "S4":
                         print('\n Invalid option entered too many times, process will be terminated')
                         print('='*68)
                         exit()
            Amount=input('Enter first amount: ')
            if not Amount == "100":
                    print("\nIntial amount should be 100...Please try it again!!\n")
                    Amount=input('Enter first amount: ')
                    if not Amount == "100":
                          print('\n Invalid option entered too many times, process will be terminated')
                          print('='*68)
                          exit()
            f.write("Item:"+"	"+ItemCode.upper()+"	"+"Supplier:"+"	"+SupplierCode.upper()+"	"+"Amount:"+"	"+Amount+"	"+"\n")
            if n == 6:
                f.close()
                print("\nNow initial inventory is created!!\n") #inventory successfully
                Twochoices()

                    
def UpdateInventory():#function to adds stock in inventory
    ItemCode = (input('Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')).upper()
    if not ItemCode == "HC"and not ItemCode == "FS" and not ItemCode == "MS" and not ItemCode == "GL" and not ItemCode == "GW" and not ItemCode == "SC":
        print("\n"+"Item code must be from 'HC','FS','MS','GL','GW','SC'"+"\n"+"\nPlease try it again!!"+"\n")
        ItemCode = (input('Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')).upper()
        if not ItemCode == "HC"and not ItemCode == "FS" and not ItemCode == "MS" and not ItemCode == "GL" and not ItemCode == "GW" and not ItemCode == "SC":
                print('\n Invalid option entered too many times, process will be terminated')
                print('='*68)
                exit()
    Amount = input('How many do you want to add to inventory?  Enter quantity: ') #asking input from user about amount to add in inventory
    while Amount.isnumeric() == False:
            n=0
            while n < 1:
                n = n + 1
                print("\nSorry quantity should be number"+"\nPlese try it again!!\n")
                Amount = input('\nHow many do you want to deliver?  Enter quantity: ')
            if Amount.isnumeric() == True:
                break
            else:
                print('\n Invalid option entered too many times, process will be terminated')
                print('='*68)
                exit()
    f = open('ppe.txt','r+') #opening file to read
    Update = f.readlines()
    for i, line in enumerate(Update):
        if ItemCode in line:
            for b in Update[i:i+1]:
                if ItemCode == "HC": # updating the amount of head cover
                   Supplier = line[19:21]
                   Current = line[-5:]
                   Change = str(Current)
                   FinalAmount = int(Amount)+int(Current)
                   Finish = str(FinalAmount)
                   f.seek(30)
                   f.write(Finish)
                   with open('distributions.txt',"a") as f: #opening file for append
                       f.write('Item:HC ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n")
                       f.write('='*50+"\n")
                       
                elif ItemCode == "FS": # updating the amount of face shield
                     Supplier = line[19:21]
                     Current = line[-5:]
                     Change = str(Current)
                     FinalAmount = int(Amount)+int(Current)
                     Finish = str(FinalAmount)
                     f.seek(65)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                       f.write('Item:FS ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n")
                       f.write('='*50+"\n")
                elif ItemCode == "MS": # updating the amount of mask
                     Supplier = line[19:21]
                     Current = line[-5:]
                     Change = str(Current)
                     FinalAmount = int(Amount)+int(Current)
                     Finish = str(FinalAmount)
                     f.seek(100)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                       f.write('Item:MS ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n")
                       f.write('='*50+"\n")
                elif ItemCode == "GL": # updating the amount of gloves
                     Supplier = line[19:21]
                     Current = line[-5:]
                     Change = str(Current)
                     FinalAmount = int(Amount)+int(Current)
                     Finish = str(FinalAmount)
                     f.seek(135)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                       f.write('Item:GL ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n")
                       f.write('='*50+"\n")
                elif ItemCode == "GW": # updating the amount of gown
                     Supplier = line[19:21]
                     Current = line[-5:]
                     Change = str(Current)
                     FinalAmount = int(Amount)+int(Current)
                     Finish = str(FinalAmount)
                     f.seek(170)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                       f.write('Item:GW ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n")
                       f.write('='*50+"\n")
                elif ItemCode == "SC": # updating the amount of shoes cover
                     Supplier = line[19:21]
                     Current = line[-5:]
                     Change = str(Current)
                     FinalAmount = int(Amount)+int(Current)
                     Finish = str(FinalAmount)
                     f.seek(205)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                       f.write('Item:SC ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n")
                       f.write('='*50+"\n")
            f.close()
            print("Now the file has more content!\n")
            n = 0
            while n < 2:
                n = n+1
                FinalChoice = str(input("Do you want to contiue??\n"+"Enter your choice...1 for yes,0 for No: ")) #asking input from user
                if FinalChoice == "1":
                        UpdateInventory()
                elif FinalChoice == "0":
                        Twochoices()
                else:
                    print("\ninvalid value try it again!!\n")
            if n == 2:
                  print('\n Invalid option entered too many times, process will be terminated')
                  print('='*68)
                  exit()
    




def Distribute(): #funtion to distribute the items to hospitals
    ItemCode = (input('Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')).upper()
    if not ItemCode == "HC"and not ItemCode == "FS" and not ItemCode == "MS" and not ItemCode == "GL" and not ItemCode == "GW" and not ItemCode == "SC":
        print("\n"+"Item code must be from 'HC','FS','MS','GL','GW','SC'"+"\n"+"\nPlease try it again!!"+"\n")
        ItemCode = (input('Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')).upper()
        if not ItemCode == "HC"and not ItemCode == "FS" and not ItemCode == "MS" and not ItemCode == "GL" and not ItemCode == "GW" and not ItemCode == "SC":
                print('\n Invalid option entered too many times, process will be terminated')
                print('='*68)
                exit()
    Hospital = str((input('Enter hospital code that you want to deliver from H1,H2,H3,H4: ')).upper())#asking user to choose hospital for distributing
    if not Hospital == "H1" and not Hospital == "H2" and not Hospital == "H3" and not Hospital == "H4":
        print("\nHospital code should be from from H1,H2,H3,H4...\n"+"\nPlease try it again!!\n")
        Hospital = str((input('Enter hospital code that you want to deliver from H1,H2,H3,H4: ')).upper())
        if not Hospital == "H1" and not Hospital == "H2" and not Hospital == "H3" and not Hospital == "H4":
                print('\n Invalid option entered too many times, process will be terminated')
                print('='*68)
                exit()
    Amount = input('How many do you want to deliver?  Enter quantity: ')#aking quantity for distributing
    while Amount.isnumeric() == False:
            n=0
            while n < 1:
                n = n + 1
                print("\nSorry quantity should be number"+"\nPlese try it again!!\n")
                Amount = input('\nHow many do you want to deliver?  Enter quantity: ')
            if Amount.isnumeric() == True:
                break
            else:
                print('\n Invalid option entered too many times, process will be terminated')
                print('='*68)
                exit()
    f = open('ppe.txt','r+')#opening file to read
    Update = f.readlines()
    for i, line in enumerate(Update):
        if ItemCode in line:
            for b in Update[i:i+1]:
                if ItemCode == "HC":# shipping the amount of Head Cover
                   Supplier = line[19:21]
                   Current = line[-5:]
                   if int(Amount) > int(Current):
                       print("\nSorry...HC/Head Cover stock is only "+Current+"\nPlease try it again from start!!\n")
                       Distribute()
                   Change = str(Current)
                   FinalAmount = int(Current)-int(Amount)
                   Finish = str(FinalAmount)+" "
                   f.seek(30)
                   f.write(Finish)
                   with open('distributions.txt',"a") as f: #opening file for append
                       f.write('Item:HC ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n"+"Delivered Hospital:"+Hospital+"\n")
                       f.write('='*50+"\n")
                       
                elif ItemCode == "FS":# shipping the amount of face shield
                     Supplier = line[19:21]
                     Current = line[-5:]
                     if int(Amount) > int(Current):
                         print("\nSorry...FS/Face Shield stock is only "+Current+"\nPlease try it again from start!!\n")
                         Distribute()
                     Change = str(Current)
                     FinalAmount = int(Current)-int(Amount)
                     Finish = str(FinalAmount)+" "
                     f.seek(65)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                         f.write('Item:FS ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n"+"Delivered Hospital:"+Hospital+"\n")
                         f.write('='*50+"\n")
                elif ItemCode == "MS":# shipping the amount of mask
                     Supplier = line[19:21]
                     Current = line[-5:]
                     if int(Amount) > int(Current):
                         print("\nSorry...MS/Mask is stock only "+Current+"\nPlease try it again from start!!\n")
                         Distribute()
                     Change = str(Current)
                     FinalAmount = int(Current)-int(Amount)
                     Finish = str(FinalAmount)+" "
                     f.seek(100)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                         f.write('Item:MS ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n"+"Delivered Hospital:"+Hospital+"\n")
                         f.write('='*50+"\n")
                elif ItemCode == "GL":# shipping the amount of gloves
                     Supplier = line[19:21]
                     Current = line[-5:]
                     if int(Amount) > int(Current):
                         print("\nSorry...GL/Gloves is stock only "+Current+"\nPlease try it again from start!!\n")
                         Distribute()
                     Change = str(Current)
                     FinalAmount = int(Current)-int(Amount)
                     Finish = str(FinalAmount)+" "
                     f.seek(135)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                         f.write('Item:GL ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n"+"Delivered Hospital:"+Hospital+"\n")
                         f.write('='*50+"\n")
                elif ItemCode == "GW":# shipping the amount of gown
                     Supplier = line[19:21]
                     Current = line[-5:]
                     if int(Amount) > int(Current):
                         print("\nSorry...GW/Gown is stock only "+Current+"\nPlease try it again from start!!\n")
                         Distribute()
                     Change = str(Current)
                     FinalAmount = int(Current)-int(Amount)
                     Finish = str(FinalAmount)+" "
                     f.seek(170)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                         f.write('Item:GW ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n"+"Delivered Hospital:"+Hospital+"\n")
                         f.write('='*50+"\n")
                elif ItemCode == "SC":# shipping the amount shoes cover
                     Supplier = line[19:21]
                     Current = line[-5:]
                     if int(Amount) > int(Current):
                         print("\nSorry...SC/Shoe Cover stock is only "+Current+"\nPlease try it again from start!!\n")
                         Distribute()
                     Change = str(Current)
                     Change = str(Current)
                     FinalAmount = int(Current)-int(Amount)
                     Finish = str(FinalAmount)+" "
                     f.seek(205)
                     f.write(Finish)
                     with open('distributions.txt',"a") as f: #opening file for append
                         f.write('Item:SC ' +"Supplier:"+Supplier+" "+ "Added quantity:"+str(Amount)+"\n"+"Delivered Hospital:"+Hospital+"\n")
                         f.write('='*50+"\n")
            f.close()
            print("Distribution was completed!!\n")
            n = 0
            while n < 2:
                n = n+1
                FinalChoice = str(input("Do you want to contiue??\n"+"Enter your choice...1 for yes,0 for No: "))#asking input from user
                if FinalChoice == "1":
                        Distribute()
                elif FinalChoice == "0":
                        Twochoices()
                else:
                    print("\ninvalid value try it again!!\n")
            if n == 2:
                  print('\n Invalid option entered too many times, process will be terminated')
                  print('='*68)
                  exit()
                       
                
def less_than_25Stock():#search function which items are less than 25
    with open('ppe.txt','r')as file:#opening file to read
        linelist= file.readlines()
        low_stock=[]
        for line in linelist:
            line=line.split('\t')
            if (int(line[5])<25):
                line='\t'.join(line)
                print("\n"+line)#print less then 25 item and amount of stock 
                low_stock.append(line)
                Twochoices()
        if low_stock==[]:
            print('\nThere is no item less than 25')
            Twochoices()


def ShowAll():#function for indicating all stock in inventory
    f = open('ppe.txt', 'r')
    ItemRead = f.readline()
    print("\n"+"="*14+"\n"+'Present Stock'+"\n"+"="*14)
    while ItemRead != '':
        ItemAmount = f.readline()
        ItemRead = ItemRead.rstrip('\n')
        ItemAmount = ItemAmount.rstrip('\n')
        print(ItemRead)
        print(ItemAmount)
        ItemRead = f.readline()
    f.close()
    Twochoices()

    
def searchInventory():#search function of item stock by item code
    ItemCode = (input('Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')).upper()#asking user to enter item code for searching
    if not ItemCode == "HC"and not ItemCode == "FS" and not ItemCode == "MS" and not ItemCode == "GL" and not ItemCode == "GW" and not ItemCode == "SC":
        print("\n"+"Item code must be from 'HC','FS','MS','GL','GW','SC'"+"\n"+" Please try it again!!"+"\n")
        ItemCode = (input('Enter item code from HC/Head Cover, FS/Face Shield, MS/Mask, GL/Gloves, GW/Gown, SC/Shoe Cover: ')).upper()
        if not ItemCode == "HC"and not ItemCode == "FS" and not ItemCode == "MS" and not ItemCode == "GL" and not ItemCode == "GW" and not ItemCode == "SC":
            print('\n Invalid option entered too many times, process will be terminated')
            print('='*68)
            exit()       
    f = open('ppe.txt', 'r')#opening file to read
    search = f.readlines()
    f.close()
    for i, line in enumerate(search):
        if ItemCode in line:
            for b in search[i:i+1]:
                if ItemCode == "HC":# printing the amount of Head Cover
                    print("\n"+"HC/Head Cover:"+line[-5:])
                elif ItemCode == "FS":# printing the amount of Face Shield
                    print("\n"+"FS/Face Shield:"+line[-5:])
                elif ItemCode == "MS":# printing the amount of Mask
                    print("\n"+"MS/Mask:"+line[-5:])
                elif ItemCode == "GL":# printing the amount of Gloves
                    print("\n"+"GL/Gloves:"+line[-5:])
                elif ItemCode == "GW":# printing the amount of Gown
                    print("\n"+"GW/Gown:"+line[-5:])
                elif ItemCode == "SC":# printing the amount of Shoe Cover
                    print("\n"+"SC/Shoe Cover:"+line[-5:])
    n = 0
    while n < 2:
        n = n+1
        FinalChoice = str(input("Do you want to contiue??\n"+"Enter your choice...1 for yes,0 for No: "))#asking input from user
        if FinalChoice == "1":
            searchInventory()
        elif FinalChoice == "0":
                Twochoices()
        else:
            print("\ninvalid value try it again!!\n")
    if n == 2:
          print('\n Invalid option entered too many times, process will be terminated')
          print('='*68)
          exit()
            
                
def WelcomePage():#user can choose functions form 9 choices at first
    n = 0
    while n < 2:
        n = n+1
        print("="*55+'\n  Hello and welcome to the Inventory Managment system\n'+"="*55)
        print("1 -Register Supplier information")
        print("2 -Register Hospital information")
        print("3 -Initial amount of inventory")
        print("4 -Update amount to inventory")
        print("5 -Distribute Item to Hospital")
        print("6 -Display Item less than 25")
        print("7 -Display All inventory")
        print("8 -Search by item code")
        print("9 -Exit")
        YourChoice = str(input("Please Enter your choice: "))
        if YourChoice == '9':
            print("Thank you bye bye")
            exit()
        elif YourChoice == '1':#calling function of Register Supplier information
            supplier_info()
        elif YourChoice == '2':#calling function of Register Hospital information
            hospital_info()
        elif YourChoice == '3':#calling function of Initial amount of inventory
            initial_amount_of_inventory()
        elif YourChoice == '4':#calling function of Update amount to inventory
            UpdateInventory()
        elif YourChoice == '5':#calling function of Distribute Item to Hospital
            Distribute()
        elif YourChoice == '6':#calling function of Display Item less than 25
            less_than_25Stock()
        elif YourChoice == '7':#calling function of Display All inventory
            ShowAll()
        elif YourChoice == '8':#calling function of Search by item code
            searchInventory()
        else:
            print('Invalid Input,your chice should be a number from 1,2,3,4,5,6,7,8,9.\nPlease try it again!!\n\n')
    if n == 2:
          print('\n Invalid option entered too many times, process will be terminated')
          print('='*68)
          exit()
login()
WelcomePage()

