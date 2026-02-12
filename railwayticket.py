import logging

logging.basicConfig(
    filename="ticket.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Ticket:
    base_fare = 100  

    def __init__(self, ticket_id, passenger_name, no_of_tickets, booked=False, cancelled=False):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.no_of_tickets = no_of_tickets
        self.booked = booked
        self.cancelled = cancelled
        self.total_fare = 0

    def book_ticket(self):
        if not self.booked:
            self.booked = True
            self.cancelled = False
            logging.info("Ticket booked for %s ID: %s", self.passenger_name, self.ticket_id)
        else:
            logging.warning("Ticket %s is already booked", self.ticket_id)

    def cancel_ticket(self):
        if self.booked and not self.cancelled:
            self.cancelled = True
            logging.info("Ticket %s cancelled", self.ticket_id)
        elif not self.booked:
            logging.warning("Cannot cancel,ticket %s not booked yet", self.ticket_id)
        else:
            logging.warning("Ticket %s already cancelled", self.ticket_id)

    def calculate_fare(self):
        if self.booked and not self.cancelled:
            self.total_fare = self.no_of_tickets * Ticket.base_fare
            logging.info("Total fare for ticket %s: %s", self.ticket_id, self.total_fare)
        elif self.cancelled:
            logging.warning("Cannot calculate fare,ticket %s is cancelled", self.ticket_id)
        else:
            logging.warning("Cannot calculate fare,ticket %s not booked", self.ticket_id)

    @classmethod
    def update_base_fare(cls, new_fare):
        cls.base_fare = new_fare
        logging.info("Updated base fare per ticket: %s", cls.base_fare)
t1 = Ticket(201, "Priya", 3)
t1.book_ticket()
t1.calculate_fare()
t1.cancel_ticket()
t1.calculate_fare()
t1.update_base_fare(150)
t1.book_ticket()
t1.calculate_fare()
