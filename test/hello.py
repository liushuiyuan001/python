print("Hello world!11")
# if True:
#     print("True")
# if False:
#     print("False")

counter = 100
miles = 1000.0
counter = 'abc'
name = "runoob"
tuplr = ("sbc", 123, 2, 33.33, 'rrr')
print(counter)
print(name)
print(miles)
print(type(counter))
print(type(miles))
print(type(name))
print(tuplr)
print(type(tuplr))
# tuplr[0] = 123

set = {1, 2, 3, 4, 3}
print(set)
print(type(set))


def hello():
    print("Hello")


hello()
import support

support.print_func('heooloooo')

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
print("1111111111")
firstName = 'shuiyuan'
lastName = 'liu'

fullName = f'{lastName} {firstName} '
print(fullName)

# import this

bicycles = ["trek", "cannondale", "redline", 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])
print(bicycles[-4])

bicycles.append("test")
print(bicycles)

bicycles = []
print(bicycles)
bicycles = [1, '2']
print(bicycles[0])
bicycles.clear()
print(bicycles)

magic = ['alice', 'david', 'carolina']

for mg in magic:
    print(mg)
print(mg)
print("hello")

for v in range(1, 5):
    print(v)

dict = {'name': 'zs', "age": 22}
print(dict['name'])
print(dict.get("grader", 123))


class Person:
    def __init__(self, age, user):
        self.age = age
        self.user = user

    def test(self):
        print("my name is ", self.user)


p1 = Person(22, 'zs')
p1.test()
p1.user = 'ls'
p1.test()