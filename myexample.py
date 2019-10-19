# print('hello world')
# salary = {'john':10,'sally':20,'meeta':24}
#
# for key in salary:
#     print(salary[key])

#enumerate specially helpful when used with for loops
# mylist = ['a','b','c']
# for index,letter in enumerate(mylist):
#     print(letter)
#     print("is at index {}".format(index))
#
#
# #.join operator is useful to join th4e strings
#
# mylist.append('d')
# print('-x-'.join(mylist))

# def secrect_check(string):
#     if 'secret' in string.lower():
#         print(True)
#     else:
#         print(False)

# secrect_check("my name is SECRET")

# def code_maker(mystring):
#     emp_list=list(mystring)
#     for index,letter in enumerate(mystring):
#         for vowel in 'aeiou':
#             if(letter.lower()==vowel):
#                 emp_list[index] = 'x'
#
#     emp_list=''.join(emp_list)
#     print(emp_list)
#
# mystring = 'srinivas'
# code_maker(mystring)

# def check_ten(n1,n2):
#     result = n1+n2
#     if(result==10):
#         print(True)
#     else:
#         print(False)
#
# check_ten(8,3)

# def first_upper(mystring):
#     upper=mystring[0]
#     print(upper.upper())
#
# first_upper('seema')

# def last_two(mystring):
#     if len(mystring)<2:
#         print('Error')
#     else:
#         print(mystring[-2::])
#
#
# last_two(mystring='srt')

# class Dog():
#
#     #class object attributes
#     #these doesn't require self keyword because they are declared outside
#     #__init__ call. so what ever be the dog name in this example, the species
#     #is going to be a mamal
#     species = 'mamal'
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#
#
# sam = Dog('lab','samy')
# print(sam.breed)
# print(sam.name)
# print(sam.species)

# class Circle():
#
#     pi = 3.14
#
#     def __init__(self,radius = 1):
#         self.radius=radius
#
#     #self basically tells the python that user is referring to the instance of
#     # of the object that you create while applying this class
#     def area(self):
#         return(self.radius * self.radius*self.pi)
#
#     def circumference(self):
#         return(2*self.pi*self.radius)
#
# mycircle = Circle(10)
# print(mycircle.radius)
# print(mycircle.area())
# print(mycircle.circumference())

# Inheritence
# class Animal():
#
#     def __init__(self,fur):
#         self.fur = fur
#
#     def report(self):
#         print("Animal")
#
#     def eat(self):
#         print("eating")
#
# #Inheriting the features of Animal as the dog belongs to the same category
# # this allows us to inherit the features of the clready exisiting code
# # thatr is why the oops allows us to use the code" reusability"
#
# class Dog(Animal):
#
#     def __init__(self,fur):
#         Animal.__init__(self,fur)
#         print('Dog created')
#
#     def report(self):
#         print("I'am a dog!!")
#
#
# d = Dog('fuzzy')
# d.eat()
# d.report()

#special methods are useful to interact to the built in functions such as len
#print functions etc etc

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return("The Title: {}, Author: {}".format(self.title,self.author))


    def __len__(self):
        return(self.pages)

mybook = Book("Pyhton rocks!",'Srini',250)
length = len(mybook)
print(length)
