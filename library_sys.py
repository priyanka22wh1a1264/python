import logging
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Library:
    fineperday=5
    def __init__(self,bname,bid,book_available,noofdays):
        self.bname=bname
        self.bid=bid
        self.fine=0
        self.book_available=book_available
        self.noofdays=noofdays
        
    def issue_book(self):
        if self.book_available:
            logging.info("issue book :%s",self.bname)
            self.book_available = False
        else:
            logging.warning("book not vailable")
            
    def return_book(self):
        if self.fine > 0:
            logging.info("pay fine=%s", self.fine)
            self.fine = 0   
        logging.info("book returned")
        self.book_available = True

    def cal_fine(self):
        if self.noofdays>15:
            self.fine=(self.noofdays-15)*Library.fineperday
            logging.info("fine to be payed =%s", self.fine)
        else:
            self.fine=0
            logging.info("no fine")
    @classmethod
    def updatedfineperday(cls,new_fineperday):
        cls.fineperday=new_fineperday
        logging.info("new fine per day :%s",cls.fineperday)
b1=Library('math',234,True,17)
b1.issue_book()
b1.cal_fine()
b1.return_book()
b1.updatedfineperday(10)
b1.cal_fine()
b1.return_book()





