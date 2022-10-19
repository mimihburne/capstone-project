'''
Write email class with method and attributes:
-	Class attributes: e_type=str(email)
-	Instance attributes:
o	(string) address (mimihburne@gmail.com)
o	(int) address length
-	Methods
o	Valid_email() [using re]
	Checks whether @ is in address
	Checks whether ends with .com or .mail
	No characters ($, ~, :)
	Returns true or false
'''
import re

class Email:

    e_type = 'email'

    def __init__(self, address):
        self.address = address
        self.address_len = len(address)

    def valid_email(self): #length?
        if re.search("@{1}.*.com$", self.address) != None and re.search('[$, ~, :]', self.address) == None:
            return True
        else:
            return False

myaddress = Email('mimi@gmail.com')
print(myaddress.valid_email())

class Outlook(Email):
    pass

myaddress = Outlook('mimi@gmail.com')
'''
-	Stretcher: write inherited child case for a given email provider(outlook, gmail etc.)
-	Additional checks
'''
