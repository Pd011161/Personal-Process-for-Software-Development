#Description of this Program
#Author : Predee Chaiyakit
#Since : 2021-07-27
#Program Name : Read & Write File04
#Program Languagu : Python
#Program Purpose : practice programming skills

#Modify : 2021-07-27
#Modify Description : Use Try except. 
#Modify by : Predee Chaiyakit
def main():#Function Menu
    def CheckName():#Function to check whether you want to continue or not.
        print("-----------------\nกรุณาใส่ตัวเลข\n-----------------")
        print("ต้องการดำเนินการต่อหรือไม่")
        print("1: ดำเนินการต่อ")
        print("2: ยกเลิกการดำเนินการ")
        inp = int(input(": "))#get alternative input.
        if inp == 1:#check conditions.
            CreateFile()#Declare a function to create a file.
        elif inp == 2:#check conditions.
            pass
        else:
            CheckName()#Declare a function to check if you want to continue.
    
    def CheckChoice():#Function to check whether you want to continue or not.
        print("-----------------\nกรุณาเลือกโหมดให้ถูกต้องระหว่าง 1-7\n-----------------")
        print("ต้องการดำเนินการต่อหรือไม่")
        print("1: ดำเนินการต่อ")
        print("2: ปิดโปรแกรม")
        inp = int(input(": "))#get alternative input.
        print("-----------------\n")
        if inp == 1:#check conditions
            main()#Use the function to return to main.
        elif inp == 2:#check conditions
            print("-----------------\nปิดการใช้งาน\n-----------------\n")
        else:
            CheckChoice()#Declare a function to check if you want to continue.
    
    def CheckText():#Function to check whether you want to continue or not.
        print("-----------------\nกรุณาใส่ตัวเลข\n-----------------")
        print("ต้องการดำเนินการต่อหรือไม่")
        print("1: ดำเนินการต่อ")
        print("2: ยกเลิกการดำเนินการ")
        inp = int(input(": "))#get alternative input.
        print("-----------------\n")
        if inp == 1:#check conditions.
            run = True
            return run
        elif inp == 2:#check conditions.
            print("-----------------\nปิดการใช้งาน\n-----------------\n")
            run = False
            return run
        else:
            CheckText()#Declare a function to check if you want to continue.
    
    def CheckAdd():#Function to check whether you want to continue or not.
        print("-----------------\nกรุณาใส่ตัวเลข\n-----------------")
        print("ต้องการดำเนินการต่อหรือไม่")
        print("1: ดำเนินการต่อ")
        print("2: ยกเลิกการดำเนินการ")
        inp = int(input(": "))#get alternative input.
        if inp == 1:#check conditions.
            AddFile()#Declare function add his information to the file
        elif inp == 2:
            main()#Use the function to return to main.
        else:
            CheckAdd()#Declare a function to check if you want to continue.
    
    def CheckRead():#Function to check whether you want to continue or not.
        print("-----------------\nกรุณาใส่ตัวเลข\n-----------------")
        print("ต้องการดำเนินการต่อหรือไม่")
        print("1: ดำเนินการต่อ")
        print("2: ยกเลิกการดำเนินการ")
        inp = int(input(": "))#get alternative input.
        if inp == 1:#check conditions.
            ReadFile()#Declare use a function to read a file.
        elif inp == 2:#check conditions.
            pass
        else:
            CheckRead()#Declare a function to check if you want to continue.
            
    def CheckReplace():#Function to check whether you want to continue or not.
        print("-----------------\nกรุณาใส่ตัวเลข\n-----------------")
        print("ต้องการดำเนินการต่อหรือไม่")
        print("1: ดำเนินการต่อ")
        print("2: ยกเลิกการดำเนินการ")
        inp = int(input(": "))#get alternative input.
        if inp == 1:#check conditions.
            ReplaceFile()#Declare use a function to overwrite the file
        elif inp == 2:#check conditions.
            main()#Use the function to return to main.
        else:
            CheckReplace()#Declare a function to check if you want to continue.          
            
            
    def CreateFile():#Function to create a file.
        print("-----------------")
        print("โหมดสร้างไฟล์")
        name = input("ชื่อไฟล์: ")#get input filename
        try:
            f = open(name+".txt","x")#open file.
            f.close()#close file.
        except:
            print("-----------------\nเกิดข้อผิดพลาด")
            print("1.มีชื่อไฟล์ที่ระบุอยู่แล้ว\n2.มีอักขระเหล่านี้อยู่: \ / : * ? \" < > |\n-----------------\n")
            CheckName()#Declare a function to check if you want to continue.
    
    def AddFile():#Function add data to file.
        print("-----------------")
        print("โหมดเขียนข้อมูล")
        name = input("ชื่อไฟล์: ")#get input filename
        run = True
        data = []
        try:
            f= open(name+".txt", "a+")
        except:
            print("-----------------\nเกิดข้อผิดพลาด")
            print("1.มีอักขระเหล่านี้อยู่: \ / : * ? \" < > |\n-----------------\n")
            CheckAdd()#Declare a function to check if you want to continue.   
            
        
        while run:#loop to get data values.
            print("กรุณาใส่ตัวเลข หรือ 'e' เพื่อหยุด")
            inp = input("ใส่ตัวเลข: ")#get input data.
            if inp.isnumeric():#Check if the data is numeric.
                data.append(inp)#Add his information to the data.
            elif inp == 'e':#Check if it's an e to go to the next step.
                def CheckE(arr):#Function to check whether you want to continue or not.
                    print("-----------------\nยืนยันการดำเนินการ(Y/N)\n-----------------")
                    check = (input("(Y/N): ").isupper)#Take the input and change it to uppercase.
                    if check == 'Y':#check conditions.
                        for i in arr:#Loop through the values ​​to write to the file.
                            f.write(i+"\n")#write data to file.
                    elif check == 'N':#check conditions.
                        run = False
                        return run
                    else:
                        CheckE(arr)#Declare a function to check if you want to continue.
                run = CheckE(data)        
            else:
                run = CheckText()
        f.close()#close file.

    def ReadFile():#function to read files
        print("-----------------")
        print("โหมดอ่านข้อมูล")
        name = input("ชื่อไฟล์: ")#get input filename
        try:
            f= open(name+".txt", "r")#open file
            print("-----------------")
            for i in f:#Looping data from a file
                print(i)#show information
            print("-----------------\n") 
        except:
            print("-----------------\nไม่พบไฟล์ดังกล่าว\n-----------------")
            CheckRead()#Declare a function to check if you want to continue.่
                    
    def Acceptfile():#Function to accept files.
        print("-----------------")
        print("ยอมรับ")
        print("-----------------\n")  
        
    def ReplaceFile():#Function to overwrite files.
        print("-----------------")
        print("โหมดเขียนทับข้อมูล")
        name = input("ชื่อไฟล์: ")#get input filename.
        run = True
        data = []
        try:
            f= open(name+".txt", "w")#open file
        except:
            print("-----------------\nเกิดข้อผิดพลาด")
            print("1.มีอักขระเหล่านี้อยู่: \ / : * ? \" < > |\n-----------------\n")
            CheckReplace()
        
        while run:#Loop to get data values.
            print("กรุณาใส่ตัวเลข หรือ 'e' เพื่อหยุด")
            inp = input("ใส่ตัวเลข: ")#get input data.
            if inp.isnumeric():#Check if the data is numeric or not.
                data.append(inp)#Add his information to the data.
            elif inp == 'e':#Check conditions.
                def CheckE(arr):#Declare a function to check if you want to continue.
                    print("-----------------\nยืนยันการดำเนินการ(Y/N)\n-----------------")
                    check = input("(Y/N): ")#Get input to continue
                    if check == 'Y':#Check conditions.
                        for i in arr:#Loop through the values ​​to write to the file.
                            f.write(i+"\n")#Write data to file
                    elif check == 'N':#Check conditions.
                        run = False
                        return run
                    else:
                        CheckE(arr)#Declare a function to check if you want to continue.
                run = CheckE(data)            
            else:
                run = CheckText()                
        f.close()#close file.
    
    def DeleteFile():#Function delete file.
        print("-----------------")
        print("โหมดลบข้อมูล")
        name = input("ชื่อไฟล์: ")#get input filename.
        f= open(name+".txt", "w")#open file.
        f.write("")#delete data in file.
      
  
    print("เลือกโหมดที่ใช้งาน \n1.สร้างไฟล์ \n2.เขียนไฟล์ \n3.เขียนทับไฟล์ \n4.อ่านไฟล์ \n5.ยอมรับไฟล์ \n6.ลบข้อมูล \n7.ปิดการใช้งาน")
    menu = input("เลือกโหมด: ")#get input to select the mode of use.
    if menu == '1':#Check conditions.
        CreateFile()#Declare a function to create a file.
        main()#Use the function to return to main.
    elif menu == '2':#Check conditions.
        AddFile()#Declaration function  to the data into the file
        main()#Use the function to return to main.
    elif menu == '3':#Check conditions.
        ReplaceFile()#Declare the function overwrite the file.
        main()#Use the function to return to main.
    elif menu == '4':#Check conditions.
        ReadFile()#Function declaration to read the file
        main()#Use the function to return to main.
    elif menu == '5':#Check conditions.
        Acceptfile()#Declaration function to accept the file
    elif menu == '6':#Check conditions.
        DeleteFile()#Declaration function to delete the data in the file
        main()#Use the function to return to main.
    elif menu == '7':#Check conditions.
        print("-----------------")
        print("ปิดการใช้งาน")
        print("-----------------\n")
    else:
        CheckChoice()#Declare a function to check if you want to continue.
    
    
main()#Declare use the program.
