import smtplib, ssl

class SMTP:
    
    def __init__(self,email,password):
        self.email = email
        self.password = password

    def check(self):
        print(self.email);

    def sendEmail(self,toaddrs, msg):
        serverSMTP =  "smtp.gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(serverSMTP, 465, context=context) as server:
         try:
          server.login(email, password)
          print("Email Logged");
          server.sendmail(self.email, toaddrs, msg)
         except ex:
          print("An exception occurred", ex)