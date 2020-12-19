import mysql.connector
import datetime
from datetime import date
from dbconnect import mydb
from createcsv import create_csv
from tkinterShow import showcsv

mydb

class CustomError (Exception) :
  pass


class ArrivalAfterDeparture(CustomError):
    """Raised when the arrival is after the departure"""
    pass



today = date.today()

while True:
  cursor = mydb.cursor()
  print("Select Action:\n1)Add a new Customer\n2)Add a new Position\n3)Add a new Booking\n4)Check In\n"
        "5)Show Current Customers On Camping\n6)Show Future Arrivals\n7)Show All Customers\n8)Show All Bookings\n"
        "9)Show  Available Positions\n10)Exit")

  a = input()

  ##Exit
  if(a=='10'):
    break
  ## Add a new Customer
  elif(a=='1'):
    try:

      id1=int(input("Give customer's Id\n"))
      name1=input("Give customer's full name\n")
      print("Does the customer has another customers who is responsible?If so please type Yes!")
      ans=input()
      if ans in ["YES","Yes","yes"]:
        print("Please choose the main customer from below:\n")
        query11 = "SELECT Id, `Full name` FROM Customers"
        cursor.execute(query11)
        result11 = cursor.fetchall()
        print("Choose a customers Id from the following\n")
        for x in result11:
          print("Customer's Id: {}, Customer's Full Name: {}\n".format(x[0], x[1]))
        resId1 = int(input("Please Choose:\n"))
      else:
        resId1=None

      phone1 =(input("Give customer's phone\n"))
      year1 = int(input('Enter year of birth\n'))
      month1 = int(input('Enter month of birt\n'))
      day1 = int(input('Enter day of birth\n'))
      while month1>13 or month1<1 or day1>31 or day1<0:
        print("There is an error with the dates.Please type again.")
        month1 = int(input('Enter month of birt\n'))
        day1 = int(input('Enter day of birth\n'))

      date1 = datetime.date(year1, month1, day1)
      formatted_date1 = date1.strftime('%Y-%m-%d')

      while date1>today:
        print("The date of birth must be before current date. Please give again the customer's day of birth")
        year1 = int(input('Enter year of birth\n'))
        month1 = int(input('Enter month of birt\n'))
        day1 = int(input('Enter day of birth\n'))
        date1 = datetime.date(year1, month1, day1)
        formatted_date1 = date1.strftime('%Y-%m-%d')

      adt1=input("Give ADT\n")
      cpd1=float(input("Give cost per day\n"))
      tc1=0
      val1=(id1,name1,resId1,phone1,formatted_date1,adt1,cpd1,tc1)
      print("Are you sure you want to add to customers the following:\n",val1, "\nIf so type yes.")
      add1=input()
      if add1 in ["YES","Yes","yes"]:


        query1 = "INSERT INTO  Customers(Id,`Full name`,ResId,`Phone number`,Birthdate,ADT,`Cost per day`,`Total cost`)" \
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query1, val1)
        mydb.commit()
        print("A new customer was added to the database")
      else:
        print("Operation Interupted ")
    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))
      if error.errno == 1062:
        if 'Customers.SSN' in error.msg:
          print("The customer's SSN is already in the database")
        else:
          print("The Customer's id is already in the system")
      elif error.errno == 1452:
        print("The Id for main customer is not in the database. Please select an id that's correct")
      else:
        print("There was an unexpected error")

  ## Add a new Position
  elif (a == '2'):
    try:
      id2 = int(input("Give position's Id\n"))
      type2 = input("Give position's type\n")
      usagecost2 = (input("Give position's usage cost\n"))
      electricity2 = input("Give position's status for electricity\n")
      wifi2 = input("Give position's status for wifi\n")
      annual2 = input("Give position's status for annual rent\n")
      maxnum2 = int(input("Give position's max number\n"))
      val2 = (id2, type2, usagecost2, electricity2, wifi2, annual2, maxnum2)
      print("Are you sure you want to add to positions the following:\n",val2, "\nif so type yes.")
      add2 = input()
      if add2 in ["YES", "Yes", "yes"]:
        query2 = "INSERT INTO Position (Id,Type,`Usage Cost`,Electricity,Wifi,`Available for annual book`,`Max number`)" \
                 "VALUES (%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(query2, val2)
        mydb.commit()
        print("A new position was added to the database")

      else:
        print("Operation Interupted ")


    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))
      if error.errno == 1062:
        print("The Position's id you choose is already in the system")
      else:
        print("There was an unexpected error")

  ## Add a new Booking
  elif (a == '3'):
    try:
      id3 = int(input("Give Booking's Id:\n"))

