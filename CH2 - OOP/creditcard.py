class CreditCard:
	""" A consumer credit card."""

	def __init__(self, customer, bank,acnt, limit): # Constructor of the class
		"""Create a new credit card instance.

		The initial balance is zero

		customer name of customer("Kwame Yaw")
		bank name of bank("Access Bank")
		acnt account identifier("5391 0375 9387 5309")
		limit credit limit(measured in dollars)
		"""

		self._customer = customer
		self._bank = bank 
		self._account = acnt
		self._limit = limit 
		self._balance = 0  

	def get_customer(self):
		"""Return name of customer"""
		return self._customer

	def get_bank(self):
		""""Return the bank's name"""
		return self._bank

	def get_account():
		"""Return the card identifying number"""
		return self._account

	def get_limit():
		"""Return current credit limit"""
		return self._limit 

	def get_balance():
		"""Return current balance."""
		return self._balance

	def charge(self, price):
		"""Charge given price to the card,assuming suffcient credit limit.
		Return True if charge was processed;
		False if charge was denied.
		"""
		if price + self._balance > self._limit:
			return False
		else:
			self._balance += price
			return True

	def make_payment(self,amount):
		"""Process customer payment that reduces balance."""
		self._balance -= amount

if __name__ == "__main__":
	wallet = []
	wallet.append(CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309" , "2500"))
	wallet.append(CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954" , "3500"))
	wallet.append(CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309" , " 5000" ))

	for val in range(1, 17):
		wallet[0].charge(val)
		wallet[1].charge(val * 2)
		wallet[2].charge(val * 3)

	for c in range(3):
		print(f"Customer = {wallet[c].get_customer()}")
		print(f"Bank = {wallet[c].get_bank()}")
		print(f"Account = {wallet[c].get_account()}")
		print(f"Balance = {wallet[c].get_balance()}")
		while wallet[c].make_payment(100):
			print("New balance = {wallet[c].get_balance()}")
		print()