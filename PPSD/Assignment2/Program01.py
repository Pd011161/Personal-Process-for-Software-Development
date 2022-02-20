print("โหมดของโปรแกรมนี้")
print("สร้างไฟล์ พิม1")
print("เขียนและแก้ไขไฟล์ พิม2")
print("อ่่านไฟล์ พิม3")
print("ออกจากโปรแกรม พิมExit")
print("ออกจากโหมด พิมOut")
menu = input("พิมExitเพื่อปิดโปรแกรม หรือ พิมStartเพื่อเริ่มโปรแกรม: ")
while menu != 'Exit':
    menu = input("กรุณาเลือกโหมดที่ต้องการใช้งาน: ")
    if menu == '1' :
        print("สร้างไฟล์")
        name = input("ชื่อไฟล์: ")
        f = open(name,"w+")
        f.close()
    elif menu == '2' :
        print("เขียนและแก้ไขไฟล์: ")
        name = input("ชื่อไฟล์: ")
        run = True
        f= open(name,"a+")
        num = []
        while run:
          print("กรุณาใส่ตัวเลข หรือ Out: ")
          nub = input("ใส่ตัวเลข: ")
          if nub.isnumeric() :
              f.write(nub)
              f.write("\n")
          elif nub == 'Out' :
              run = False
          else :
              print("เกิดข้อผิดพลาด")
        f.close()
    elif menu == '3' :
        print("อ่านไฟล์")
        name = input("ชื่อไฟล์: ")
        f= open(name, "r")
        for i in f:
            print(i)
    elif menu == "Exit" :
        print("สิ้นสุดโปรแกรม")
    else :
        print("เกิดข้อผิดพลาด")

