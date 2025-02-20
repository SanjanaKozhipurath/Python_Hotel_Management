import MySQLdb
from tabulate import tabulate
db=MySQLdb.connect("localhost","root","vminkook9597",'trial')
a=db.cursor()

sql1="CREATE TABLE if not exists orders(Item VARCHAR(35), Quantity INT,Cost INT, Total_Price INT)"
a.execute(sql1)

def orders_food(m,ch):
    a.execute("select * from "+m)
    y=a.fetchall()
    print()
    for i in y:
        if i[0]==ch:
            qty=int(input("Enter quantity for the chosen dish:"))
            q="INSERT INTO orders values('{}',{},{},{})".format(i[1],qty,i[2],qty*i[2])
            a.execute(q)
            db.commit()

def services(m,ch):
    a.execute("select * from "+m)
    y=a.fetchall()
    print()
    for i in y:
        if i[0]==ch:
            qty=int(input("Enter quantity of specified cloth:"))
            q="INSERT INTO orders values('{}',{},{},{})".format(i[1],qty,i[2],qty*i[2])
            a.execute(q)
            db.commit()
            
def orders_room(ch):
    global b
    a.execute("Select * from roombooking")
    y=a.fetchall()
    print()
    for i in y:
        if i[0]==ch:
            qty=int(input("Enter number of rooms:"))
            no_days=int(input("Enter number of days to book the room:"))
            q="INSERT ignore INTO orders values('{}',{},{},{})".format(i[1],qty,i[3],qty*no_days*i[3])
            a.execute(q)
            db.commit()
            if i[0]==1:
                for j in range (qty):
                    sql2="update roombooking set Availability=Availability-1 where Room='Single'";
                    a.execute(sql2)
                    db.commit()
                
            elif i[0]==2:
                for j in range (qty):
                    sql2="update roombooking set Availability=Availability-1 where Room='Twin'";
                    a.execute(sql2)
                    db.commit()
                    
            elif i[0]==3:
                for j in range (qty):
                    sql2="update roombooking set Availability=Availability-1 where Room='Triple'";
                    a.execute(sql2)
                    db.commit()
                
            elif i[0]==4:
                for j in range (qty):
                    sql2="update roombooking set Availability=Availability-1 where Room='Quad'";
                    a.execute(sql2)
                    db.commit()
                
            elif i[0]==5:
                for j in range (qty):
                    sql2="update roombooking set Availability=Availability-1 where Room='Queen'";
                    a.execute(sql2)
                    db.commit()
            
            elif i[0]==6:
                for j in range (qty):
                    sql2="update roombooking set Availability=Availability-1 where Room='King'";
                    a.execute(sql2)
                    db.commit()
                
            elif i[0]==7:
                for j in range (qty):
                    sql2="update roombooking set Availability=Availability-1 where Room='Suite'";
                    a.execute(sql2)
                    db.commit()
                        
def billing():
        print()
        print(" --------------------------------")
        print("             PAYMENT")
        print(" --------------------------------")
        print("   MODE OF PAYMENT")
   
        print(" 1- Credit/Debit Card")
        print(" 2- Paytm/PhonePe")
        print(" 3- Using UPI")
        print(" 4- Cash")  
   
        print(" --------------------------------")
        print()
        x=int(input("Enter mode of payment: "))
        n={}
        name=input("Enter you full name: ")
        phone=input("Enter your phone number: ")
        n[name]=name
        n[phone]=phone
        sql="select sum(total_price) from orders"
        a.execute(sql)
        x=a.fetchall()
        y=x[0][0]
        
        amount=int(y)
        print("\nAmount: ",amount)
        print("Confirm bill for S&H Hotel ?")
        print("(y/n)")
        ch=str(input("->"))
        if ch=='y' or ch=='Y':
            print("\n\n---------------------------------------------------------------------------------------------------------")
            print("                                          S&H hotel ")
            print(" ---------------------------------------------------------------------------------------------------------")
            print("                                             Bill")
            print(" ----------------------------------------------------------------------------------------------------------")
            print(" Name: ",n[name],"\t\n Phone No.: ",n[phone],"\t")
            tax=10+(0.05*amount)
            print(" Hotel Charges plus tax:\t",tax)
            print(" --------------------------------------------------------------------------------------------------------")
            a.execute("select Item,Quantity,Total_Price from orders")
            data=a.fetchall()
            print(tabulate(data,headers=['Item','Quantity','Total Price'],tablefmt='grid'))
            print("\n Total Amount:Dhs.",amount+tax,"\t")
            print(" --------------------------------------------------------------------------------------------------------")
            print("                                           Thank You")
            print("                                         Visit Again :)")
            print(" -------------------------------------------------------------------------------------------------------\n")             
