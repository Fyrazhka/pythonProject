class Car(object):
    color="White"
    def __init__(self,maxSpeed,mileage):
        self.maxSpeed=maxSpeed
        self.mileage=mileage
    def assginSeatingCapacity(self,capacity):
        self.seatingCapacity=capacity
    def show(self):
        print(" Max speed: ",self.maxSpeed ,"\n","Mileage: ",self.mileage,"\n","Color: ",self.color,"\n","Seating capacity: ",self.seatingCapacity)



if __name__ == '__main__':
    car1=Car(200,50000)
    car1.assginSeatingCapacity(5)
    car1.show()
    car2 = Car(180, 75000)
    car2.assginSeatingCapacity(4)
    car2.show()