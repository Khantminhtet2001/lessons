print(10>9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def __len__(self):
    return 0            #O IS FALSE

myobj = myclass()
print(bool(myobj))


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")