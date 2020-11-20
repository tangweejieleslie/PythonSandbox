d = dict()

print(d)

d["a"] = 0
d["a"] += 1

d[1]=1

print(d)




def thisIsAFunction():
    print("Hi from a function")

thisIsAFunction()

# https://www.programiz.com/python-programming/class
class Person:
    age = 10
    def greet(self):
        print("Hi! My age is ", self.age)

harry = Person()
harry.greet()
Person.greet(harry)


myList = [1,2,3,4]
print(myList[-4]) #negative index = last item

print("3:4",myList[3:4])
print("2:3",myList[2:3])
print(":3",myList[:3])
print("0:1",myList[0:1])
print("0:2",myList[0:2])



print(myList.pop(2))
print(myList)

