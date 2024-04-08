# Copyright (c) 2024, Ashwini Khadse and contributors
# For license information, please see license.txt

# import frappe
from datetime import datetime
from frappe.model.document import Document
# from frappe.utlis import getdate


class Driver(Document):
	
	def validate(self):
		self.set_full_name()
		self.calculate_age()
		

	def set_full_name(self):
		self.full_name = f"{self.first_name} {self.last_name}"

	
	# def calculate_age(self):

	# 	# today = datetime.today()

	# 	year = getdate.year
	# 	print(year)

	# 	dob = self.dob.split("-")# 1999-12-13 (in frappe the date is in reverse format if you add it in correct format)
	# 	print(dob)
	# 	self.age = year - int(dob[0]) 
		# print(self.age)



	def calculate_age(self):

		today = datetime.today()

		year = today.year
		
		dob = self.dob.split("-")# 1999-12-13 (in frappe the date is in reverse format if you add it in correct format)
		
		self.age = year - int(dob[0]) 
		
		
