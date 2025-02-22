The Online Hotel Booking System is designed to simplify and enhance the booking experience for both customers and hotel staff. This interactive system provides real-time updates and an intuitive user interface, ensuring a seamless reservation process. It integrates both customer booking functionalities and administrative controls for hotel staff to manage accommodations and services efficiently. The system stores and updates user data dynamically, ensuring that all modifications made by customers or staff are reflected instantly.

Technology Stack:
Python, MySQL

System Functionality:
  Upon execution, the system presents two user roles: Customer and Staff.

  For Hotel Staff:
  Staff members must log in using a valid ID number (9948) and name. An incorrect entry requires verification from the hotel manager.
  Once authenticated, staff can choose between two management options:
    Accommodation Management – Modify room details, update prices, and manage availability.
    Room Services Management – Add, remove, or adjust room service options such as food and laundry.
  All changes are saved and reflected in the customer-facing interface.

  For Customers:
  When a customer logs in, a table called "Orders" is created in MySQL to store their selections.
  Customers can perform the following actions:
    Room Booking: View available rooms, select preferred options, and specify the number of rooms and duration of stay.
    Room Services:
      Food Ordering: Displays a menu where customers can select food items along with prices.
      Laundry Services: Allows customers to specify the number of clothing items for washing.
    Add-On Services: Book additional amenities such as city tours, flight tickets, or bus reservations.
    Modify Orders: Customers can add or remove items from their bill before finalizing their booking.
    Billing and Invoice Generation: The system calculates the total cost and generates an invoice for the customer.
    
This project provides an efficient, user-friendly platform for hotel management, enhancing the customer experience while streamlining hotel operations.