### Customer's Id
      query31 = "SELECT Id FROM Customers"
      cursor.execute(query31)
      result31 = cursor.fetchall()
      print("Choose a customers Id from the following\n")
      for x in result31:
        print("Customer's Id: {}\n".format(x[0]))
      custId3 = int(input("Give customers's Id:\n"))

### Positions Id
      query32 = "SELECT Id FROM Position"
      cursor.execute(query32)
      result32 = cursor.fetchall()
      print("Choose a position's Id from the following\n")
      for x in result32:
        print("Position's Id: {}\n".format(x[0]))
      posId3 = int(input("Give position's Id:\n"))
### Check if arrival is before departure
      while True:
        try:
          ### Arrival
          year31 = int(input('Enter arranged year of arrival\n'))
          month31 = int(input('Enter arranged month of arrival\n'))
          day31 = int(input('Enter arranged day of arrival\n'))
          while month31 > 13 or month31 < 1 or day31 > 31 or day31 < 0:
            print("There is an error with the dates.Please type again.")
            month31 = int(input('Enter month of birt\n'))
            day31 = int(input('Enter day of birth\n'))
          date31 = datetime.date(year31, month31, day31)
          ### Departure
          year32 = int(input('Enter arranged year of departure\n'))
          month32 = int(input('Enter arranged month of departure\n'))
          day32 = int(input('Enter arranged day of departure\n'))
          while month32 > 13 or month32 < 1 or day32 > 31 or day32 < 0:
            print("There is an error with the dates.Please type again.")
            month32 = int(input('Enter month of birt\n'))
            day32 = int(input('Enter day of birth\n'))
          date32 = datetime.date(year32, month32, day32)

          arrival3 = date31.strftime('%Y-%m-%d')
          departure3 = date32.strftime('%Y-%m-%d')
          if date31 > date32:
            raise ArrivalAfterDeparture
          else:
            break
        except ArrivalAfterDeparture:
          print("The Arrival date is after Departure. Please Give again the correct dates")

      advance3 = float(input("Enter advance (if there is not please enter 0)\n"))
      totalcost3 = float(input("Enter total cost of Booking\n"))
### Condition
      condition3 = 'Active'


      Type3 = "Annual"

      year33 = int(input('Enter year of booking\n'))
      month33 = int(input('Enter month of booking\n'))
      day33 = int(input('Enter day of booking\n'))
      while month33 > 13 or month33 < 1 or day33 > 31 or day33 < 0:
        print("There is an error with the dates.Please type again.")
        month33 = int(input('Enter month of birt\n'))
        day33= int(input('Enter day of birth\n'))
      date33 = datetime.date(year33, month33, day33)
      BookingDate3 =date33.strftime('%Y-%m-%d')

      val3 = (id3, custId3, posId3, arrival3, departure3, advance3, totalcost3, condition3, Type3, BookingDate3)
      print("Are you sure you want to add to bookings the following:\n", val3, "if so type yes.")
      add3 = input()
      if add3 in ["YES", "Yes", "yes"]:
        query33 = "INSERT INTO  Booking(Id,`Customer Id`, `Position Id`,`Due date of arrival` ," \
                  "`Due date of departure`,Advance,`Total Cost`, `Condition`,`Type`,`Booking Date`)" \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(query33, val3)
        mydb.commit()
        print("A new booking was added to the database")
      else:
        print("Operation Interupted ")


