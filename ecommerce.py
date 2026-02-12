import logging
logging.basicConfig(
    filename="order.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class Order:
    tax_percent = 5  
    def __init__(self, order_id, customer_name, items, prices, placed=False, cancelled=False):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.prices = prices  
        self.placed = placed
        self.cancelled = cancelled
        self.total_price = 0
    def place_order(self):
        if not self.placed:
            self.placed = True
            logging.info("Order placed: %s by %s", self.order_id, self.customer_name)
        else:
            logging.warning("Order %s already placed", self.order_id)
    def cancel_order(self):
        if self.placed and not self.cancelled:
            self.cancelled = True
            logging.info("Order cancelled: %s", self.order_id)
        elif not self.placed:
            logging.warning("Cannot cancel, order %s not placed yet", self.order_id)
        else:
            logging.warning("Order %s already cancelled", self.order_id)
    def calculate_total(self):
        if self.placed and not self.cancelled:
            subtotal = sum(self.prices)
            tax_amount = subtotal * Order.tax_percent / 100
            self.total_price = subtotal + tax_amount
            logging.info("Total price for order %s: %.2f", self.order_id, self.total_price)
        elif self.cancelled:
            logging.warning("Cannot calculate total, order %s is cancelled", self.order_id)
        else:
            logging.warning("Cannot calculate total, order %s not placed", self.order_id)
    @classmethod
    def update_tax(cls, new_tax):
        cls.tax_percent = new_tax
        logging.info("Updated tax percentage: %s%%", cls.tax_percent)
o1 = Order(101, "Priya", ["Laptop", "Mouse"], [50000, 1500])
o1.place_order()
o1.calculate_total()
o1.cancel_order()
o1.calculate_total()
o1.update_tax(10)
o1.calculate_total()
