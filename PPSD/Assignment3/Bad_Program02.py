def createfile(name):           
    f = open(name+".txt","w+")  
    f.close()                   
def AddFile(name):                          
    run = True                              
    f= open(name+".txt","a+")               
    while run:                              
        print("กรุณาใส่ตัวเลข หรือ 'e' เพื่อหยุด")  
        inp = input("ใส่ตัวเลข: ")                       
        if inp.isnumeric():                 
            f.write(inp)                    
            f.write("\n")                   
        elif inp == 'e':                    
            run = False                     
        else:                               
            print("ใส่ให้ถูก")                 
    f.close()                               
def ReadFile(name):              
    f= open(name+".txt", "r")    
    print("-----------------")   
    for i in f:                  
         print(i)                
    print("-----------------\n")        
def Acceptfile():                    
    print("-----------------")       
    print("ยอมรับ")                   
    print("-----------------\n")     
def Replacefile(name):                      
    run = True                              
    f= open(name+".txt", "w")               
    while run:                              
        print("กรุณาใส่ตัวเลข หรือ 'e' เพื่อหยุด")  
        inp = input("ใส่ตัวเลข: ")            
        if inp.isnumeric():                 
            f.write(inp)                    
            f.write("\n")                   
        elif inp == 'e':                    
            run = False                     
        else:                               
            print("ใส่ให้ถูก")              
    f.close()                               
def DeleteFile(name):                                                                                               # 
    f= open(name+".txt", "w")                                                                                       #
    f.write("")                                                                                                     #
print("เลือกโหมดที่ใช้งาน \n1.สร้างไฟล์ \n2.เขียนไฟล์ \n3.เขียนทับไฟล์ \n4.อ่านไฟล์ \n5.ยอมรับไฟล์ \n6.โหมดลบข้อมูล \n7.ปิดการใช้งาน")    #
menu = input("เลือกโหมด: ")                                                                                          #
if menu == '1':                                                                                                     #
        print("-----------------")                                                                             
        print("โหมดสร้างไฟล์")                                                                                             
        name = input("ชื่อไฟล์: ")                                                                                     
        createfile(name)                                                                                           
        main()                                                                                                     
elif menu == '2':                                                                                                   
        print("-----------------")  
        print("โหมดเขียนข้อมูล")       
        name = input("ชื่อไฟล์: ")    
        AddFile(name)
        main()
elif menu == '3':
        print("-----------------")
        print("โหมดเขียนทับข้อมูล")
        name = input("ชื่อไฟล์: ")
        Replacefile(name)
        main()
elif menu == '4':
        print("-----------------")
        print("โหมดอ่านข้อมูล")
        name = input("ชื่อไฟล์: ")
        ReadFile(name)
        main()
elif menu == '5':
        Acceptfile()
elif menu == '6':
        print("-----------------")
        print("โหมดลบข้อมูล")
        name = input("ชื่อไฟล์: ")
        DeleteFile(name)
        main()
elif menu == '7':
        print("-----------------")
        print("ปิดการใช้งาน")
        print("-----------------\n")
else:
        print("-----------------")
        print("ไม่มีโหมดที่เลือก")
        print("-----------------\n")

