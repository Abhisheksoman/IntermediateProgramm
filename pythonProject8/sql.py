import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="asd"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), password VARCHAR(255) ,balance integer(233))")
c = input("enter your choice (a) create  account (b) view account (c) deposit balance (d) withdraw amount")

if c=="a":
  sql = "INSERT INTO customers (name, password , balance) VALUES (%s, %s ,%s)"
  user_name = input("enter the user name")
  password = input("enter the password")
  balance = int(input("enter the balance"))
  val = (f"{user_name}",f"{password}",f"{str(balance)}")
  mycursor.execute(sql, val)
  mydb.commit()


else:
  user_name= input("enter the user name")
  password= input("enter the password")

  if c=="b":
    sql = f"SELECT * FROM  customers where name='{user_name}' and password='{password}'"
    mycursor.execute(sql)
    x =mycursor.fetchone()
    print(x)

  elif c=="c":
    dep= int(input("enter balance to deposit"))
    sql = f"UPDATE customers set balance = balance+'{dep}' where name='{user_name}' and password='{password}'"
    mydb.commit()

  elif c=="d":
    min_balance=530
    wid=int(input("enter balance to withdraw"))
    sql=f"UPDATE customers set balance= balance-'{wid}' where name='{user_name}' and password='{password}' and balance>='{min_balance}'"
    mycursor.execute(sql)
    mydb.commit()