### Handle errors
    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))

      if error.errno == 1452 :

        if 'REFERENCES `Customers` (`Id`)' in error.msg:
          print("There was a problem with the customer's id. Please choose an id that exists on the database\n")
        elif 'REFERENCES `Position` (`Id`)' in error.msg:
          print("There was a problem with thw position's id. Please choose an id that exists on the database\n")
      elif error.errno == 1062:
        print("The Booking's id you choose is already in the system")
      elif ArrivalAfterDeparture:
        print("The Arrival date can't be after the departure date")
    except ArrivalAfterDeparture:
      print("The Arrival date can't be after the departure date")

  ## Check In
  elif (a == '4'):
    try:
      query41 = "SELECT Id FROM Customers"
      cursor.execute(query41)
      result41 = cursor.fetchall()
      print("Choose a customers Id from the following\n")
      for x in result41:
        print("Customer's Id: {}\n".format(x[0]))
      custId4 = int(input("Give customers's Id:\n"))

      query42= "SELECT Id FROM Position"
      cursor.execute(query42)
      result42=cursor.fetchall()
      print("Choose a position's Id from the following\n")
      for i in result42:
        print("Position's Id: {}\n".format(i[0]))
      posId4= int(input("Give Position's Id: \n"))

      arrival4=today

      year4 = int(input('Enter year of arranged departure\n'))
      month4 = int(input('Enter month of arranged departure\n'))
      day4 = int(input('Enter day of arranged departure\n'))
      while month4 > 13 or month4 < 1 or day4 > 31 or day4 < 0:
        print("There is an error with the dates.Please type again.")
        month4 = int(input('Enter month of birt\n'))
        day4 = int(input('Enter day of birth\n'))
      date4 = datetime.date(year4, month4, day4)
      BookingDate4 = date4.strftime('%Y-%m-%d')

      val4=(posId4,custId4,arrival4,BookingDate4)
      print("Are you sure you want to add to check ins the following:\n", val4, "if so type yes.")
      add4 = input()
      if add4 in ["YES", "Yes", "yes"]:
        query43 = "INSERT INTO CheckIn(`Position Id`,`Customers Id`,`Arrival Date`,`Due date of departure`) VALUES (%s,%s,%s,%s)"
        cursor.execute(query43, val4)
        mydb.commit()
        print("A new check in was added to the database")
      else:
        print("Operation Interupted ")
    except mysql.connector.Error as error:
      print("Something went wrong: {} \n".format(error))

  ## Show Current Customers On Camping
  elif (a == '5'):
    query5="select `Position Id`, `Customers Id`,`Arrival Date`, `Due date of departure`, `Full name`,`Phone number`,`ADT` " \
           "from CheckIn join Customers " \
           "where `Due date of departure`>curdate() " \
           "and `Position Id` = Id"

    cursor.execute(query5)
    result5= cursor.fetchall()
    print(result5)
    firstrow5=[("Position's Id", "Customer's Id", "Arrival Date"," Departure Date"," Full Name","Phone Number","Social Security Number")]
    create_csv(result5,firstrow5)
    showcsv("file.csv")
  ## Show Future Arrivals
  elif (a == '6'):
    query6="select  * from Booking " \
           "WHERE `Due date of arrival`>curdate();"
    cursor.execute(query6)
    result6 = cursor.fetchall()
    print(result6)
    firstrow6 = [("Id", "Customer's Id", "Position's Id", " Date of Arranged Arrival", " Date of Departure", "Advance",
                  "Total Cost","Condition", "Type","Booking Date")]
    create_csv(result6, firstrow6)
    showcsv("file.csv")
  ## Show All Customers
  elif (a == '7'):
    query="SELECT * FROM Customers"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    firstrow = [('Id', 'Full Name', 'ResId', 'Phone Number', 'Birthdate', 'ADT', 'Cost per Day', 'Total Cost')]
    create_csv(result,firstrow)
    showcsv("file.csv")
  ## Show All Bookings
  elif (a == '8'):
    query = "SELECT * FROM Booking"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    firstrow = [('Id', "Customer's Id", "Position's Id", 'Due Date of Arrival', 'Due Date of Departure', 'Advance', 'Total Cost', 'Condition','Type','Booking Date')]
    create_csv(result, firstrow)
    showcsv("file.csv")
  ## Show All Available Positions
  elif (a == '9'):
    print(a)

  else:
    print("Please choose again\n")


cursor.close()
mydb.close()

