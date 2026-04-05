#  Tour Management CLI Application

## Overview

The **Tour Management CLI Application** is a command-line based system designed to help a travel firm manage:

* Tours
* Customers
* Bookings

It allows users to perform full CRUD (Create, Read, Update, Delete) operations and manage relationships between customers and tours through bookings.


## Objectives

* Provide a simple CLI interface for managing travel data
* Maintain relationships between customers and tours
* Store data persistently using JSON
* Prevent invalid inputs and system crashes

---

## System Design

### Object Relationships

* **Customer → Bookings → Tours**
* One customer can have multiple bookings
* Each booking is linked to one tour

```
Customer (1) ────< Booking >──── (1) Tour
```


##  Features

### Tours

* Add a new tour (destination, duration, price, seats)
* View all tours
* Search tours by destination
* Update tour details
* Delete a tour


### Customers

* Add a new customer (name, email, phone)
* View all customers
* Search customers by name
* Update customer details
* Delete a customer


### Bookings

* Create booking (link customer to tour)
* Specify number of seats
* View all bookings
* View bookings by:

  * Customer
  * Tour
* Update booking (change seats)
* Cancel booking


## Technologies Used

* **Python 3**
* **JSON** (for data storage)
* Command Line Interface (CLI)


## Project Structure

```
tour_mngt_cli/
│
├── main.py        # CLI interface & user input handling
├── service.py    # Business logic (CRUD operations)
├── storage.py     # JSON data handling
├── models.py      # Data structures (optional)
├── data.json      # Stored data (auto-generated)
└── README.md      # Project documentation
```


## Installation & Setup

### 1. Install Python

Download and install Python from:
https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

### 2. Clone or Download Project

```bash
git clone <your-repo-url>
cd tour_management_cli


### 3. Run the Application

```bash
python main.py
```

## Usage Guide

After running the program, you will see a menu:
--- TOUR MANAGEMENT ---
1. Add Tour
2. View Tours
...
16. Cancel Booking
0. Exit

Enter the number corresponding to the action you want.


## Future Improvements

* Add email format validation
* Prevent duplicate customers
* Restore seats when booking is cancelled
* Add login/authentication system
* Add reporting (e.g., total bookings, revenue)


## Example Workflow

1. Add a Tour
2. Add a Customer
3. Create a Booking
4. View Bookings
5. Update or Cancel Booking


## Author
Sharon Bochaberi.

