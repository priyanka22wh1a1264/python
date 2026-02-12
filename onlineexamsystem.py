import logging
logging.basicConfig(
    filename="onlineexam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Onlinexam:
    passmarks=30
    noofque=50
    scoreforeachque=1
    def __init__(self,sname,queattempted,noofcorrect,attended):
        self.sname=sname
        self.queattempted=queattempted
        self.noofcorrect=noofcorrect
        self.attended=attended
        self.score=0
    def start_exam(self):
        if self.attended==True:
            logging.info("started exam:%s",self.sname)
        else:
            logging.warning("cant write the exam")
    def submit_exam(self):
        if self.queattempted==50:
            logging.info("submit exam")
        else:
            logging.warning("attempt all the questions")
    def calculate_score(self):
        if self.noofcorrect>0:
            self.score=Onlinexam.scoreforeachque*self.noofcorrect
            logging.info("score:%s",self.score)
        else:
            logging.info("score is 0")
    @classmethod
    def updatepassmarks(cls,new_passmarks):
        cls.passmarks=new_passmarks
        logging.info("new pass marks:%s",cls.passmarks)

s1=Onlinexam('priya',50,10,True)
s1.start_exam()
s1.calculate_score()
s1.submit_exam()
s1.updatepassmarks(20)

    

