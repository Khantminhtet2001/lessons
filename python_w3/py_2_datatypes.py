#main funciton is type()

#int
x=5
print(x)

#float
x=0.5
print(x)

#complex
x=1j
print(x)


#str
x="hello world"
print(x)


# list
x=['🤍','💚','💙']
print(x)


#tuple
x=('🤍','💚','💙')
print(x)


#set
x={'🤍','💚','💙'}
print(x)
print(len(x))

#dict

x={
    "name":"khant min htet",
    "age":22,
    "edu":"student"
}
print(x)

#frozenset
x=frozenset({'🤍','💚','💙'})
print(x)

#bool

x= True
y= False

print(x)
print(y)

#bytes
x=b"hello"
print(x)

# bytearray
x=bytearray(5)
print(x)

x=memoryview(bytes(5))
print(x)

#none
x=None
print(x)


#random number

import random
print(random.randrange(1,50))


#looping through in string

for x in "khant min htet":
    print(x)


#check Sting
    
txt="I am Khant Min Htet"
print("Min" in txt)
print("zoe" in txt)
print("zoe" not in txt) #not

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


b="hello world"
print(b[4:9])
print(b.upper())
print(b.lower())
print(b.strip())   # beginning or end - whitespace remove
print(b.replace("h","d"))
print(b.split())


#format string
y=19
fs=f'your age is {y}'

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))



