class Car(object):
    def __init__(self,colour,company,milage,maxspeed,seating):
        self.colour=colour
        self.company=company
        self.milage=milage
        self.speed=0
        self.maxspeed=maxspeed
        self.seating=seating
    def start(self):
        print("Car has started")
    def stop(self):
        print(self.company,"has stopped")
    def changeSpeed(self,speed):
        self.speed=speed

car1=Car("White","maruti","11km/l",180,6)
car1.start()
car1.changeSpeed(20)
print(car1.speed)
car1.stop()