def cust_management():
    def room_booking():
        while True:
            print()
            sql="Select * from roombooking"
            a.execute(sql)
            print()
            print(tabulate(a, headers=["Sl No", "Room","Availability","Price Per Day"], tablefmt="psql", showindex=False))
            ch=int(input("Enter you choice of room:"))
            orders_room(ch)
            an=input("Do you wish to book more rooms?(y/n):")
            if an=='n':
                print()
                print()
                break
            else:
                print()
                continue

    def room_services():
        global b
        print()
        sql="Select * from roomservices"
        a.execute(sql)
        print(tabulate(a, headers=["Sl No", "Services"], tablefmt="psql", showindex=False))
        print()
        ch=int(input("Enter your choice(1/2):"))
        if ch==1:
            an='y'
            while an=='y':
                print()
                print("-------------------------------------------------------------------------")
                print("                                S&H HOTEL")
                print("-------------------------------------------------------------------------")
                print("                                Menu Card")
                print("-------------------------------------------------------------------------")
                print("\n BEVARAGES                              BIRIYANI")
                print("----------------------------------     ----------------------------------")
                print(" 1  Tea..................... 12.00      26 Mutton Dum biriyani..... 20.00")
                print(" 2  Coffee.................. 15.00      27 Chicken Biriyani........ 25.00")
                print(" 3  Water...................  5.00      28 Fish Biriyani........... 28.00")
                print(" 4  Cold Drink..............  7.00      29 Veg biriyani............ 22.00")
                print(" 5  Cocktails............... 10.00        ")
                print(" 6  Milkshakes.............. 25.00      ")
                print(" 7  Fresh Juices............ 16.00      ROTI")
                print("                                       ----------------------------------")
                print("                                        30 Chapatti................  2.00")
                print(" CHAATS                                 31 Paratha.................  3.00")
                print("----------------------------------      32 Butter Naan.............  4.00")
                print(" 8  Pav Bhaji............... 10.00       ")
                print(" 9  Bhel Puri............... 12.00       ")
                print(" 10 Sev Puri................  8.00      CURRY")
                print(" 11 Vada Pav................ 14.00     ----------------------------------")
                print(" 12 Dahi Papri Chaat........ 18.00      33 Butter Chicken..........  20.00")
                print("                                        34 Mutton Kurma............  25.00")
                print("                                        35 Veg Special.............  24.00")
                print(" SALADS                                 36 Beef Fry................  25.00")
                print("----------------------------------      ")
                print(" 13 Grilled Chicken Salad... 10.00      ")
                print(" 14 Club Salad.............. 10.00      DESSERTS")
                print(" 15 Italian Salad........... 14.00     ----------------------------------")
                print(" 16 Greek Salad............. 20.00      37 Gulab Jamun.............  7.00")
                print(" 17 MexicanStreetCornSalad.. 40.00      38 Rasmala.................  8.00")
                print("                                        39 Kunafa.................. 10.00")
                print("                                        40 Luqaimat................  4.00")
                print(" PASTA                                  41 Baqlava.................  8.00")
                print("----------------------------------      42 Ice Cream...............  6.00")
                print(" 18 ChickenScaloppiniPasta.. 20.00      43 Brownies................ 10.00")
                print(" 19 Creamy Shrimps Pasta.... 20.00      44 Cheesecake..............  6.00")
                print(" 20 Italian Spaghetti....... 24.00      45 Choco Molten Lava Cake.. 18.00")
                print("                                        46 Choco Molten Lava Cake.. 18.00")
                print("                                        ")
                print("                     QUESADILLA                             ")
                print("                    ----------------------------------      ")
                print("                     21 Grilled Shrimp.......... 20.00      ")
                print("                     22 Cheese Quesadilla....... 15.00      ")
                print("                     23 Chicken Fajita.......... 18.00      ")
                print("                     24 Steak Combo Meal........ 30.00      ")
                print()
                print("-------------------------------------------------------------------------")
                print()
                print("1.Beverages\n2.Chaats\n3.Salads\n4.Pasta\n5.Quesadilla\n6.Biriyani\n7.Roti\n8.Curry\n9.Desserts")
                print()
                cho=int(input("Enter your choice:"))
                if cho==1:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("**********")
                        print("BEVARAGES")
                        print("**********")
                        a.execute("Select * from beverages")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='beverages'
                        ch=int(input("Enter you choice of beverages:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more beverages? (y/n):")
                        print()
                                    
                elif cho==2:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("*******")
                        print("CHAATS")
                        print("*******")
                        a.execute("Select * from chaat")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='chaat'
                        ch=int(input("Enter you choice of chaats:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more chaats? (y/n):")
                        print()

                elif cho==3:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("*******")
                        print("SALADS")
                        print("*******")
                        a.execute("Select * from salads")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='salads'
                        ch=int(input("Enter you choice of salads:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more salads? (y/n):")
                        print()

                elif cho==4:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("*******")
                        print("PASTA")
                        print("*******")
                        a.execute("Select * from pasta")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='pasta'
                        ch=int(input("Enter you choice of pasta:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more pasta? (y/n):")
                        print()

                elif cho==5:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("***********")
                        print("QUESADILLA")
                        print("***********")
                        a.execute("Select * from quesadillas")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='quesadillas'
                        ch=int(input("Enter you choice of quesadilla:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more quesadilla? (y/n):")
                        print()

                elif cho==6:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("*********")
                        print("BIRIYANI")
                        print("*********")
                        a.execute("Select * from biriyani")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='biriyani'
                        ch=int(input("Enter you choice of biriyani:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more biriyani? (y/n):")
                        print()

                elif cho==7:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("*****")
                        print("ROTI")
                        print("*****")
                        a.execute("Select * from roti")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='roti'
                        ch=int(input("Enter you choice of roti:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more roti? (y/n):")
                        print()

                elif cho==8:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("******")
                        print("CURRY")
                        print("******")
                        a.execute("Select * from curry")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='curry'
                        ch=int(input("Enter you choice of curry:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more curry? (y/n):")
                        print()

                elif cho==9:
                    ans='y'
                    while ans=='y':
                        print()
                        print()
                        print("*********")
                        print("DESSERTS")
                        print("*********")
                        a.execute("Select * from desserts")
                        print(tabulate(a,headers=['Sl_No','Item','Price'],tablefmt='grid'))
                        ns='y'
                        m='desserts'
                        ch=int(input("Enter you choice of desserts:"))
                        orders_food(m,ch)
                        ans=input("Do you wish to order more desserts? (y/n):")
                        print()
                
                        
                an=input("Would you like to order more food? (y/n):")
                print()

        elif ch==2:
            print("-------------------")
            print(" Laundry Services")
            print("-------------------")
            a.execute("Select * from laundry_services")
            data=a.fetchall()
            print(tabulate(a,headers=['Srno','Item','Price'],tablefmt='grid'))
            ans='y'
            while ans=='y':
                ch=int(input("Enter type of dress:"))
                m='laundry_services'
                services(m,ch)
                ans=input("Do you have more clothes to give? (y/n):")
                print()

    def add_on_services():
        global b
        print()
        print("1.Tourism Services \n2.Travel Services")
        print()
        ch=int(input("Please enter your choice:"))
        print()
        if ch==1:
            print("-----------------")
            print("TOURISM SERVICES")
            print("-----------------")
            print("Time slots:")
            print("a)8am-12pm \nb)1pm-5pm \nc)6pm-10pm \nd)10pm-2am \ne)3am-7am")
            l=['8am-12pm','1pm-5pm','6pm-10pm','10pm-2am','3am-7am']
            print()
            time=input("Enter your desired time slot:")
            t=['a','b','c','d','e']
            
            ans=input("Do you like to confirm the time slot chosen? (y/n):")
            if ans=="n":
                time=input("Please choose your desired timings:")

            for i in range (len(t)):
                if t[i]==time:
                    tm=l[i]
            print()
            print("Price with guide:175 Dhs \nPrice without guide:100 Dhs")
            gde=input("Do you wish to have a guide (y/n):")
            print()
            if gde=='y':
                dat="Tour"
                cos=175
                qty=1
                sql="INSERT INTO orders values('{}',{},{},{})".format(dat,qty,cos,cos)
                a.execute(sql)
                db.commit()
                print()
                print("YOUR TOUR WITH A GUIDE AT ",tm,"IS CONFIRMED")
                print()
                
            elif gde=='n':
                dat="Tour"
                cos=100
                qty=1
                q="INSERT INTO orders values('{}',{},{},{})".format(dat,qty,cos,cos)
                a.execute(q)
                db.commit()
                print()
                print("***YOUR TOUR WITHOUT A GUIDE AT ",tm,"IS CONFIRMED***")
                print()

        elif ch==2:
            print("----------------")
            print("TRAVEL SERVICES")
            print("----------------")
            print("1.Bus \n2.Plane")
            ch=int(input("Please choose your mode of transport:"))
            print()
            if ch==1:
                print("****")
                print("BUS")
                print("****")
                print("Price per adult=50 Dhs \nPrice per child (below 12 years)=20 Dhs")
                print()
                adl=int(input("Enter number of adults:"))
                chl=int(input("Enter number of children:"))
                date=input("Enter date of travel:")
                des=input("Enter destination:")
                price=adl*50+chl*20
                qty=adl+chl
                d=50
                c="Bus ticket"
                q="INSERT INTO orders values('{}',{},{},{})".format(c,qty,d,price)
                a.execute(q)
                db.commit()
                print()
                print("Your bus ticket for",date,'to',des,'is confirmed')
                print()

            elif ch==2:
                print("******")
                print("PLANE")
                print("******")
                print("Price per adult=550 Dhs \nPrice per child (below 12 years)= 320 Dhs")
                print()
                adl=int(input("Enter number of adults:"))
                chl=int(input("Enter number of children:"))
                date=input("Enter date of travel:")
                des=input("Enter destination:")
                price=550*adl+320*chl
                qty=adl+chl
                c="Plane ticket"
                d=550
                q="INSERT INTO orders values('{}',{},{},{})".format(c,qty,d,price)
                a.execute(q)
                db.commit()
                print()
                print("Your plane ticket for",date,'to',des,'is confirmed')
                print()

    def delete_orders():
        a.execute("Select * from orders")
        data=a.fetchall()   
        print(tabulate(data,headers=['Item','Quantity','Cost','Total_Price'],tablefmt='grid'))
        print()
        ans="y"
        while ans=="y":
            print()
            print("1.Delete the chosen item\n2.Reduce the number of the chosen item")
            ch=int(input("Enter choice:"))
            print()
            if ch==1:
                name=input("Enter the order name to be deleted:")
                sql="delete from orders where Item="+"'"+name+"'"
                a.execute(sql)
                db.commit()
                a.execute("Select * from orders")
                data=a.fetchall()
                print(tabulate(data,headers=['Item','Quantity','Cost','Total_Price'],tablefmt='grid'))
                print()
                
            elif ch==2:
                name=input("Enter the order name to be alter:")
                num=input("Enter the new quantity of item:")
                sql='update orders set Quantity='+str(num)+" "+'where Item='+"'"+str(name)+"'"
                a.execute(sql)
                db.commit()
                a.execute("Select * from orders")
                data=a.fetchall()
                print(tabulate(data,headers=['Item','Quantity','Cost','Total_Price'],tablefmt='grid'))
                print()
            ans=input("Wish to alter your order? (y/n):")
            print()

# Main program for customer
    ans="y"
    while ans=="y":
        print()
        print('1.Add to your order\n2.Delete from current order\n3.Bill\n4.Exit')
        print()
        B=input("Select your choice:")
        print()
        if B=='1':
            sql="Select * from main"
            a.execute(sql)
            print(tabulate(a, headers=["Sl No", "Services"], tablefmt="psql", showindex=False))
            ch=int(input("Enter your choice (1/2/3):"))
            if ch==1:
                room_booking()
            elif ch==2:
                room_services()
            elif ch==3:
                add_on_services()
        elif B=='2':
            delete_orders()
        elif B=='3':
            billing()
        ans=input("Do you want to make changes to your order?[y/n]:")
        if ans=='n':
            s="Drop table orders"
            a.execute(s)
            print()
            print(" *********************************************")
            print(" Thank you for visiting S&H Hotel ")
            print(" Ph.No : 056-8376239")
            print(" Khalifa St,\n     Behind World Trade Centre,\nNext to seashells cafe")
            print(" *********************************************")

def Rest_management():
    
    def insert(x):
        ta=x
        no=int(input("Enter Srno:"))
        na=input("Enter item:")
        pr=int(input("Enter price:"))
        Check=input("Are you sure you want to make the change?[y/n]:")
        if Check=='y':
            q="INSERT INTO {} values({},'{}',{})".format(ta,no,na,pr)
            a.execute(q)
            db.commit()
        print()
        print("************************")
        print(" Table after Insertion")
        print("************************")
        print()
        display(x)
        print()

    def update(x):
        ta=x
        no=int(input("Enter number of the item whose price you want to change:"))
        pr=int(input("Enter new price for item:"))
        q="UPDATE {} set Price={} WHERE Sl_no={}".format(ta,pr,no)
        a.execute(q)
        db.commit()
        print()
        print("************************")
        print("  Table after Updation")
        print("************************")
        display(x)
        print()

    def updateroom(x):
        ta=x
        no=int(input("Enter number of the item whose price you want to change:"))
        pr=int(input("Enter new price for item:"))
        q="UPDATE roombooking set Price_per_day={} WHERE Sl_no={}".format(pr,no)
        a.execute(q)
        db.commit()
        print()
        print("************************")
        print("  Table after Updation")
        print("************************")
        displayroom(x)
        print()

    def insertroom(x):
        no=int(input("Enter Srno:"))
        na=input("Enter name of the room:")
        av=int(input("Enter the availability of the room:"))
        pr=int(input("Enter price/day:"))
        q="INSERT ignore INTO roombooking values({},'{}',{},{})".format(no,na,av,pr)
        a.execute(q)
        db.commit()
            
    def delete(x):
        ta=x
        na=int(input("Enter srno for item:"))
        q="DELETE from {} WHERE Sl_no={}".format(ta,na)
        a.execute(q)
        db.commit()
        print()
        print("***********************")
        print(" Table after Deletion")
        print("***********************")
        if x=="roombooking":
            displayroom(x)
            print()
        else:
            display(x)
            print()

    def display(x):
        q="select Sl_no,Item,Price from {}".format(x)
        a.execute(q)
        data=a.fetchall()
        print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
        print()

    def displayroom(x):
        a.execute("Select * from roombooking")
        y=a.fetchall()
        print(tabulate(y,headers=['Srno',"Room",'Availability','Price'],tablefmt='grid'))
        print()

    print()
    ans='y'
    while ans=='y':
        print("Changes can be made in \n1.Accomodation \n2.Room Services")
        print()
        an=int(input("Input the item to be modified:"))
        if an==1:
            print("-----------------")
            print("  Accomodation")
            print("-----------------")
            a.execute("Select * from roombooking")
            y=a.fetchall()
            print(tabulate(y,headers=['Srno',"Room",'Availability','Price'],tablefmt='grid'))
            print()
            u='y'
            while u=='y':
                print()
                print("Modifications possible in the following methods")
                print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                print()
                c=int(input("Enter your choice:"))
                print()
                if c==1:
                    insertroom('roombooking')
                elif c==2:
                    updateroom('roombooking')
                elif c==3:
                    delete('roombooking')
                elif c==4:
                    print()
                    break
            
        elif an==2:  
            print("Menues:")
            print()
            print('1.Starters\n2.Main\n3.Desserts\n4.Beverages')
            print()
            ch=int(input("Enter your choice (1/2/3/4):"))
            print()
            if ch==1:
                x='y'
                while x=='y':
                    print("1.Salads\n2.Quesadillas\n3.Chaat")
                    print()
                    s=int(input("Enter your choice:"))
                    print()
                    if s==1:
                        a.execute("Select * from salads")
                        data=a.fetchall()
                        print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                        print()
                        u='y'
                        while u=='y':
                            print("Modifications possible in the following methods")
                            print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                            print()
                            c=int(input("Enter your choice:"))
                            print()
                            if c==1:
                                insert('salads')
                            elif c==2:
                                update('salads')
                            elif c==3:
                                delete('salads')
                            elif c==4:
                                print()
                                break
                            
                    elif s==2:
                        a.execute("Select * from quesadillas")
                        data=a.fetchall()
                        print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                        print()
                        while u=='y':
                            print("Modifications possible in the following methods")
                            print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                            c=int(input("Enter your choice:"))
                            print()
                            if c==1:
                                insert('quesadillas')
                            elif c==2:
                                update('quesadillas')
                            elif c==3:
                                delete('quesadillas')
                            elif c==4:
                                print()
                                break
                            
                    elif s==3:
                        a.execute("Select * from chaat")
                        data=a.fetchall()
                        print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                        print()
                        u='y'
                        while u=='y':
                            print("Modifications possible in the following methods")
                            print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                            print()
                            c=int(input("Enter your choice: "))
                            print()
                            if c==1:
                                insert('chaat')
                            elif c==2:
                                update('chaat')
                            elif c==3:
                                delete('chaat')
                            elif c==4:
                                print()
                                break
                            
                    x=input("Do you want to continue with Starters?[y/n]: ")
                    print()
                   
            elif ch==2:
                x='y'
                while x=='y':
                    print("1.Pasta\n2.Biriyani\n3.Roti\n4.Curry")
                    m=int(input("Enter your choice: "))
                    print()
                    if m==1:
                        a.execute("Select * from pasta")
                        data=a.fetchall()
                        print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                        print()
                        u='y'
                        while u=='y':
                            print("Modifications possible in the following methods")
                            print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                            print()
                            c=int(input("Enter your choice: "))
                            print()
                            if c==1:
                                insert('pasta')
                            elif c==2:
                                update('pasta')
                            elif c==3:
                                delete('pasta')
                            elif c==4:
                                print()
                                break

                    elif m==2:
                        a.execute("Select * from biriyani")
                        data=a.fetchall()
                        print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                        print()
                        while u=='y':
                            print("Modifications possible in the following methods")
                            print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                            print()
                            c=int(input("Enter your choice: "))
                            print()
                            if c==1:
                                insert('biriyani')
                            elif c==2:
                                update('biriyani')
                            elif c==3:
                                delete('biriyani')
                            elif c==4:
                                print()
                                break
                            
                    elif m==3:
                        a.execute("Select * from roti")
                        data=a.fetchall()
                        print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                        print()
                        while u=='y':
                            print("Modifications possible in the following methods")
                            print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                            print()
                            c=int(input("Enter your choice: "))
                            print()
                            if c==1:
                                insert('roti')
                            elif c==2:
                                update('roti')
                            elif c==3:
                                delete('roti')
                            elif c==4:
                                print()
                                break

                    elif m==4:
                        a.execute("Select * from curry")
                        data=a.fetchall()
                        print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                        print()
                        while u=='y':
                            print("Modifications possible in the following methods")
                            print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                            print()
                            c=int(input("Enter your choice: "))
                            print()
                            if c==1:
                                insert('curry')
                            elif c==2:
                                update('curry')
                            elif c==3:
                                delete('curry')
                            elif c==4:
                                print()
                                break

                    x=input("Do you want to continue with Mains[y/n]? ")
                    print()
                    
            elif ch==3:
                a.execute("Select * from desserts")
                data=a.fetchall()
                print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                print()
                u='y'
                while u=='y':
                    print("Modifications possible in the following methods")
                    print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        insert('desserts')
                    elif c==2:
                        update('desserts')
                    elif c==3:
                        delete('desserts')
                    elif c==4:
                        print()
                        break

            elif ch==4:
                a.execute("Select * from beverages")
                data=a.fetchall()
                print(tabulate(data,headers=['Srno','Item','Price'],tablefmt='grid'))
                print()
                u='y'
                while u=='y':
                    print("Modifications possible in the following methods")
                    print("1.Add a new record\n2.Update the price\n3.Delete a record\n4.Exit")
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        insert('beverages')
                    elif c==2:
                        update('beverages')
                    elif c==3:
                        delete('beverages')
                    elif c==4:
                        print()
                        break

            ans=input("Do you want to continue with the modifications?[y/n]: ")
            print()

#Main program
ans='Y'
while ans=='Y':
    print("-----------------------")
    print(" WELCOME TO S&H HOTEL")
    print("-----------------------")
    print()
    print("1.CUSTOMER\n2.STAFF")
    print()
    R=int(input("Enter your choice:"))
    print()
    if R==1:
        cust_management()
        break
    elif R==2:
        user=input("Enter your Staff ID name:")
        pas=int(input("Enter your Staff ID password:"))
        print()
        if pas==9948:
            Rest_management()
            break
        else:
            print("***********************************************")
            print(" Please approach your manager for verification")
            print("***********************************************")
            break            

