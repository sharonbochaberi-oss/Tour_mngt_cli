from service import *

def get_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("❌ Enter a valid number.")

def get_float(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except:
            print("❌ Enter a valid number.")

def get_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ Input cannot be empty.")


def menu():
    while True:
        print("\n--- TOUR MANAGEMENT ---")
        print("1. Add Tour")
        print("2. View Tours")
        print("3. Search Tour")
        print("4. Update Tour")
        print("5. Delete Tour")

        print("6. Add Customer")
        print("7. View Customers")
        print("8. Search Customer")
        print("9. Update Customer")
        print("10. Delete Customer")

        print("11. Add Booking")
        print("12. View Bookings")
        print("13. View Customer Bookings")
        print("14. View Tour Bookings")
        print("15. Update Booking")
        print("16. Cancel Booking")

        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_tour(
                get_text("Destination: "),
                get_int("Duration: "),
                get_float("Price: "),
                get_int("Seats: ")
            )

        elif choice == "2":
            view_tours()

        elif choice == "3":
            search_tour(get_text("Destination: "))

        elif choice == "4":
            update_tour(
                get_int("Tour ID: "),
                get_float("New Price: "),
                get_int("New Duration: "),
                get_int("New Seats: ")
            )

        elif choice == "5":
            delete_tour(get_int("Tour ID: "))

        elif choice == "6":
            add_customer(
                get_text("Name: "),
                get_text("Email: "),
                get_text("Phone: ")
            )

        elif choice == "7":
            view_customers()

        elif choice == "8":
            search_customer(get_text("Name: "))

        elif choice == "9":
            update_customer(
                get_int("Customer ID: "),
                get_text("New Name: "),
                get_text("New Email: "),
                get_text("New Phone: ")
            )

        elif choice == "10":
            delete_customer(get_int("Customer ID: "))
            
        elif choice == "11":
            add_booking(
                get_int("Customer ID: "),
                get_int("Tour ID: "),
                get_int("Seats: ")
            )

        elif choice == "12":
            view_bookings()

        elif choice == "13":
            view_bookings_by_customer(get_int("Customer ID: "))

        elif choice == "14":
            view_bookings_by_tour(get_int("Tour ID: "))

        elif choice == "15":
            update_booking(
                get_int("Booking ID: "),
                get_int("New Seats: ")
            )

        elif choice == "16":
            cancel_booking(get_int("Booking ID: "))

        elif choice == "0":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice.")


menu()