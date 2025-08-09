#creating object and class and printing the data of the person

class Bank:
    bname='SBI'
    bloc='Chennai'
    IFSC='SBIN786'
    #here I have created a constructor ( which is used to initialize the values to the object )
    def __init__(obj, name, Mob_nu, mail):
        obj.name = name
        obj.Mob_nu = Mob_nu
        obj.mail = mail

c1=Bank('Sung Jin Woo',54844544,'usbdvjbjb@gmail.com')

c2=Bank('Jin Ho',49495,'usbdsdgsg@gmail.com')

c3=Bank('Woo jin wul',5444545,'usghreh35fjbjb@gmail.com')

c4=Bank('Chae Haeng',545487,'jbxvino98@gmail.com')

c5=Bank('Go Hin Hee',5944669,'jbsiibqr65@gmail.com')

print(c1.name,c1.Mob_nu,c1.mail)
print(c2.name,c2.Mob_nu,c2.mail)
print(c3.name,c3.Mob_nu,c3.mail)
print(c4.name,c4.Mob_nu,c4.mail)
print(c5.name,c5.Mob_nu,c5.mail)

'''c1=Bank()
c1.name='Sung Jin Woo'
c1.Mob_nu='452 985 765'
c1.mail='shadowMonarch@gmail.com'

c2=Bank()
c2.name='Christoper Nolan'
c2.Mob_nu='4543 025 765'
c2.mail='dirnolan@gmail.com'

c3=Bank()
c3.name='John Wick'
c3.Mob_nu='0101010101'
c3.mail='babayaga@gmail.com'

c4=Bank()
c4.name='Thor'
c4.Mob_nu='nil'
c4.mail='askarddude@gmail.com'

c5=Bank()
c5.name='Thomas Andrew'
c5.Mob_nu='442-996-264565'
c5.mail='kinghunter@gmail.com'''

