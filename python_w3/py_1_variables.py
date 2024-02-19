x=5      #int
y='john'  #str  
print(x)
print(y)

#overwrite
z = 4       # z is of type int
z = "Sally" # z is now of type str
print(z)

a=str(3)
b=int(3)
c=float(3)
print(a,b,c)

# type()

d=5
e='jon'
f=4.5
print(type(d))
print(type(e))
print(type(f))


g=4
G='sally'
print(G)
print(g)
#not overwrite

h,i,j="o",'b','c'
print(h)
print(i)
print(j)

h=i=j='orange'
print(h)
print(i)
print(j)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#global Variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#glob al keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)




