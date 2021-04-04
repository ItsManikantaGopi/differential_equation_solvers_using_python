from prettytable import PrettyTable as pt
from math import *
from matplotlib import pyplot as pa
t=pt()
def eu(f,x,y,n,h):
    l=[]
    x=x
    y=y
    l.append(y)
    xv=[]
    xv.append(x)
    for i in range(n):
        x=x+h
        xv.append(round(x,5))
        y=y+h*(eval(f))
        l.append(round(y,5))
    pa.plot(xv,l,"b--",label="Eulers")
    return(xv,l)
def meu(f,n,h,xv,fa):
    mx=[]
    my=[]
    l=len(fa)
    a=fa[0]
    for i in range(l-1):
        x=xv[i]
        mx.append(x)
        y=fa[i]
        ja=eval(f)
        x=xv[i+1]
        y=fa[i+1]
        jb=eval(f)
        g=a+(h/2)*(ja+jb)
        a=g
        my.append(round(g,5))
    pa.plot(mx,my,"r-",label="Modified Eulers")
    return mx,my
def rk(q,h,n,a,b):
    xa=[]
    ya=[]
    for i in range(n):
        try:
            x=a
            y=b
            k1=h*eval(q)
            x=a+h/2
            y=b+k1/2
            k2=eval(q)*h
            x=a+h/2
            y=b+k2/2
            k3=eval(q)*h
            x=a+h
            y=b+k3
            k4=eval(q)*h
            k=(1/6)*(k1+2*(k2+k3)+k4)
            a=a+h
            b=b+k
            xa.append(round(a,5))
            ya.append(round(b,5)) 
        except:
            continue
    pa.plot(xa,ya,"g-",label="RK")
    return xa,ya
while 1:
    f=input("enter the function:=")
    x=float(input("enter the x value:="))
    y=float(input("enter the y value:="))
    n=int(input("enter the no of values:="))
    h=float(input("enter the step size:="))
    xv,fa=eu(f,x,y,n,h)
    mex,mey=meu(f,n,h,xv,fa)
    rx,ry=rk(f,h,n,x,y)
    l=len(mey)
    t.field_names=["x-values","Eulers","Modified Eulers","RK method"]
    for i in range(0,l):
        t.add_row([xv[i],fa[i],mey[i],ry[i]])
    print(t)
    pa.legend()
    pa.show()



