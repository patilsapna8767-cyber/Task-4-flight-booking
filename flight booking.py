from abc import ABC, abstractmethod
import random

# Flight Class - Encapsulation
class Flight:
    def __init__(self, flight_code, airline, source, destination, available_seats, base_fare):
        self.__flight_code = flight_code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = available_seats
        self.__base_fare = base_fare

    def get_flight_code(self): return self.__flight_code
    def get_available_seats(self): return self.__available_seats
    def get_base_fare(self): return self.__base_fare
    def get_details(self):
        return {"code": self.__flight_code, "airline": self.__airline, "source": self.__source,
                "destination": self.__destination, "seats": self.__available_seats, "fare": self.__base_fare}
    
    def check_availability(self, required): return self.__available_seats >= required
    
    def book_seats(self, count):
        if self.check_availability(count):
            self.__available_seats -= count
            return True
        return False

    def display_flight(self):
        print(f"{self.__flight_code:<8} | {self.__airline:<12} | {self.__source:<10} -> {self.__destination:<10} | Seats: {self.__available_seats:<3} | Fare: Rs.{self.__base_fare}")

# Abstraction
class Passenger(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def get_name(self): return self._name
    @abstractmethod
    def get_discount_percentage(self): pass
    @abstractmethod
    def get_category(self): pass
    def validate_details(self):
        if not self._name.strip(): return False, "Name empty"
        if not isinstance(self._age, int) or self._age <=0: return False, "Invalid age"
        return True, "Valid"

# Inheritance + Polymorphism
class RegularPassenger(Passenger):
    def get_discount_percentage(self): return 0
    def get_category(self): return "Regular"

class StudentPassenger(Passenger):
    def get_discount_percentage(self): return 15
    def get_category(self): return "Student"

class Booking:
    def __init__(self, flight, passenger, ticket_count):
        self.booking_id = f"BK{random.randint(1000,9999)}"
        self.flight = flight
        self.passenger = passenger
        self.ticket_count = ticket_count
        self.final_amount = self.calculate_fare()

    def calculate_fare(self):
        base_total = self.flight.get_base_fare() * self.ticket_count
        discount_per = self.passenger.get_discount_percentage()
        self.base_total = base_total
        self.discount_amount = (base_total * discount_per) / 100
        return base_total - self.discount_amount

    def display_summary(self):
        print("\n" + "="*50)
        print(f" BOOKING CONFIRMED - {self.booking_id}")
        print("="*50)
        print(f"Passenger : {self.passenger.get_name()} ({self.passenger.get_category()})")
        print(f"Flight    : {self.flight.get_flight_code()}")
        print(f"Tickets   : {self.ticket_count}")
        print(f"Base Fare : Rs.{self.base_total}")
        print(f"Discount  : Rs.{self.discount_amount}")
        print(f"Final Amt : Rs.{self.final_amount}")
        print("="*50 + "\n")

class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("AI202", "Air India", "Delhi", "Mumbai", 50, 4500),
            Flight("6E303", "IndiGo", "Raipur", "Hyderabad", 30, 3800),
            Flight("SG404", "SpiceJet", "Nagpur", "Bangalore", 40, 5200),
        ]
        self.current_booking = None

    def display_flights(self):
        print("\n--- Available Flights ---")
        for f in self.flights: f.display_flight()
        print()

    def find_flight_by_code(self, code):
        for f in self.flights:
            if f.get_flight_code().lower() == code.lower(): return f
        return None

    def book_flight(self):
        code = input("Enter Flight Code: ").strip()
        flight = self.find_flight_by_code(code)
        if not flight: print("Error: Invalid code\n"); return
        name = input("Enter Name: ").strip()
        try: age = int(input("Enter Age: ").strip())
        except: print("Error: Age must be number\n"); return
        print("1. Regular (0%) 2. Student (15%)")
        p_type = input("Choice (1/2): ").strip()
        passenger = StudentPassenger(name, age) if p_type=="2" else RegularPassenger(name, age)
        valid, msg = passenger.validate_details()
        if not valid: print(f"Error: {msg}\n"); return
        try: tickets = int(input("Enter No. of Tickets: ").strip())
        except: print("Error: Tickets must be number\n"); return
        if tickets <=0 or not flight.check_availability(tickets):
            print(f"Error: Only {flight.get_available_seats()} seats left\n"); return
        flight.book_seats(tickets)
        self.current_booking = Booking(flight, passenger, tickets)
        self.current_booking.display_summary()

    def view_booking(self):
        if not self.current_booking: print("\nNo booking found\n")
        else: self.current_booking.display_summary()

    def run(self):
        print("\nWelcome to Flight Booking System\n")
        while True:
            print("1. View Flights 2. Book Flight 3. View Booking 4. Exit")
            ch = input("Enter choice: ").strip()
            if ch=="1": self.display_flights()
            elif ch=="2": self.book_flight()
            elif ch=="3": self.view_booking()
            elif ch=="4": print("\nGoodbye!\n"); break
            else: print("Invalid choice\n")

if __name__ == "__main__":
    FlightBookingSystem().run()