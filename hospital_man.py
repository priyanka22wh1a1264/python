import logging
logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class Hospital:
    hname='kims'
    haddress='hyd'
    con_fee=500
    def __init__(self,name,registered,admitted,noofdays,paid_bill,bill=0):
        self.name=name
        self.registered=registered
        self.admitted=admitted
        self.noofdays=noofdays
        self.bill=bill
        self.paid_bill=paid_bill
    def admitpatient(self):
        if self.registered:
            self.admitted=True
            logging.info("patient admitted:%s",self.name)
        else:
            logging.warning("Not admitted")
        
    def dischargepatient(self):
        if self.paid_bill==True:
            logging.info("discharge patient")
        else:
            logging.warning("cant discharge")
    def calculate_bill(self):
        if self.registered and self.admitted:
            self.bill=Hospital.con_fee*self.noofdays
            logging.info("Total bill:%s",self.bill)
        else:
            logging.info("no bill to be payed")
    def paybill(self):
        if self.bill == 0:
            logging.info("No bill generated")
        elif self.paid_bill:
            logging.info("Bill already paid")
        else:
            self.paid_bill = True
            logging.info("Bill paid successfully")

    @classmethod
    def update_consul_fee(cls,new_confee):
        cls.con_fee=new_confee
        logging.info("updated consultation fee:%s",cls.con_fee)
p1 = Hospital('priya', True, False, 10, False)

p1.admitpatient()
p1.paybill()
p1.calculate_bill()
p1.dischargepatient()
p1.paybill()
p1.dischargepatient()
p1.update_consul_fee(600)
p2 = Hospital('rosh',False, False, 10, False)
p2.admitpatient()
p2.paybill()
p2.dischargepatient()
p2.calculate_bill()
p2.paybill()



        


