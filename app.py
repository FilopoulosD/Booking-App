import mysql.connector
import datetime
from datetime import date
from dbconnect import mydb
from createcsv import create_csv
from tkinterShow import showcsv
from DeleteFileCSV import delete


mydb




class CustomError (Exception) :
    pass
class AllPositionsBooked(CustomError):
    pass
class ArrivalAfterDeparture(CustomError):
    pass
class PositionsNotCorrect(CustomError):
    pass
class BookingNotCorrect(CustomError):
    pass
class CheckInAlreadyIn(CustomError):
    pass

today = date.today()

while True:


    cursor = mydb.cursor()
    print("Select Action:\n1)Add a new Customer\n2)Add a new Position\n3)Add a new Booking\n4)Check In\n"
          "5)Show Current Customers On Camping\n6)Show Future Arrivals\n7)Show All Customers\n8)Show All Bookings Between two Dates\n"
          "9)Show  Available Positions\n10)Delete a Booking\n11)Search A Customer By Name\n12)Check Out\n"
          "13)Find the Total Cost of a Customer\n14)Change the arrival o date of a booking\n15)Chande the departure\n16)Exit")

    a = input()

    ##Exit
    if(a=='16'):
        delete("file.csv")
        cursor.close()
        mydb.close()
        break
    ## Add a new Customer
    elif (a == '1'):
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
            while month1>13 or month1<=0 or day1>=31 or day1<=0:
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
            if ((today.year - year1 > 18) or (today.year - year1 ==18 and today.month - month1 > 0) or(today.year - year1 ==18 and today.month - month1==0 and today.day >= day1)):
                cpd1 = 5
            else:
                cpd1 = 3
            tc1=0
            val1=(id1,name1,resId1,phone1,formatted_date1,adt1,cpd1,tc1)
            print("Are you sure you want to add to customer's the following:\nCustomer's Id: "
                  , id1, "\nCustomer's Name: ", name1, "\nResponsible customer's Id: ", resId1, "\nPhone Number: "
                  , phone1, "\nDate of Birth: ", formatted_date1, "\nADT: "
                  , adt1, "\nCost Per Day: ", cpd1,"\nTotal Cost: ",tc1,"\nIf so enter yes")
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
            maxnum2 = int(input("Give position's max number\n"))
            val2 = (id2, type2, usagecost2, electricity2, wifi2, maxnum2)
            print("Are you sure you want to add to positions the following:\nPosition's Id: "
                  ,id2, "\nPosition's Type:", type2, "\nUsage Cost: ", usagecost2,"\nElectricity: "
                  , electricity2,"\nWifi: ", wifi2, "\nMax number:", maxnum2,"\nIf so enter yes" )
            add2 = input()
            if add2 in ["YES", "Yes", "yes"]:
                query2 = "INSERT INTO Position (Id,Type,`Usage Cost`,Electricity,Wifi,`Max number`)" \
                         "VALUES (%s,%s,%s,%s,%s,%s);"
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
            query31 = "SELECT Id FROM Customers ORDER BY Id"
            cursor.execute(query31)
            result31 = cursor.fetchall()
            print("Choose a customers Id from the following\n")
            for x in result31:
                print("Customer's Id: {}\n".format(x[0]))
            custId3 = int(input("Give customers's Id:\n"))
            ### Check if arrival is before departure
            while True:
                try:
                    ### Arrival
                    year31 = int(input('Enter arranged year of arrival\n'))
                    month31 = int(input('Enter arranged month of arrival\n'))
                    day31 = int(input('Enter arranged day of arrival\n'))
                    while month31 > 13 or month31 < 1 or day31 > 31 or day31 < 1:
                        print("There is an error with the dates.Please type again.")
                        month31 = int(input('Enter month of arrival\n'))
                        day31 = int(input('Enter day of arrival\n'))
                    date31 = datetime.date(year31, month31, day31)
                    ### Departure
                    year32 = int(input('Enter arranged year of departure\n'))
                    month32 = int(input('Enter arranged month of departure\n'))
                    day32 = int(input('Enter arranged day of departure\n'))
                    while month32 > 13 or month32 < 1 or day32 > 31 or day32 < 1:
                        print("There is an error with the dates.Please type again.")
                        month32 = int(input('Enter month of departure\n'))
                        day32 = int(input('Enter day of departure\n'))
                    date32 = datetime.date(year32, month32, day32)

                    arrival3 = date31.strftime('%Y-%m-%d')
                    departure3 = date32.strftime('%Y-%m-%d')
                    if date31 > date32:
                        raise ArrivalAfterDeparture
                    else:
                        break
                except ArrivalAfterDeparture:
                    print("The Arrival date is after Departure. Please Give again the correct dates")
            ### Position's Id
            try:
                cursor.execute("SELECT DISTINCT p.id,p.Type,p.`Max number`  FROM Position p WHERE p.id   NOT IN "
                               "(SELECT Position.id FROM Position LEFT JOIN Booking  ON Position.id=Booking.`Position Id` "
                               "WHERE   (%s>=Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                               "or (%s>Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                               "or (%s<Booking.`Due date of arrival` and %s>=Booking.`Due date of departure`)) ",
                               (date31, date31, date32, date32, date31, date32,))

                result3a = cursor.fetchall()
                if len(result3a) == 0:
                    print("The are not empty positions for the selected dates")
                    raise AllPositionsBooked
                else:
                    print(result3a)
                    print("Choose a position's Id from the following\n")
                    for x1 in result3a:
                        print("Position's Id: {}".format(x1[0]))
                        print("Position's Type: {}".format(x1[1]))
                        print("Position's Max Number: {}\n".format(x1[2]))

                    posId3 = int(input("Give position's Id\n"))

                    var3 = 0
                    for x2 in result3a:
                        if (posId3 == x2[0]):
                            var3 = 1
                    if (var3 == 1):
                        ### Number of Adults
                        print("Please give the number of adults")
                        adults = int(input())
                        ### Number of Children
                        print("Please give the number of Children")
                        children = int(input())
                        ### Total Cost
                        cursor.execute("select `Usage Cost`,`Electricity`,`Wifi`, `Max Number` from Position where `id`=%s;",(posId3,))
                        result33 = cursor.fetchall()
                        totaldays = date32 - date31
                        if result33[0][1] in ["YES", "Yes", "yes"]:
                            electr = 2
                        else:
                            electr = 0

                        if result33[0][2] in ["YES", "Yes", "yes"]:
                            wifi = 3
                        else:
                            wifi = 0

                        totalcost3 = totaldays.days * result33[0][
                            0] + adults * totaldays.days * 5 + children * totaldays.days * 3 + totaldays.days * electr + totaldays.days * wifi

                        print("Total Cost is: ", totalcost3)
                        ### Advance
                        advance3 = float(input("Enter advance (if there is not please enter 0)\n"))
                        ### Booking Date
                        year33 = int(input('Enter year of booking\n'))
                        month33 = int(input('Enter month of booking\n'))
                        day33 = int(input('Enter day of booking\n'))
                        while month33 > 13 or month33 < 1 or day33 > 31 or day33 < 0:
                            print("There is an error with the dates.Please type again.")
                            month33 = int(input('Enter month of birt\n'))
                            day33 = int(input('Enter day of birth\n'))
                        date33 = datetime.date(year33, month33, day33)
                        BookingDate3 = date33.strftime('%Y-%m-%d')

                        val3 = (id3, custId3, posId3, date31, date32, advance3, totalcost3, today, adults, children)

                        print("Are you sure you want to add to positions the following:\nBooking's Id: "
                              , id3, "\nCustomer's Id:", custId3, "\nPosition's Id: ", posId3, "\nArrival: "
                              , arrival3, "\nDeparture: ", departure3, "\nAdvance: "
                              , advance3, "\nTotal Cost:", totalcost3, "\nBooking Date: ", BookingDate3,
                              "\nNumber of Adults: ",
                              adults, "\nNumber of Children: ", children, "\nIf so enter yes")
                        add3 = input()
                        if add3 in ["YES", "Yes", "yes"]:
                            query33 = "INSERT INTO  Booking(Id,`Customer Id`, `Position Id`,`Due date of arrival` ," \
                                      "`Due date of departure`,Advance,`Total Cost`,`Booking Date`,`Adult`,`Underage`)" \
                                      "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                            cursor.execute(query33, val3)
                            mydb.commit()
                            print("A new booking was added to the database")
                        else:
                            print("Operation Interupted ")
                    else:
                        raise PositionsNotCorrect
            except PositionsNotCorrect:
                print("The Position you gave is not correct")
        except mysql.connector.Error as error:
            print("Something went wrong: {} \n".format(error))
            if error.errno == 1452:
                if 'REFERENCES `Customers` (`Id`)' in error.msg:
                    print("There was a problem with the customer's id. Please choose an id that exists on the database\n")
                elif 'REFERENCES `Position` (`Id`)' in error.msg:
                    print("There was a problem with thw position's id. Please choose an id that exists on the database\n")
            elif error.errno == 1062:
                print("The Booking's id you choose is already in the system")
            elif ArrivalAfterDeparture:
                print("The Arrival date can't be after the departure date")
            else:
                print("There was an unexpected error")
    ## Check In
    elif (a == '4'):
        try:
            try:
                try:
                    query41 = "SELECT `Id` FROM Booking WHERE `Due date of arrival`<= CURDATE()"
                    cursor.execute(query41)
                    result41 = cursor.fetchall()
                    print("Choose a customers Id from the following\n")
                    for x in result41:
                        print("Booking's Id: {}\n".format(x[0]))
                    bookId4 = int(input("Give Booking's Id:\n"))
                    query42 = "SELECT `Booking Id` FROM `Checkin`"
                    cursor.execute(query42)
                    result42 = cursor.fetchall()
                    temp42 = 0
                    temp4 = 0
                    for y1 in result42:
                        if (bookId4 == y1[0]):
                            temp42 = 1
                    if (temp42 == 1):
                        raise CheckInAlreadyIn

                    for x2 in result41:
                        if (bookId4 == x2[0]):
                            temp4 = 1
                    if (temp4 != 1):
                        raise BookingNotCorrect
                except BookingNotCorrect:
                    print("The Booking you choose does not exist")

                arrival4 = today
                cursor.execute("SELECT `Due date of departure` FROM Booking WHERE `Id`=%s", (bookId4,))
                result42 = cursor.fetchall()
                print("Departure Date is: {}".format(result42[0][0]))
                cursor.execute("SELECT `Position Id` FROM Booking WHERE `Id`=%s", (bookId4,))
                result43 = cursor.fetchall()
                print("Position's Id is: {}".format(result43[0][0]))
                print("Are you sure you want to add to Check Ins the following:\nBooking's Id: "
                      , bookId4, "\nArrival: ", today, "\nDeparture Date: "
                      , result42[0][0],"\nPosition's Id: ",result43[0][0], "\nIf so enter yes")
                add4 = input()
                val4 = (bookId4, today, result42[0][0],result43[0][0])
                if add4 in ["YES", "Yes", "yes"]:
                    query43 = "INSERT INTO Checkin(`Booking Id`, `Arrival Date`,`Due date of departure`, `Position Id`) VALUES (%s,%s,%s,%s)"
                    cursor.execute(query43, val4)
                    mydb.commit()
                    print("A new check in was added to the database")
                else:
                    print("Operation Interupted ")
            except CheckInAlreadyIn:
                print("Booking already Checked in")
        except mysql.connector.Error as error:
            print("Something went wrong: {} \n".format(error))
    ## Show Current Customers On Camping
    elif (a == '5'):
        query5 = "select `Booking Id`,`Position Id`, `Customer Id`,`Arrival Date`, " \
                 "Booking.`Due date of departure`,`Total Cost`,`Underage`,`Adult` " \
                 "from Booking join Checkin where `Booking Id`= Booking.Id"

        cursor.execute(query5)
        result5 = cursor.fetchall()

        firstrow5 = [("Booking's Id", "Position's Id", "Customer's Id", "Arival Date", " Departure Date", " Total Cos",
                      "Underage",
                      "Adults")]
        create_csv(result5, firstrow5)
        showcsv("file.csv")
    ## Show Future Arrivals
    elif (a == '6'):
        query6="select  * from Booking " \
               "WHERE `Due date of arrival`>curdate();"
        cursor.execute(query6)
        result6 = cursor.fetchall()
        firstrow6 = [("Id", "Customer's Id", "Position's Id", " Date of Arranged Arrival", " Date of Departure", "Advance",
                      "Total Cost","Condition", "Type","Booking Date")]
        create_csv(result6, firstrow6)
        showcsv("file.csv")
    ## Show All Customers
    elif (a == '7'):
        query="SELECT * FROM Customers"
        cursor.execute(query)
        result = cursor.fetchall()

        firstrow = [('Id', 'Full Name', 'ResId', 'Phone Number', 'Birthdate', 'ADT', 'Cost per Day', 'Total Cost')]
        create_csv(result,firstrow)
        showcsv("file.csv")
    ## Show All Bookings Between 2 Dates
    elif (a == '8'):
        year81 = int(input('Enter arranged year of arrival\n'))
        month81 = int(input('Enter arranged month of arrival\n'))
        day81 = int(input('Enter arranged day of arrival\n'))
        while month81 > 13 or month81 < 1 or day81 > 31 or day81 < 1:
            print("There is an error with the dates.Please type again.")
            month81 = int(input('Enter month of arrival\n'))
            day81 = int(input('Enter day of arrival\n'))
        date81 = datetime.date(year81, month81, day81)

        year82 = int(input('Enter arranged year of departure\n'))
        month82 = int(input('Enter arranged month of departure\n'))
        day82 = int(input('Enter arranged day of departure\n'))
        while month82 > 13 or month82 < 1 or day82 > 31 or day82 < 1:
            print("There is an error with the dates.Please type again.")
            month82 = int(input('Enter month of departure\n'))
            day82 = int(input('Enter day of departure\n'))
        date82 = datetime.date(year82, month82, day82)

        cursor.execute("SELECT * FROM Booking WHERE %s<`Due date of departure` and %s>`Due date of arrival`",
                       (date81, date82))
        result = cursor.fetchall()
        firstrow = [('Id', 'Customer Id', 'Position Id', 'Due date of arrival', 'Due date of departure',
                     'Advance', 'Total Cost', 'Condition', 'Booking Date', 'Adults', 'Children')]
        create_csv(result, firstrow)
        showcsv("file.csv")
    ## Show All Available Positions
    elif (a == '9'):
        query = "select Id,Type FROM Position WHERE  Id NOT IN " \
                "(select `Position Id` from Checkin left join Booking on Booking.Id=Checkin.`Booking Id`)"
        cursor.execute(query)
        result = cursor.fetchall()
        firstrow = [('Position Id', 'Type')]
        create_csv(result, firstrow)
        showcsv("file.csv")
    ##Delete a Booking
    elif ( a== '10'):
        print("Please choose the book you want to delete:\n")
        query101 = "SELECT Id FROM Booking "
        cursor.execute(query101)
        result101 = cursor.fetchall()
        for x in result101:
            print("Booking's Id: {}\n".format(x[0]))
        canceledId = int(input("Please Choose:\n"))
        cursor.execute("DELETE FROM `Booking` where id=%s;", (canceledId,))
        mydb.commit()
        if canceledId in result101:
            print("Booking has been deleted")
        else:
            print("The Id you choose is not correct")
    ##Customer Search By Name
    elif(a == '11'):
        print("Please enter the full name of the customer you want\n")
        name11=input()
        cursor.execute("select * from Customers where `Full name`=%s;", (name11,))
        result112 = cursor.fetchall()
        firstrow = [('Id', 'Full Name', 'ResId', 'Phone Number', 'Birthdate', 'ADT', 'Cost per Day', 'Total Cost')]
        create_csv(result112, firstrow)
        showcsv("file.csv")
    ### Check Out
    elif(a == '12'):
        try:
            try:
                query121 = "SELECT `Booking Id` FROM Checkin"
                cursor.execute(query121)
                result121 = cursor.fetchall()
                print("Choose a booking's Id to check out\n")
                for x in result121:
                    print("Booking's Id: {}\n".format(x[0]))
                bookId12 = int(input("Give Booking's Id:\n"))
                temp4 = 0
                for x12 in result121:
                    if (bookId12 == x12[0]):
                        temp4 = 1
                if (temp4 != 1):
                    raise BookingNotCorrect
                cursor.execute("delete from Checkin where `Booking Id`=%s", (bookId12,))
                mydb.commit()
                print("Check Out Successful")
            except BookingNotCorrect:
                print("The Booking you choose does not exist")


        except mysql.connector.Error as error:
            print("Something went wrong: {} \n".format(error))
    ### Calculate the total cost of all the bookings of a specific customer
    elif(a == '13'):
        custId13=input("Please give the customer's Id: \n")
        cursor.execute("SELECT `Total Cost` FROM `Booking` WHERE `Customer Id`=%s",(custId13,))
        result13=cursor.fetchall()
        totalcost13=0
        for i in range(len(result13)):
            totalcost13=totalcost13 + result13[i][0]
        cursor.execute("UPDATE `Customers` SET `Total Cost`=%s WHERE Id=%s", (totalcost13, custId13,))
        print("The total cost is: ", totalcost13)
        mydb.commit()
    ### Change the arrival date of a booking
    elif(a=='14'):


        try:
            query = "SELECT DISTINCT `Customers`.id FROM `Customers` JOIN `Booking` ON `Customers`.id=Booking.`Customer Id` ORDER BY `Customers`.id"
            cursor.execute(query)
            result = cursor.fetchall()
            result_list=[]
            print("The customers ids are:\n")
            for x in range(len(result)):
                print(result[x][0])

                result_list.append(result[x][0])
            customer_id = int(input("Choose the id that wants to make the changes\n"))
            while customer_id not in result_list:
                print("Give a customer id from the above that exists:")
                customer_id = int(input("Choose the id that wants to make the changes\n"))


            cursor.execute("SELECT id,`Position Id`,`Due date of arrival`,`Due date of departure` "
                           "FROM Booking "
                           "WHERE `Customer Id`= %s ", (customer_id,))

            result = cursor.fetchall()

            result_list2 = []
            print("The id of the bookings of this customer are:")
            for x in range(len(result)):
                print(result[x][0])
                result_list2.append(result[x][0])
            flag = True
            book_id = int(input("Choose the booking id:\n"))
            while book_id not in result_list2:
                print("Please choose a booking id that exists from the above\n")
                book_id = int(input("Choose the booking id:\n"))

            for x in range(len(result)):
                if flag == False:
                    break
                for y in range(len(result[0])):
                    if result[x][y] == book_id:
                        flag = False
                        row = x

                    break

            print("Booking id:",result[row][0])

            print("Position id:",result[row][1])

            print("Arrival Date:",result[row][2])

            print("Departure Date:",result[row][3])

            print("\n")
            year11 = int(input('Enter  year of arrival\n'))
            month11 = int(input('Enter  month of arrival\n'))
            day11 = int(input('Enter  day of arrival\n'))
            while month11 > 13 or month11 < 1 or day11 > 31 or day11 < 1:  # day31<1 oxi day31<0
                print("There is an error with the dates.Please type again.")
                month11 = int(input('Enter month of arrival\n'))  # arrival oxi birth
                day11 = int(input('Enter day of arrival\n'))
            date11 = datetime.date(year11, month11, day11)
            ArrivalDate = date11.strftime('%Y-%m-%d')


            current_arrival_date = datetime.date(result[row][2].year, result[row][2].month, result[row][2].day)
            departure_date = datetime.date(result[row][3].year, result[row][3].month, result[row][3].day)

            cursor.execute("SELECT p.`Usage Cost`,p.`Electricity`,p.`Wifi`,b.`Adult`,b.`Underage` "
                          "FROM `Position` p "
                          "JOIN `Booking` b ON p.`Id`=b.`Position Id` "
                          "WHERE b.`id`= %s ",(result[row][0],))
            resultc=cursor.fetchall()

            if resultc[0][1] in ["YES", "Yes", "yes"]:
                electr = 2
            else:
                electr = 0

            if resultc[0][2] in ["YES", "Yes", "yes"]:
                wifi = 3
            else:
                wifi = 0
            while date11 >= departure_date:
                print("Please choose again the the new arrival date to be before departure\n  ")
                year11 = int(input('Enter the new year of arrival\n'))
                month11 = int(input('Enter the new month of arrival\n'))
                day11 = int(input('Enter the new day of arrival\n'))
                while month11 > 13 or month11 < 1 or day11 > 31 or day11 < 1:  # day31<1 oxi day31<0
                    print("There is an error with the dates.Please type again.")
                    month11 = int(input('Enter month of arrival\n'))  # arrival oxi birth
                    day11 = int(input('Enter day of arrival\n'))
                date11 = datetime.date(year11, month11, day11)

            total_days14=departure_date-date11
            totalcost14 = total_days14.days * resultc[0][0] + resultc[0][3] * total_days14.days * 5 + resultc[0][4] * total_days14.days * 3 + total_days14.days * electr + total_days14.days *wifi

            if date11 > current_arrival_date:
                cursor.execute("UPDATE `Booking` "
                               "SET `Due date of arrival`=%s, `Total Cost`= %s "
                               "WHERE id=%s ", (date11,totalcost14, book_id))

                result11 = mydb.commit()
                print("Change is made!\n")
            else:
                cursor.execute("SELECT p.id "
                               "FROM Position p "
                               "WHERE  p.id=%s and p.id NOT IN (SELECT Position.id "
                               "FROM Position "
                               "LEFT JOIN Booking  ON Position.`id`=Booking.`Position Id` "
                               "WHERE   (%s>=Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                               "  or (%s>Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                               "  or (%s<Booking.`Due date of arrival` and %s>=Booking.`Due date of departure`)) ", (
                                   result[row][1], date11, date11, current_arrival_date, current_arrival_date, date11,
                                   current_arrival_date,))

                result11_a = cursor.fetchall()

                if len(result11_a) == 1:
                    cursor.execute("UPDATE `Booking` "
                                   "SET `Due date of arrival`=%s ,`Total Cost`= %s "
                                   "WHERE id=%s ", (date11,totalcost14, book_id))
                    mydb.commit()
                    print("Change is made!\n")
                else:
                    cursor.execute("SELECT DISTINCT p.id,p.Type,p.`Max number` "
                                   "FROM Position p "
                                   "WHERE   p.id NOT IN (SELECT Position.id "
                                   "FROM Position "
                                   "LEFT JOIN Booking  ON Position.`id`=Booking.`Position Id` "
                                   "WHERE   (%s>=Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                                   "  or (%s>Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                                   "  or (%s<Booking.`Due date of arrival` and %s>=Booking.`Due date of departure`)) ",
                                   (date11, date11, departure_date, departure_date, date11, departure_date,))

                    result11_b = cursor.fetchall()

                    if len(result11_b) == 0:
                        print("No available positions to change the dates\n")
                    else:
                        print("\n")
                        print("You cannot book this position these dates,check for empty positions")
                        print("The id , the type and the max number of these positions are:")

                        for i in result11_b:
                            print(i)

                        print("Do you want to book in one of these positions?")
                        ans = input("If you want to do the booking type yes:\n")
                        if ans in ["YES", "yes", "Yes"]:
                            pos_id = int(input("Choose one of the above positions id:\n"))
                            cursor.execute("UPDATE `Booking` "
                                           "SET `Due date of arrival`=%s ,`Position Id`=%s ,`Total Cost`= %s WHERE id=%s ", (date11, pos_id, totalcost14,book_id))
                            mydb.commit()
                            print("Change is made!\n")
                        else:
                            print("Make no changes\n")
        except ValueError:
            print("Something went wrong! \n")

    elif (a == '15'):


        try:
            query = "SELECT DISTINCT `Customers`.id FROM `Customers` " \
                    "JOIN `Booking` ON `Customers`.id=Booking.`Customer Id` ORDER BY `Customers`.id"
            cursor.execute(query)
            result = cursor.fetchall()
            result_list15 = []
            print("The customers ids are:\n")
            for x in range(len(result)):
                print(result[x][0])
                result_list15.append(result[x][0])

            customer_id = int(input("Choose the Customer id that wants to make the changes\n"))
            while customer_id not in result_list15:
                print("Give a customer id from the above that exists:")
                customer_id = int(input("Choose the id that wants to make the changes\n"))



            cursor.execute("SELECT id,`Position Id`,`Due date of arrival`,`Due date of departure` "
                           "FROM Booking "
                           "WHERE `Customer Id`= %s ", (customer_id,))

            result = cursor.fetchall()

            result_list15b = []
            print("The id of the bookings of this customer are:")
            for x in range(len(result)):
                print(result[x][0])
                result_list15b.append(result[x][0])

            flag = True

            book_id = int(input("Choose the booking id:\n"))
            while book_id not in result_list15b:
                print("Please choose a booking id that exists from the above")
                book_id = int(input("Choose the booking id:\n"))

            for x in range(len(result)):
                if flag == False:
                    break
                for y in range(len(result[0])):
                    if result[x][y] == book_id:
                        flag = False
                        row = x

                    break

            print("Booking id:", result[row][0])

            print("Position id:", result[row][1])

            print("Arrival Date:", result[row][2])

            print("Departure Date:", result[row][3])
            print("\n")

            year12 = int(input('Enter the new year of departure\n'))
            month12 = int(input('Enter the new month of departure\n'))
            day12 = int(input('Enter the new day of departure\n'))
            while month12 > 13 or month12 < 1 or day12 > 31 or day12 < 1:  # day31<1 oxi day31<0
                print("There is an error with the dates.Please type again.")
                month12 = int(input('Enter month of departure\n'))  # arrival oxi birth
                day12 = int(input('Enter day of departure\n'))
            date12 = datetime.date(year12, month12, day12)
            DepartureDate = date12.strftime('%Y-%m-%d')

            cursor.execute("SELECT p.`Usage Cost`,p.`Electricity`,p.`Wifi`,b.`Adult`,b.`Underage` "
                           "FROM `Position` p "
                           "JOIN `Booking` b ON p.`Id`=b.`Position Id` "
                           "WHERE b.`id`= %s ", (result[row][0],))
            resultc = cursor.fetchall()

            if resultc[0][1] in ["YES", "Yes", "yes"]:
                electr = 2
            else:
                electr = 0

            if resultc[0][2] in ["YES", "Yes", "yes"]:
                wifi = 3
            else:
                wifi = 0

            arrival_date = datetime.date(result[row][2].year, result[row][2].month, result[row][2].day)
            current_departure_date = datetime.date(result[row][3].year, result[row][3].month, result[row][3].day)

            while date12 <= arrival_date:
                print("Please choose again the the new departure date to be after arrival ")
                year12 = int(input('Enter  year of departure\n'))
                month12 = int(input('Enter  month of departure\n'))
                day12 = int(input('Enter  day of departure\n'))
                while month12 > 13 or month12 < 1 or day12 > 31 or day12 < 1:  # day31<1 oxi day31<0
                    print("There is an error with the dates.Please type again.")
                    month12 = int(input('Enter month of departure\n'))  # arrival oxi birth
                    day12 = int(input('Enter day of departure\n'))
                date12 = datetime.date(year12, month12, day12)

            total_days15 =  date12 - arrival_date
            totalcost15 = total_days15.days * resultc[0][0] + resultc[0][3] * total_days15.days * 5 + resultc[0][4] * total_days15.days * 3 + total_days15.days * electr + total_days15.days * wifi


            if date12 < current_departure_date:
                cursor.execute("UPDATE `Booking` "
                               "SET `Due date of departure`=%s ,`Total Cost`= %s WHERE id=%s ", (date12, totalcost15 , book_id)
                               )
                mydb.commit()
                print("Change is made!\n")
            else:

                cursor.execute("SELECT DISTINCT p.id "
                               "FROM Position p "
                               "WHERE  p.id=%s and p.id NOT IN (SELECT Position.id "
                               "FROM Position "
                               "LEFT JOIN Booking  ON Position.`id`=Booking.`Position Id` "
                               "WHERE   (%s>=Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                               "  or (%s>Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                               "  or (%s<Booking.`Due date of arrival` and %s>=Booking.`Due date of departure`)) ",
                               (result[row][1], current_departure_date, current_departure_date, date12, date12,
                                current_departure_date, date12,))

                result12_a = cursor.fetchall()

                if len(result12_a) == 1:
                    cursor.execute("UPDATE `Booking` "
                                   "SET `Due date of departure`=%s,`Total Cost`= %s "
                                   "WHERE id=%s ", (date12,totalcost15,book_id))
                    mydb.commit()
                    print("Change is made!\n")
                else:
                    cursor.execute("SELECT DISTINCT p.id,p.Type,p.`Max number` "
                                   "FROM Position p "
                                   "WHERE   p.id NOT IN (SELECT Position.id "
                                   "FROM Position "
                                   "LEFT JOIN Booking  ON Position.`id`=Booking.`Position Id` "
                                   "WHERE   (%s>=Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                                   "  or (%s>Booking.`Due date of arrival` and %s<Booking.`Due date of departure`) "
                                   "  or (%s<Booking.`Due date of arrival` and %s>=Booking.`Due date of departure`)) ",
                                   (arrival_date, arrival_date, date12, date12, arrival_date, date12,))

                    result12_b = cursor.fetchall()

                    if len(result12_b) == 0:
                        print("No positions available to change the date")
                    else:
                        print("\n")
                        print("You cannot book this position these dates,check for empty positions")
                        print("The id , the type and the max number of these positions are:")
                        for i in result12_b:
                            print(i)

                        print("Do you want to book in one of these positions?")
                        ans = input("If you want to do the booking type yes:\n")
                        if ans in ["YES", "yes", "Yes"]:
                            pos_id = int(input("Choose one of the above positions id:\n"))
                            cursor.execute("UPDATE `Booking` "
                                           "SET `Due date of departure`=%s ,`Position Id`=%s,`Total Cost`= %s "
                                           "WHERE id=%s ", (date12, pos_id,totalcost15 ,book_id))
                            mydb.commit()
                            print("Change is made!\n")
                        else:
                            print("Make no changes")
        except ValueError:
            print("Something went wrong \n")


    else:
        print("Please choose again\n")
