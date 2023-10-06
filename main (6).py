class bankAccount:

def__init__(self,account_number,account_holder_name,initial_balance=0.0):
  self._account_number = account_munber
  self._account_holder_name = account_holder_name
  self._account_balance = initial_balance
  
  def deposit(self, amount):
    if amount > 0:
      self.account_balance += amount
      #self.__account_balance_balance = self.__account
      print("deposited ₹{}. new balance:₹{}".format(amount,self.__account_balanced))
    else:
      print("Invalid deposit amount.Please deposite a positive amount.")
      
  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balnced:
      self.__account_balance_= amount
      print("withdrew ₹{}.new balance:₹{}".format(amount<self.__accont_balance))
      else