class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "This account belongs to %s and there is $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print "The balance: $%.2f" % self.balance
  def deposit(self, amount):
    if amount <=0:
      print "The amount must be more than 0"
      return
    else: 
      print "You deposited $%.2f" % amount
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount>self.balance:
      print "You cant withdraw more than you have"
      return
    else:
      print "You withdrew $%.2f" % amount
      self.balance -= amount
      self.show_balance()
my_account = BankAccount("Ewa")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account