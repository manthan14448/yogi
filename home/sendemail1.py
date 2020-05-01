import  smtplib
server=smtplib.SMTP_SSL("smptp.gmail.com",465)
server.login("manthangelot@gmail.com","manthan@330")
server.sendmail("manthangelot@gmail.com",
                "manthangelot310@gmail.com","Its work!!!!!:)")
server.quit()
