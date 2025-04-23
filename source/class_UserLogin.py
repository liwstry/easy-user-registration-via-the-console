from email_validator import validate_email, EmailNotValidError

class UserLogin:
    
    def __init__(self, fio, login, password, email):
        self.fio = fio
        self.login = login
        self.password = password
        self.email = email
        
    def check_fio(self, fio):
        if fio.count(" ") == 2:
            return True
        return False

    def check_password(self, password):
        if len(password) >= 7 and any(i.islower() for i in password) and any(i.isupper() for i in password):
            return True
        return False
    
    def check_email(self, email):
        valid_email = validate_email(email)
        return valid_email['email']
