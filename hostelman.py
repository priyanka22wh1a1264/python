import logging

logging.basicConfig(
    filename="hostel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Hostel:
    room_rent = 5000  

    def __init__(self, room_no, student_name, allocated=False, vacated=True, months=0):
        self.room_no = room_no
        self.student_name = student_name
        self.allocated = allocated
        self.vacated = vacated
        self.months = months
        self.total_fee = 0

    def allocate_room(self, months):
        if not self.allocated:
            self.allocated = True
            self.vacated = False
            self.months = months
            logging.info("Room %s allocated to %s for %s months", self.room_no, self.student_name, self.months)
        else:
            logging.warning("Room %s is already allocated", self.room_no)

    def vacate_room(self):
        if self.allocated and not self.vacated:
            self.vacated = True
            self.allocated = False
            logging.info("Room %s vacated by %s", self.room_no, self.student_name)
            self.months = 0
        else:
            logging.warning("Room %s is already vacant", self.room_no)

    def calculate_monthly_fee(self):
        if self.allocated and not self.vacated:
            self.total_fee = Hostel.room_rent * self.months
            logging.info("Total fee for room %s: %s", self.room_no, self.total_fee)
        else:
            logging.warning("Room %s is not allocated, no fee to calculate", self.room_no)

    @classmethod
    def update_room_rent(cls, new_rent):
        cls.room_rent = new_rent
        logging.info("Updated room rent per month: %s", cls.room_rent)


r1 = Hostel(101,'priya')
r1.allocate_room(6)
r1.calculate_monthly_fee()
r1.vacate_room()
r1.update_room_rent(6000)
r2 = Hostel(102,'rosh')
r2.allocate_room(3)
r2.calculate_monthly_fee()
