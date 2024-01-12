class bank:
    def getroi(self):
        return 10;
class sbi(bank):
    def getroi(self):
        return 7;


class icici(bank):
    def getroi(self):
        return 8;
b1=bank()
b2=sbi()
b3=icici()
print("bank rate of intrest:",b1.getroi());
print("sbi rate of intrest:",b2.getroi());
print("icici rate of intrest:",b3.getroi());