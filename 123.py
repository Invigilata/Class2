class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setnewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Количество этажей в доме:", self.numberOfFloors)

my_house = House()
my_house.setnewNumberOfFloors(5)
my_house.setnewNumberOfFloors(10)