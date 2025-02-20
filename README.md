The project is an online booking system for hotels. The system that I are proposing here greatly simplifies the booking process for both the customer and the hotel staff. It presents interactive and up to date options in an easy-to-use manner. It is an integrated system with both the options for the customer to make a booking and the staff to make changes to the hotel's facilities.

It using Python as the front-end and MySQL as the back-end.
The program works based on database management. It collects all the information provided by the user and then stores it until the end. Every time the customer completes any online booking or makes modifications to his selected preference, his choice is updated and hence functions successfully. 

The Project is carried out in the following ways:

The program, when executed, displays two options to the user-Customer, Staff.

If the user chooses the ‘staff’ option:
A valid ID number (9948) and name is to be entered. An incorrect entry would require verification from the manager. 
When a correct ID number and name is entered, the staff gets an option to choose betIen ‘accommodation’ and ‘room services’.   
Then the details under the selected option will be displayed to which the staff can make changes (update the price/Add or delete the previously listed items).
After making the desired changes, the final details will be saved successfully which will then be displayed to the customers.

If the user chooses the ‘customer’ option:
When the user chooses the customer option, a table called Orders is created in MySQL which saves their orders. 
Orders are updated into the orders table by the order_food(), services() and order_room() functions. 
The customers are given the option to add to their bill, delete from their orders, display the bill and to exit the program. 
The functions of cust_management() are as follows:

1.	room_booking(): This function displays all the available rooms and allows the customer to select the room of their choice, the number of rooms and days. The choices are then updated into the orders table.
2.	room_services(): This function gives Food, Laundry services as choices to the customers.
•	Under the food option, the menu is displayed from the customer can select the food according to his choice and price.
•	Laundry services takes the count of the clothes put for wash.
3. add_on_services(): This function allows the hotel guests to book a city tour, a flight or bus ticket.
4. delete_orders(): This option helps the customer was to modify his choice.
The billing() function is used in preparing a bill/invoice for using the hotel and its facilities.
