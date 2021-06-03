import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter import messagebox 
class hitung(object):
    
    level, attack, tallent, multiplier, cr, cd, deffmultiplier,noncrit,crit,avgdmg,hilcur  = 0,0,0,0,0,0,0,0,0,0,0
    inputan = ""
    def __init__(self, level, attack, tallent, multiplier, cr, cd, deffmultiplier, noncrit, crit, avgdmg, inputan,hilcurl) :
        self.level = level
        self.attack = attack
        self.tallent = tallent
        self.multiplier = multiplier
        self.cr = cr
        self.cd = cd
        self.deffmultiplier = deffmultiplier
        self.noncrit = noncrit
        self.crit = crit
        self.avgdmg = avgdmg
        self.inputan = inputan
        self.hilcurl = hilcurl
    def deffmultiplierfunc(self):
        self.deffmultiplier = (self.level+100)/(self.level+(self.hilcurl+200))
    def damagenoncrit(self):
        self.noncrit= self.attack * (self.tallent/100) * (1+(self.multiplier/100)) * self.deffmultiplier * 0.9
    def damagecrit(self):
        self.crit= self.attack * (self.tallent/100) * (1+(self.multiplier/100)) * (1+(self.cd/100)) * self.deffmultiplier * 0.9
    def damageavgdps(self):
        self.avgdps= self.attack * (self.tallent/100) * (1+(self.multiplier/100)) * (1+((self.cd/100)*(self.cr/100))) * self.deffmultiplier * 0.9
    def setdata(self, level, attack, tallent, multiplier, cr, cd, hilcurl ):
        self.level = level
        self.attack = attack
        self.tallent = tallent
        self.multiplier = multiplier
        self.cr = cr
        self.cd = cd
        self.hilcurl = hilcurl
        pass
    def getnoncrit(self):
        return self.noncrit
    def getcrit(self):
        return self.crit
    def getavgdps(self):
        return self.avgdps
kalkulasikan = hitung(0,0,0,0,0,0,0,0,0,0,"",0)
def clear():
    stringoutcrit.set("")
    stringoutnoncrit.set("")
    stringoutavgdps.set("")

def submit():
    level = stringlevel.get()
    attack = stringattack.get()
    tallent = stringtallent.get()
    multiplier = stringdamagemul.get()
    cr = stringCR.get()
    if float(cr)>100:
        cr = 100
    cd = stringCD.get()
    hilcurl = stringhilcurl.get()
    kalkulasikan.setdata(float(level),float(attack),float(tallent),float(multiplier),float(cr),float(cd),int(hilcurl))
    kalkulasikan.deffmultiplierfunc()
    kalkulasikan.damagenoncrit()
    kalkulasikan.damagecrit()
    kalkulasikan.damageavgdps()
    crit = kalkulasikan.getcrit()
    noncrit = kalkulasikan.getnoncrit()
    avgdps = kalkulasikan.getavgdps()
    stringoutnoncrit.set(str(int(noncrit)))
    stringoutcrit.set(str(int(crit)))
    stringoutavgdps.set(str(int(avgdps)))
root = Tk()

root.geometry('600x450')
root.configure(background='#C1CDCD')
root.title('Genshin Impact Damage Calculator')


stringlevel = StringVar()
inputcharlvl=Entry(root, textvariable=stringlevel).place(x=172, y=54)
stringattack = StringVar()
tInputattack=Entry(root, textvariable=stringattack).place(x=173, y=91)
stringtallent = StringVar()
tInputtallent=Entry(root, textvariable=stringtallent).place(x=172, y=125)
stringdamagemul = StringVar()
tInputdamagemul=Entry(root, textvariable=stringdamagemul).place(x=172, y=161)
stringCR = StringVar()
tInputCR=Entry(root, textvariable=stringCR).place(x=173, y=196)
stringCD = StringVar()
tInputCD=Entry(root, textvariable=stringCD).place(x=172, y=230)
stringhilcurl =StringVar()
tInputHilcurl = Entry(root, textvariable=stringhilcurl).place(x=172, y=260)
Label(root, text='Character level', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=10, y=51)
Label(root, text='Total attack', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=10, y=89)
Label(root, text='Tallent multiplier %', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=10, y=124)
Label(root, text='Damage multiplier', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=10, y=160)
Label(root, text='Crit Rate', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=10, y=194)
Label(root, text='Crit Damage', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=10, y=227)
Label(root, text='Enemy Level', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=10, y=257)
Label(root, text='Damage if crit', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=407, y=54)
Label(root, text='Damage if not crit', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=396, y=127)
Label(root, text='Average DPS', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=407, y=197)
Label(root, text='*Assuming if enemy is Hilcurl', bg='#C1CDCD', font=('arial', 12, 'normal')).place(x=328, y=284)
stringoutcrit = StringVar()
toutputcrit=Entry(root, textvariable=stringoutcrit,state='readonly').place(x=393, y=83)
stringoutnoncrit = StringVar()
toutputnotcrit=Entry(root,textvariable=stringoutnoncrit,state='readonly').place(x=394, y=159)
stringoutavgdps = StringVar()
tOutputAvrDPS=Entry(root,textvariable=stringoutavgdps,state='readonly').place(x=395, y=235)

btn1 = Button(root, command = submit, text="SUBMIT").place(x=50,y=300)
btn2 = Button(root, command = clear, text="CLEAR").place(x=150,y=300)
root.mainloop()
