import sys

f1=open(sys.argv[1]+".txt","r")
f2=open("ex.txt","r")
origin=f1.read().split("\n")
newdata=f2.read().split("\n")
# print(origin)
originlen=len(origin)
newlen=len(newdata)
# print(originlen)
# print(newlen)
xo=origin[0].split(",")[0]
yo=origin[0].split(",")[1]
xn=newdata[0].split(",")[0]
yn=newdata[0].split(",")[1]
xo=int(xo)
xn=int(xn)
yo=int(yo)
yn=int(yn)
idx=abs(xo-xn)
idy=abs(yo-yn)
# print(idx)
# print(idy)
count=0
for i in range(1,originlen):
    if(i+3>newlen):
        break
    # print(origin[i])
    # print(newdata[i-1])
    # print(newdata[i+1])
    xo = origin[i].split(",")[0]
    yo = origin[i].split(",")[1]
    xn1 = newdata[i-1].split(",")[0]
    yn1 = newdata[i-1].split(",")[1]
    xn2 = newdata[i+1].split(",")[0]
    yn2 = newdata[i+1].split(",")[1]
    xn3 = newdata[i].split(",")[0]
    yn3 = newdata[i].split(",")[1]
    # print(yn2)
    # print("xo " + xo)
    xo = int(xo)
    # print("yo " + yo)
    yo = int(yo)
    # print("xn1 " + xn1)
    # print("yn1 " + yn1)
    # print("xn2 " + xn2)
    # print("yn2 " + yn2)
    # print("xn3 " + xn3)
    # print("yn3 " + yn3)
    xn1 = int(xn1)
    yn1 = int(yn1)
    xn2 = int(xn2)
    yn2 = int(yn2)
    xn3=int(xn3)
    yn3=int(yn3)
    # print("1 x "+str(abs(xo-xn1)))
    # print("1 y "+str(abs(yo-yn1)))
    # print("2 x " + str(abs(xo - xn2)))
    # print("2 y " + str(abs(yo - yn2)))
    # print("3 x " + str(abs(xo - xn3)))
    # print("3 y " + str(abs(yo - yn3)))
    # print(abs(xo-xn2))
    # print(abs(yo-yn2))
    if((abs(xo-xn1)<=idx+10 and abs(yo-yn1)<=idy+10) or( abs(xo-xn2)<=idx+10 and abs(yo-yn2)<=idy+10) or( abs(xo-xn3)<=idx+10 and abs(yo-yn3)<=idy+10) ):
        continue
    else:
        count+=1
        # print(count)


per=(count+abs(originlen-newlen))/originlen

out=1-per
if(out<0):
    out=0
f=open("result.txt","w")
f.write(str(out))