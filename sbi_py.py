#       ------------------------ Online Banking simulation system --------------------------- 
import sys
import pandas as pd
import random
from datetime import date
try:
    
    x1 = str(date.today())
    x2 = random.randint(111111111111,999999999999)
    x3 = []
   
    flag = True
    while(flag):
        title = 'Welcome to State Bank of India'
        print(title.center(100,'*'))
        print('1).Create Account')
        print('2).Login')
        print('3).Exit')
        i = int(input('Enter your Preferred choice [1/2/3] =  '))
        if i in [1,2,3]:
            if i == 1:
                title = input('*********** Create Account ***********')
                a = input('Enter your Name =  ')
                b = (input('Enter your Gender [Male/Female/Other] = '))
                c = int(input('Enter your adhaar ID =  '))
                d = int(input('Enter your Phone number =  '))
                e = input('Enter your Address =   ')
                x3 = input('Enter emailID =  ')
                f2 = input('Enter your Account type [C/S] =   ')
                pwd = input('Enter Password =  ')
                con_pwd = input('confirm Password =  ')
                if con_pwd == pwd:
                    with open(f'C:\\Users\\GANESH THORBOLE\\OneDrive\\Desktop\\Banking system\\RegDet\\{x2}.txt','w') as f:
                        f.write(x3 + '\n')
                        f.write(pwd)
                    f.close()
                    print('you had registered successfully')
                else:
                    print('Please enter valid password')
                g = int(input('Enter the amount (not less than 500) ₹ =  '))
                if g > 500:
                    g = str(g) 
                    BalDet = str(x2) 
                    with open(f'C:\\Users\\GANESH THORBOLE\\OneDrive\\Desktop\\Banking system\\BalDet\\{BalDet}.txt','w') as f:
                        f.write(g)
                    f.close()
                   
                else:
                    print('invalid amount entered please try again')
                print('----------------------------------------------------------------------------------------------------------------- \n')
                print('**************** Account Successfully Created ****************')
                print('****************  Your Account Details ****************')
                print(f'Account No = {x2}')
                print(f'Your Name = {a}')
                print(f'Your gender [Male/Female/others] = {b}')
                print(f'Your adhaar number [ID] = {c}')
                print(f'Your Phone number = {d}')
                print(f'Your Full Address = {e}')
                print(f'Your Email - ID = {x3}')
                print(f'Your account Type = {f2}')  
                print('------------------------------------------------------------------------------------------------------------------ \n')
                user_info = str(x2) 
                with open(f'C:\\Users\\GANESH THORBOLE\\OneDrive\\Desktop\\Banking system\\UserDet\\{user_info}.txt','w') as f:
                    f.write(f'------------------------------------------------------------ \n')
                    f.write(f'****************  Your Account Details **************** \n')
                    f.write(f'Account No = {x2} \n')
                    f.write(f'Your Name = {a} \n')
                    f.write(f'Your gender [Male/Female/Others] = {b} \n')
                    f.write(f'Your adhaar number [ID] = {c} \n')
                    f.write(f'Your Phone number = {d} \n')
                    f.write(f'Your Full address = {e} \n')
                    f.write(f'your account type = {f2} \n')
                    f.write(f'------------------------------------------------------------  \n')
                    f.close()
            elif i == 2:
                print('************* Login Details *************')
                Account_no = int(input('Enter your Account number =  '))
                stored_email = input('Enter Email ID = ')
                pwd = input('Enter password =   ')
                con_pwd = input('confirm password =  ')
                if x3 == stored_email and pwd == con_pwd:
                    print(f'**************** Successful Login  **************** \n')
                    print(f'--------------------------------------------------------------------- \n')
                    print(f'--------------- Your Detailed Bank Account information --------------- \n')
                    print(f' 1]. Check Balance  \n')
                    print(f' 2]. Amount Deposit \n')
                    print(f' 3]. Amount Withdraw \n')
                    print(f' 4]. Bank Transactions \n')
                    print(f' 5]. Log out  \n')
                    print(f'-------------------------------------------------------------- \n')
                    while True:
                        choice = int(input('Enter choice [1/2/3/4/5]   =  '))
                        if choice in [1,2,3,4,5]:    
                            if choice == 1:
                                print('-------------- Check Balance ------------------')
                                with open(f'C:\\Users\\GANESH THORBOLE\\OneDrive\\Desktop\\Banking system\\BalDet\\{BalDet}.txt','r') as f:
                                    print(f'********* Your Balance Details ********* \n Your account no =  {BalDet}','₹',f.read())                                   
                            elif choice == 2:
                                    print('-------------- Deposit Amount ---------------')
                                    j = int(input('Enter the Deposit amount ₹ =   '))
                                    g = int(g)
                                    j = int(j)
                                    g += j
                                    print(f'Total amount deposited = ₹ {j}')
                                    print(f'Total Balance in your bank account = ₹ {g}')
                                    with open(f'C:\\Users\\GANESH THORBOLE\\OneDrive\\Desktop\\Banking system\\BalDet\\{BalDet}.txt','w') as f:
                                        f.write(str(g))
                                        print(f'********* Your Balance Details ********* \n Your account no =  {BalDet} \n Total Balance = ₹ {g} \n Total amount Deposited = ₹ {j}')
                                    f.close()          
                            elif choice == 3:
                                    print('------------------ Withdraw Amount ------------------')      
                                    h = int(input('Enter the withdrawal amount ₹ =   '))
                                    g = int(g)
                                    h = int(h)
                                    g -= h
                                    print(f'Total amount withdrawal = ₹ {h}')
                                    print(f'Total Balance Remained in your bank account = ₹ {g}')
                                    with open(f'C:\\Users\\GANESH THORBOLE\\OneDrive\\Desktop\\Banking system\\BalDet\\{BalDet}.txt','w') as f:
                                        f.write(str(g))
                                        print(f'********* Your Balance Details ********* \n Your account no =  {BalDet} \n Total Balance Remained = ₹ {g} \n Total amount withdrawal = ₹ {h}')
                                        f.close()
                            elif choice == 4:
                                print('------------------ Transaction Statement ------------------')
                                firstDeposit = int(j)
                                print(f' Total amount Deposited in Rs = {firstDeposit}')
                                firstwithdraw= int(h)
                                print(f' Total amount withdraw in Rs = {firstwithdraw}')
                                Total_Balance = str(g)
                                print(f' Total balance in your account in Rs = {Total_Balance}')
                                df = pd.DataFrame({'Full name':[a],'Account no':[BalDet],'Total amount Deposited in Rs ₹': [firstDeposit],'Total amount withdrawed in Rs ₹': [firstwithdraw],'Current Balance in Rs ₹':[Total_Balance],'Dated':[x1]})
                                writer = pd.ExcelWriter(f'C:\\Users\\GANESH THORBOLE\\OneDrive\\Desktop\\Banking system\\StateDet\\{x2}.xlsx', engine='xlsxwriter')
                                df.to_excel(writer, sheet_name='Sheet1', index=False)
                                writer.close()
                                print('-----------------------------------------------------------')   
                            elif choice == 5:
                                print(f'---------------------------------- \n Logged Out \n -----------------------------------')
                                break
                else:
                    print(f'----------------------------- \n Login Failed Please Try Again \n ---------------------------------------')
                    
            elif i == 3:
                    print(f'---------------------------------------------------- \n Thanks for using our bank management system,have a nice day!!!!!!! \n ---------------------------------------------------------------')
                    sys.exit() 
except BaseException as ex:
    print(ex)


