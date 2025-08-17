class fruit:
    def show(self):
        print("mango")

class Child(fruit):
    def show(self):
        # super().show() #this line for call super class also
        print("banana")

c = Child() #object for class child & fruit
c.show()