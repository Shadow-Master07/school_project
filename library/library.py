import mysql.connector as mysql_connector 

connector = mysql_connector.connect(
                host="localhost",
                user="shaktiman",
                passwd="12345",
                database="library"
)

def addbook():
    book_name = input("Enter BOOK Name: ")
    book_code = input("Enter BOOK Code: ")
    total_books = input("Total Books: ")
    subject = input("Enter Subject: ")

    data = (
        book_name,
        book_code,
        total_books,
        subject
        )
    
    sql = 'insert into books values(%s,%s,%s,%s)'
    
    cursor = connector.cursor()
    cursor.execute(sql, data)
    connector.commit()
    
    print(">------------------------------------------------------<")
    print("Data Entered Successfully")
    

def issueb():
    customer_name = input("Enter Your Name: ")
    customer_registration_number = input("Enter Your Reg No: ")
    book_code = input("Enter Book Code: ")
    issue_date = input("Enter Date Of Issuing : ")
    query = "insert into issue values(%s,%s,%s,%s)"
    
    data = (
        customer_name,
        customer_registration_number,
        book_code,
        issue_date
        )
    
    cursor = connector.cursor()
    cursor.execute(query, data)
    connector.commit()

    print(">----------------------------------------------<")
    print(f"Book issued to : {customer_name}")
    bookup(book_code,-1)

def submitb():
    customer_name = input("Enter Name: ")
    customer_registration_number = input("Enter Reg No: ")
    book_code = input("Enter Book Code: ")
    issue_date = input("Enter Date: ")
    query = "insert into submit values(%s,%s,%s,%s)"

    data = (
        customer_name,
        customer_registration_number,
        book_code,
        issue_date
        )

    cursor = connector.cursor()
    cursor.execute(query, data)
    connector.commit()

    print(">-----------------------------------------------------<")
    print("Book Submitted from: {customer_name}")
    bookup(book_code, 1)

def bookup(book_code,u):
    query = "select TOTAL from books where BCODE=%s"

    data = (book_code,)
    cursor = connector.cursor()
    cursor.execute(query, data)

    myresult = cursor.fetchone()
    total_books = myresult[0] + u

    sql = "update books set TOTAL = %s where BCODE = %s"
    data = (total_books, book_code)
    cursor.execute(sql, data)

    connector.commit()
    

def dbook():
    book_code = input("Enter Book Code: ")
    query = "delete from books where BCODE = %s"
    
    data = (book_code,)
    cursor = connector.cursor()
    cursor.execute(query, data) 

    connector.commit()


def dispbook():
    query = "select * from books"

    cursor = connector.cursor()
    cursor.execute(query)
    myresult = cursor.fetchall()
    
    for i in myresult:
        print("Book Name : ",i[0])
        print("Book Code: ",i[1])
        print("Total : ",i[2])
        print(">------------------------------------------<")



def main(): 
    print("""
                            LIBRARY MANAGER
    1. ADD BOOK
    2. ISSUE BOOK
    3. SUBMIT BOOK
    4. DELETE BOOK
    5. DISPLAY BOOKS
    q. QUIT
    """)
    choice = input("Enter Task No: ")
    print(">-----------------------------------------------------<")
    if choice == '1':
        addbook()
    elif choice=='2':
        issueb()
    elif choice=='3':
        submitb()
    elif choice=='4':
        dbook()
    elif choice=='5':
        dispbook()
    elif choice.lower() == "q":
        exit("Bye...")
    else :
        print(" Wrong choice..........")


def Password():
    passcode = input("Enter Password: ")
    if passcode == "py143":
        while True:
            main()

Password()