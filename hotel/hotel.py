import os
import platform
import mysql.connector


mydb  =  mysql.connector.connect(
                            user = 'gangadhar',
                            password = 'N6bXcH8lZeJ9mWf?',
                            host = 'localhost',
                            database = 'hotel'
                            )
mycursor = mydb.cursor()


def registercustomer():
    name = input("Enter name: ")
    addr = input("Enter address: ")
    indate = input("Enter check in date: ")
    outdate = input("Enter check out date: ")

    L = [name,addr,indate,outdate]
    customer_data = (L)

    query = "insert into customer_data(customer_name,address,in_date,out_date) values(%s,%s,%s,%s)"
    mycursor.execute(query, customer_data)
    mydb.commit()


def roomtypeview():
    query = "select * from roomtype"
    mycursor.execute(query)
    rows = mycursor.fetchall()

    for i in rows:
        print(i)


def roomrent():
    print("We have the following rooms for you:-")
    print("1. type A---->rs 1000 PN\-")
    print("2. type B---->rs 2000 PN\-")
    print("3. type C---->rs 3000 PN\-")
    print("4. type D---->rs 4000 PN\-")

    choice = int(input("Enter Your Choice Please-> "))
    nights = int(input("For How Many Nights Did You Stay: "))

    if choice == 1:
        print("You have opted room type A")
        amount = 1000*nights

    elif choice == 2:
        print("You have opted room type B")
        amount = 2000*nights

    elif choice == 3:
        print("You have opted room type C")
        amount = 3000*nights

    elif choice == 4:
        print("You have opted room type D")
        amount = 4000*nights

    else:
        print("Please choose a room")

    print("Your room rent is  = ",s,"\n")


def restaurentmenuview():
    query  = "select * from restaurant"
    mycursor.execute(query)
    rows = mycursor.fetchall()

    for x in rows:
        print(x)


def orderitem():
    query  = "select * from restaurent"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    
    for x in rows:
        print(x)
    
    print("Do you want to purchase from above list?")
    
    d = int(input("Enter your choice: "))

    if d == 1:
        print("You have ordered tea")
        a = int(input("Enter quantity "))
        amount = 10*a
        print("Your amount for tea is :",s,"\n")

    elif d == 2:
        print("You have ordered coffee")
        a = int(input("Enter quantity "))
        amount = 10*a
        print("Your amount for coffee is :",s,"\n")

    elif d == 3:
        print("You have ordered colddrink")
        a = int(input("Enter quantity "))
        amount = 20*a
        print("Your amount for colddrink is :",s,"\n")

    elif d == 4:
        print("You have ordered samosa")
        a = int(input("Enter quantity "))
        amount = 10*a
        print("Your amount fopr samosa is :",s,"\n")

    elif d == 5:
        print("You have ordered sandwich")
        a = int(input("Enter quantity "))
        amount = 50*a
        print("Your amount fopr sandwich is :",s,"\n")

    elif d == 6:
        print("You have ordered dhokla")
        a = int(input("Enter quantity "))
        amount = 30*a
        print("Your amount for dhokla is :",s,"\n")

    elif d == 7:
        print("You have ordered kachori")
        a = int(input("Enter quantity "))
        amount = 10*a
        print("Your amount for kachori is :",s,"\n")

    elif d == 8:
        print("You have ordered milk")
        a = int(input("Enter quantity "))
        amount = 20*a
        print("Your amount for kachori is :",s,"\n")

    elif d == 9:
        print("You have ordered noodles")
        a = int(input("Enter quantity "))
        amount = 50*a
        print("Your amount for noodles is :",s,"\n")

    elif d == 10:
        print("You have ordered pasta")
        a = int(input("Enter quantity "))
        amount = 50*a
        print("Your amount for pasta is :",s,"\n")

    else:
        print("Please enter your choice from the menu")


def laundarybill():
    query  = "select * from laundary"
    mycursor.execute(query)
    rows = mycursor.fetchall()

    for x in rows:
        print(x)
        number_of_clothes = int(input("Enter Your number of clothes-> "))
        bill = number_of_clothes*10
        print("Your laundary bill:", bill, "\n")


def viewbill():
    customer_name = input("Enter customer name: ")
    print("Customer name :", customer_name, "\n")
    print("Laundary bill:")
    print("Restaurant bill:")


def Menuset():
    print("Enter 1: To enter customer data")
    print("Enter 2 : To view roomtype")
    print("Enter 3 : For calculating room bill")
    print("Enter 4 : For viewing restaurent menu")
    print("Enter 5 : For restaurent bill")
    print("Enter 6 : For laundary bill")
    print("Enter 7 : For complete bill")
    print("Enter 8 : For exit:")
    
    try:
        userinput = int(input("Please select an above option: "))
    except ValueError:
        exit("\n hi thats not a number")
    
    if userinput == 1:
        registercustomer()

    elif userinput == 2:
        type_of_room  =  roomtypeview()

    elif userinput == 3:
        room_rent_cost  =  roomrent()

    elif userinput == 4:
        restaurent_menu  =  restaurentmenuview()

    elif userinput == 5:
        items_ordered  =  orderitem()

    elif userinput == 6:
        laundary_bill  =  laundarybill()

    elif userinput == 7:
        view_bill  =  viewbill()

    elif userinput == 8:
        quit()

    else:
        print("Enter correct choice")
    
    runagain()
    

def runagain():
    runagn = input("\nDo want to run again y/n: ")
    
    while runagn.lower() == 'y':
        if platform.system() == "Windows":
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn = input("\n want to run again y/n: ")

Menuset()