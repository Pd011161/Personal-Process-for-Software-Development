#Description of this Program
#Author : Predee Chaiyakit
#Since : 2021-05-06
#Program Name : Read & Write File
#Program Languagu : Python
#Program Purpose : practice programming skills
def main():#Function Menu
    def createfile(name):#Function to create a file.
        f = open(name+".txt","w+")#open file.
        f.close()#close file.
    
    def AddFile(name):#Function to add data to file.
        run = True
        f= open(name+".txt","a+")#open file.
        while run:#loop to get data values.
            print("กรุณาใส่ตัวเลข หรือ 'e' เพื่อหยุด")
            inp = input("ใส่ตัวเลข: ")#get input data.
            if inp.isnumeric():#Check if the data is numeric.
                f.write(inp)
                f.write("\n")
            elif inp == 'e':#Check conditions.
                run = False
            else:#Check conditions.
                print("ใส่ให้ถูก")
        f.close()

    def ReadFile(name):#function to read files
        f= open(name+".txt", "r")
        print("-----------------")
        for i in f:#Looping data from a file
            print(i)#show information
        print("-----------------\n") 
        
    def Acceptfile():#Function to accept files.
        print("-----------------")
        print("ยอมรับ")
        print("-----------------\n")  
        
    def Replacefile(name):#Function to overwrite files.
        run = True
        f= open(name+".txt", "w")#open file
        while run:
            print("กรุณาใส่ตัวเลข หรือ 'e' เพื่อหยุด")
            inp = input("ใส่ตัวเลข: ")#get input data.
            if inp.isnumeric():#Check if the data is numeric or not.
                f.write(inp)
                f.write("\n")
            elif inp == 'e':#Check conditions.
                run = False
            else:#Check conditions.
                print("ใส่ให้ถูก")
        f.close()
    
    def DeleteFile(name):#Function delete file.
        f= open(name+".txt", "w")#open file.
        f.write("")#delete data in file.
    
    print("เลือกโหมดที่ใช้งาน \n1.สร้างไฟล์ \n2.เขียนไฟล์ \n3.เขียนทับไฟล์ \n4.อ่านไฟล์ \n5.ยอมรับไฟล์ \n6.โหมดลบข้อมูล \n7.ปิดการใช้งาน")
    menu = input("เลือกโหมด: ")
    if menu == '1':#Check conditions.
        print("-----------------")
        print("โหมดสร้างไฟล์")
        name = input("ชื่อไฟล์: ")#get input file name.
        createfile(name)#Declare a function to create a file.
        main()#Use the function to return to main.
    elif menu == '2':#Check conditions.
        print("-----------------")
        print("โหมดเขียนข้อมูล")
        name = input("ชื่อไฟล์: ")#get input file name.
        AddFile(name)#Declare use a function to add data to the file
        main()#Use the function to return to main.
    elif menu == '3':#Check conditions.
        print("-----------------")
        print("โหมดเขียนทับข้อมูล")
        name = input("ชื่อไฟล์: ")#get input file name.
        Replacefile(name)#Declare use a function to overwrite the file
        main()#Use the function to return to main.
    elif menu == '4':#Check conditions.
        print("-----------------")
        print("โหมดอ่านข้อมูล")
        name = input("ชื่อไฟล์: ")#get input file name.
        ReadFile(name)#Declare use a function to read the file
        main()#Use the function to return to main.
    elif menu == '5':#Check conditions.
        Acceptfile()#Declare use a function to accept files.
    elif menu == '6':#Check conditions.
        print("-----------------")
        print("โหมดลบข้อมูล")
        name = input("ชื่อไฟล์: ")#get input file name.
        DeleteFile(name)#Declare use a function delete file.
        main()#Use the function to return to main.
    elif menu == '7':#Check conditions.
        print("-----------------")
        print("ปิดการใช้งาน")
        print("-----------------\n")
    else:#Check conditions.
        print("-----------------")
        print("ไม่มีโหมดที่เลือก")
        print("-----------------\n")
        main()#Use the function to return to main.
    
    
main()#Declare use the program.
