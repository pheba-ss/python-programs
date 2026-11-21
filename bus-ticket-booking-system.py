# Bus Ticket Booking System

seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
names = ["", "", "", "", "", "", "", "", "", ""]

while True:
    print("\n------ BUS TICKET BOOKING SYSTEM ------")
    print("1. Book Ticket")
    print("2. View Seat Availability")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Book Ticket
    if choice == "1":

        print("\nAvailable Seats:")

        for seat in range(1, 11):
            if seats[seat - 1] == 0:
                print(seat, end=" ")

        print()

        seat_number = int(input("Enter Seat Number: "))

        if seat_number >= 1 and seat_number <= 10:

            if seats[seat_number - 1] == 0:

                name = input("Enter Passenger Name: ")
                age = int(input("Enter Passenger Age: "))

                if age >= 0:
                    price = 500

                    if age < 12:
                        price = 250
                        print("Child Discount Applied")

                    elif age > 60:
                        price = 350
                        print("Senior Citizen Discount Applied")

                    else:
                        print("No Discount Applied")

                    seats[seat_number - 1] = 1
                    names[seat_number - 1] = name

                    print("\nTicket Booked Successfully")
                    print("Passenger Name:", name)
                    print("Seat Number:", seat_number)
                    print("Final Ticket Price:", price)

                else:
                    print("Invalid age!")

            else:
                print("Seat is already booked!")

        else:
            print("Invalid seat number!")

    # View Seat Availability
    elif choice == "2":

        print("\n------ SEAT AVAILABILITY ------")

        for seat in range(1, 11):
            if seats[seat - 1] == 0:
                print("Seat", seat, "- Available")
            else:
                print("Seat", seat, "- Booked by", names[seat - 1])

        available_seats = 0

        for seat in seats:
            if seat == 0:
                available_seats += 1

        print("Total Available Seats:", available_seats)
        print("Total Booked Seats:", 10 - available_seats)

    # Cancel Ticket
    elif choice == "3":

        seat_number = int(input("Enter Seat Number to Cancel: "))

        if seat_number >= 1 and seat_number <= 10:

            if seats[seat_number - 1] == 1:
                seats[seat_number - 1] = 0
                names[seat_number - 1] = ""

                print("Ticket Cancelled Successfully")

            else:
                print("Seat is not booked!")

        else:
            print("Invalid seat number!")

    # Exit
    elif choice == "4":
        print("Thank You for Using Bus Ticket Booking System")
        break

    else:
        print("Invalid choice!")
