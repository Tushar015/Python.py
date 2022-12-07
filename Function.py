#import math  #def student(Name,course="PES308"):
 #   print("Name",Name)
 #   print("Course",course)
#student("Rahul","PEV108")
#student("safhhff")

#def emp(en,ed,country="INDIA"):
 #   print("NAME:",en)
  #  print("EDUCATION:",ed)
   # print("COUNTRY:",country)
#a=input("Employer name:  ")
#b=input("Employer education: ")
#c=input("Country: ")
#if c!="INDIA":
#    emp(a,b,c)
#else:
 #   emp(a,b)


#def stu1(regno,name):
#    print("Name: ",name)
#    print("Reg.no.: ",regno)
#stu1(name="Ram",regno=12234)
#stu1(32432,name="Sam")
#stu1(regno=12323,"tan")   #this 3rd case give us a error because positional argument follows keyword argument


#def stu1(*name):
 #   print("K22ST",name)
#stu1("ram","sam","tan",4263)


#def add(*add):
#    a=0
#    for i in add:
 #       a=a+i
#    print(a)
#add(3,4,8,9,10)


#def great(*greater):
 #   a=0
  #  for i in greater:
   #     if a<i:
    #        a=1
    #print(a)
#great(20,40,20)


#d=lambda x:x*3
#print(d(8))


#salary=int(input())
#tax=lambda x:salary*20/100
#print(tax(10000))

#d=lambda a:a+10
#print(d(10))


#d=lambda a:a+15
#print(d(15))
#c=lambda x,y:x*y
#print(c(2,3))


#p=int(input())
#o=lambda p:p*433
#print(o(6))

#def f1(a,b):
#    return (a*b)
#d=f1(2,3)
#print((d))
     #or
#print(f1(2,3))


#def p(a):
#    return lambda x:x*a
#d=p(2)
#print(d(15))
#t=p(400)
#print((t(400)))


#def e():
 #   a=90
 #   print(a)
#def e2():
#    a=32
#    print(a)
#e()
#e2()


#a=10
#def e():
 #   global a
 #   a=200
#def e2():
 #   global w
 #   w=900
#print(a)
#e()
#e2()
#print(a)
#print(w)


#def p(n):
#    if n==1:
#        return n
#    else:
#        return n*p(n-1)
#d=p(5)
#print(d)
    #or
#n=int(input())
#if n<0:
#    print(("no factorial"))
#elif n==0:
#    print("factorial is 1")
#else:
#    print(p(n))


#def p(x,y):
 #   if y==0:
  #      return x
   # else:
    #    return 1+p(x,y-1)
#a=int(input())
#b=int(input())
#d=p(a,b)
#print(d)


#def rev(x,y):
#    if x==0:
#        return y
#    else:
#        return rev(x//10,y*10 + x%10)
#f=rev(345,0)
#print(f)


#def sum(a,b):
#    print(a+b)



#def fun1(Student_name,Regno):
#    print("Name:",Student_name)
#    print("Reg.no.:",Regno)
#def fun2(eng,math,ece):
#    return "Average_no.:",(eng+math+ece)/3
#def fun3(pincode):
#    print("Pincode:",pincode)



def pow1(a):
    print(a**2)
def mult(x,y):
    print(x*y)
def sum(z,v):
    print(z+v)

















































