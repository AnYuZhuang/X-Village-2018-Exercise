import re

class AuthSystem:
    
    def __init__(self):
        """Define regex"""
        self.username_regex = re.compile(r'Tom')
        self.password_regex = re.compile(r'tom059357')
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Welcome,Tom!")
            return True
        else: 
            print("Username format error! Your username is "+username)
            return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            print("Correct password")
            return True
        else:
            print("Password format error! Your password is "+password)
            return False
        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Valid user")

    
# Construct a object of type AuthSystem
auth = AuthSystem()

# authenticate the user's credentials
auth.authenticate(input("your_name:"),input("your_password:"))
