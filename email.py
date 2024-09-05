class EmailValidator:
    def __init__(self,min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
    def validate_name(self,name):
        return len(name) >= self.min_length
        return True
    def validate_mail(self, mail):
        return mail in self.mail
        return False
    def validate_domain(self, domain):
        return domain in self.domain
        return False
    def validate(self, email):
        username, mail_domain = email.split('@')
        mail, domain = mail_domain.split('.')
        return False
        
        return self.validate_mail(mail) and self.validate_domain(domain)
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("per77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
        