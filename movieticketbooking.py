import logging

logging.basicConfig(
    filename="movieticket.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Movieticket:
    ticket_price = 100

    def __init__(self, ticket_id, movie_name, customer_name, seats=0, booked=False, cancelled=False):
        self.ticket_id = ticket_id
        self.movie_name = movie_name
        self.customer_name = customer_name
        self.seats = seats
        self.booked = booked
        self.cancelled = cancelled
        self.total_price = 0

    def book_seat(self, seats):
        if not self.booked:
            self.seats = seats
            self.booked = True
            self.cancelled = False
            logging.info("Seats booked for %s for movie %s (%s seats)", self.customer_name, self.movie_name, self.seats)
        else:
            logging.warning("Booking already done for ticket %s", self.ticket_id)

    def cancel_booking(self):
        if self.booked and not self.cancelled:
            self.cancelled = True
            self.seats = 0
            self.total_price = 0
            logging.info("Booking cancelled for ticket %s (%s)", self.ticket_id, self.customer_name)
        elif not self.booked:
            logging.warning("Cannot cancel, ticket %s not booked yet", self.ticket_id)
        else:
            logging.warning("Ticket %s already cancelled", self.ticket_id)

    def calculate_ticket_price(self):
        if self.booked and not self.cancelled:
            self.total_price = self.seats * Movieticket.ticket_price
            logging.info("Total ticket price for %s: %s", self.customer_name, self.total_price)
        elif self.cancelled:
            logging.warning("Cannot calculate price, ticket %s is cancelled", self.ticket_id)
        else:
            logging.warning("Cannot calculate price, ticket %s not booked", self.ticket_id)

    @classmethod
    def update_ticket_price(cls, new_price):
        cls.ticket_price = new_price
        logging.info("Updated ticket price: %s", cls.ticket_price)

t1 = Movieticket(301, "Avatar", "Priya")
t1.book_seat(3)
t1.calculate_ticket_price()
t1.cancel_booking()
t1.calculate_ticket_price()
t1.update_ticket_price(300)

t2 = Movieticket(101, "Dune", "Rosh")
t2.book_seat(1)
t2.calculate_ticket_price()
