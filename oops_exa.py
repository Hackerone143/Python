class Bank:
    Bname='Karnataka Bank Lmt.'
    branch='Kodambakkam'
    helpline='140-524-896'
    Type='Private'

    def __init__(self,name,add,mob_no,acc_no,pan_no):
        self.name=name
        self.add=add
        self.mob_no=mob_no
        self.acc_no=acc_no
        self.pan_no=pan_no

    def disp(self):
        print('Name : ',self.name)
        print('Address : ',self.add)
        print('Mobile _no : ',self.mob_no)
        print('Account num : ',self.acc_no)
        print('Pan number : ',self.pan_no)
    '''@cassmethod
    def ch_branch(cls,newb):
        cls.branch=newb
    @classmethod
    def cont(cls,help_l):
        cls.helplin=help_l

    def addr(self,address):
        self.add=address
    def ph_no(self,phnum):
        self.mob_no=phnum'''

c1=Bank('Immanuvel','sdgdsg','9154445555955','94949465595595','DSGS94494F')
c2=Bank('john','uudbbgdbdbsv','444444412216555','8442649849565','jbdvkb445')

c1.disp()
c2.disp()


'''class college:
    cname='SMASC'
    cloc='kundrathur'
    affiliated='UNOM'
    def __init__(self,sname,smob,semis):
        self.sname=sname
        self.smob=smob
        self.semis=semis
    def disp(self):
        print('name : ',self.sname)
        print('Mobile : ',self.smob)
        print('Emis : ',self.semis)
    def ch_mob(self,new):
        self.smob=new
    def ch_emis(self,nemis):
        self.semis=nemis
s1=college('imman',144,1846)
s2=college('hbsds',645,94499)
'''
