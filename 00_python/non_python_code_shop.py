class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("Sipping Chai...")

    def add_sugar(self, amount):
        print('add the sugar')

my_Chai = Chai(sweetness=5, milk_level='medium')
my_Chai.add_sugar(2)