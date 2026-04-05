from dataclasses import dataclass

@dataclass
class Tour:
    id: int
    destination: str
    duration: int
    price: float
    available_seats: int

@dataclass
class Customer:
    id: int
    name: str
    email: str
    phone: str

@dataclass
class Booking:
    id: int
    customer_id: int
    tour_id: int
    seats_booked: int