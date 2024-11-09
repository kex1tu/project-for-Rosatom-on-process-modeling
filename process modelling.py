from math import *
from tkinter import *
def s():
    global zt, rz, sz, ht, rh, sh, n
    zt=int(n1.get())
    rz=float(n2.get())
    sz=float(n3.get())
    ht=int(n4.get())
    rh=float(n5.get())
    sh=float(n6.get())
    n=int(n7.get())
    vubor()

def vubor():
    s= int(selected.get())
    x, y=main(s)
    grafik(len(x), y)
    

def typ1(zt, rz, n):
        xt = []
        yt = []
        xn = zt;
        xt.append(0)
        yt.append(xn)
        for i in range(1, n+1):
            xn = xn + xn*rz;
            xt.append(i)
            yt.append(int(xn))
        return xt, yt

def typ2(ht, rh, zt, sh, n):
        xt = []
        yt = []
        xt.append(0)
        yt.append(ht)
        for i in range(1, n+1):
            zt1 = zt + rz*zt - sz*zt*ht
            hn = ht + rh*zt1*ht - sh*ht
            xt.append(i)
            yt.append(int(hn))
            ht = hn
        return xt, yt

def typ3(zt, rz, sz, ht, n):
        xt = []
        yt = []
        xt.append(0)
        yt.append(zt)
        for i in range(1, n+1):
            ht1 = ht + rh*zt*ht - sh*ht
            zn = zt + rz*zt - sz*zt*ht1
            xt.append(i)
            yt.append(int(zn))
            zt = zn
        return xt, yt

def main(typ):
        if typ==1:
            x, y = typ1(zt, rz, n)
        elif typ == 2:
            x, y = typ2(ht, rh, zt, sh, n)
        elif typ == 3:
            x, y = typ3(zt, rz, sz, ht, n)
        return x, y

root = Tk()
fr=Frame(root)
top2=Frame(fr, width=500, height=200)
top=Frame(fr, width=50, height=20, bg='black')
lb1=Label(top2, text='к-во жертв')

n1=Entry(top2, width=10)

lb2=Label(top2, text='рожд. жертв')

n2=Entry(top2, width=10)

lb3=Label(top2, text='смерть жертв')

n3=Entry(top2, width=10)

lb4=Label(top2, text='к-во хищ')

n4=Entry(top2, width=10)

lb5=Label(top2, text='рожд. хищ')

n5=Entry(top2, width=10)

lb6=Label(top2, text='смерть хищ')

n6=Entry(top2, width=10)

lb7=Label(top2, text='к-во циклов')

n7=Entry(top2, width=10)


itog=Button(top2, text='Рассчитать', command=s)

selected=IntVar()

vb1=Radiobutton(top2, text='первый', value=1, variable=selected)
vb2=Radiobutton(top2, text='второй', value=2, variable=selected)
vb3=Radiobutton(top2, text='третий', value=3, variable=selected)

fr.pack()
top2.pack(side=LEFT)
top.pack()
vb1.pack()
vb2.pack()
vb3.pack()
lb1.pack()
n1.pack()
lb2.pack()
n2.pack()
lb3.pack()
n3.pack()
lb4.pack()
n4.pack()
lb5.pack()
n5.pack()
lb6.pack()
n6.pack()
lb7.pack()
n7.pack()
itog.pack(side=BOTTOM)

canv= Canvas(top, width = 1000, height = 1000, bg ='lightblue')
canv.pack()
def grafik(x,y):
    canv.delete("all")
    canv.create_line(1, 690, 990, 690, width=2, arrow=LAST)
    canv.create_line(5, 690, 5, 10, width=2, arrow=LAST)

    kmx = 4
    kmy = 60
    j= 5
    k = 690
    for i in range(1, x):
        try:
            canv.create_line(j,k,i*kmx+5,690-log(y[i])*kmy,width=2)
            j = i*kmx+5
            k = 690-log(y[i])*kmy
            if i%10==0:
                canv.create_line(i*kmx,695,i*kmx,685,width=2)
                canv.create_text(i*kmx,670, text = str(i), fill="purple",
                font=("Helvectica", "10"))
        except:
            pass
root.mainloop()

    
