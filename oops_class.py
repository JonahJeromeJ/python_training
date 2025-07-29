# class Person:
#     def print_name(self,name):
#         print("my name is" +name)

# person = Person()
# person.print_name("shiva")


#all function in class 
# class City:
#     def addCityDetails(self,name,country):
#         self.name=name
#         self.country=country
#     def printCityDetails(self):
#         print("cityname is" + self.name)
#         print("country name is" + self.country)
    
# mumbai=City()
# mumbai.addCityDetails("delhi","india")
# mumbai.printCityDetails()

# delhi=City()
# delhi.addCityDetails("chennai","india")
# delhi.printCityDetails()


# print(mumbai.name)


class Person1:
    def addenterDetails(self,name):
        self.name=name

class Person2(Person1):
    def printenterDetails(self):
        print("cityname is" + self.name)
        

delhi=Person2()
delhi.addenterDetails("iuiuh")

delhi.printenterDetails()
#'Person2' object has no attribute 'addenterDetails'. Did you mean: 'printenterDetails'?




class Person1:
    def addenterDetails(self, name1):
        self.name1 = name1

class Person2(Person1):
    def againenterdetails(self, name2):
        self.name2 = name2

class Person3(Person2):
    def printenterDetails(self):
        print("cityname is " + self.name2)

# Create an object of Person3
delhi = Person3()

# Set both details
delhi.addenterDetails("iuiuh")
delhi.againenterdetails("Delhi")   # <- This was missing!

# Print the details
delhi.printenterDetails()
