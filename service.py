from storage import load_data, save_data

data = load_data()

# ---------------- TOURS ----------------
def add_tour(destination, duration, price, seats):
    tour = {
        "id": len(data["tours"]) + 1,
        "destination": destination,
        "duration": duration,
        "price": price,
        "available_seats": seats
    }
    data["tours"].append(tour)
    save_data(data)
    print("✅ Tour added successfully!")

def view_tours():
    if not data["tours"]:
        print("No tours available.")
        return
    for t in data["tours"]:
        print(t)

def search_tour(destination):
    found = False
    for t in data["tours"]:
        if destination.lower() in t["destination"].lower():
            print(t)
            found = True
    if not found:
        print("❌ No matching tours found.")

def update_tour(tour_id, price, duration, seats):
    for t in data["tours"]:
        if t["id"] == tour_id:
            t["price"] = price
            t["duration"] = duration
            t["available_seats"] = seats
            save_data(data)
            print("✅ Tour updated!")
            return
    print("❌ Tour not found.")

def delete_tour(tour_id):
    before = len(data["tours"])
    data["tours"] = [t for t in data["tours"] if t["id"] != tour_id]
    save_data(data)
    if len(data["tours"]) < before:
        print("✅ Tour deleted.")
    else:
        print("❌ Tour not found.")


# ---------------- CUSTOMERS ----------------
def add_customer(name, email, phone):
    customer = {
        "id": len(data["customers"]) + 1,
        "name": name,
        "email": email,
        "phone": phone
    }
    data["customers"].append(customer)
    save_data(data)
    print("✅ Customer added!")

def view_customers():
    if not data["customers"]:
        print("No customers found.")
        return
    for c in data["customers"]:
        print(c)

def search_customer(name):
    found = False
    for c in data["customers"]:
        if name.lower() in c["name"].lower():
            print(c)
            found = True
    if not found:
        print("❌ No matching customers.")

def update_customer(customer_id, name, email, phone):
    for c in data["customers"]:
        if c["id"] == customer_id:
            c["name"] = name
            c["email"] = email
            c["phone"] = phone
            save_data(data)
            print("✅ Customer updated!")
            return
    print("❌ Customer not found.")

def delete_customer(customer_id):
    before = len(data["customers"])
    data["customers"] = [c for c in data["customers"] if c["id"] != customer_id]
    save_data(data)
    if len(data["customers"]) < before:
        print("✅ Customer deleted.")
    else:
        print("❌ Customer not found.")


# ---------------- BOOKINGS ----------------
def add_booking(customer_id, tour_id, seats):
    for t in data["tours"]:
        if t["id"] == tour_id:
            if t["available_seats"] >= seats:
                booking = {
                    "id": len(data["bookings"]) + 1,
                    "customer_id": customer_id,
                    "tour_id": tour_id,
                    "seats_booked": seats
                }
                data["bookings"].append(booking)
                t["available_seats"] -= seats
                save_data(data)
                print("✅ Booking successful!")
                return
            else:
                print("❌ Not enough seats.")
                return
    print("❌ Tour not found.")

def view_bookings():
    if not data["bookings"]:
        print("No bookings found.")
        return
    for b in data["bookings"]:
        print(b)

def view_bookings_by_customer(customer_id):
    found = False
    for b in data["bookings"]:
        if b["customer_id"] == customer_id:
            print(b)
            found = True
    if not found:
        print("❌ No bookings for this customer.")

def view_bookings_by_tour(tour_id):
    found = False
    for b in data["bookings"]:
        if b["tour_id"] == tour_id:
            print(b)
            found = True
    if not found:
        print("❌ No bookings for this tour.")

def update_booking(booking_id, seats):
    for b in data["bookings"]:
        if b["id"] == booking_id:
            b["seats_booked"] = seats
            save_data(data)
            print("✅ Booking updated!")
            return
    print("❌ Booking not found.")

def cancel_booking(booking_id):
    before = len(data["bookings"])
    data["bookings"] = [b for b in data["bookings"] if b["id"] != booking_id]
    save_data(data)
    if len(data["bookings"]) < before:
        print("✅ Booking cancelled.")
    else:
        print("❌ Booking not found.")