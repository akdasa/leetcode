# 1603 Design Parking System

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.__available = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        available = self.__available[carType - 1]
        if available >= 1:
            available -= 1
            self.__available[carType - 1] = available
            return available >= 0
        else:
            return False