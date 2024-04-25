import math
class Circle: 
    def __init__(self, x = 1, y = 1, radius = 1): 
        """Конструктор объекта класса

        Args:
            x (int, optional): Координата X - положение центра окружности на оси X. Стандартное значение = 1.
            y (int, optional): Координата Y - положение центра окружности на оси Y. Стандартное значение = 1.
            radius (int, optional): Радиус окружности. Стандартное значение = 1.
        """
        self.x = x #Поле Х - это положение центра окружности по координате Х.
        self.y = y #Поле Y - это положение центра окружности по координате Y.
        self.radius = radius #Поле radius - радиус окружности.

    def __str__(self): #Вывод полей объекта класса в строковом формате
        return f"X = {self.x} | Y = {self.y} | radius = {self.radius}"

    def calculateRadius(self): 
        """Данный метод вычисляет радиус-вектор.

        Returns:
            int, float: Расстояние до центра окружности.
        """
        return math.sqrt((self.x**2) + (self.y**2))
    
    def lengthOfCircle(self):
        """Данный метод вычисляет длину окружности.

        Returns:
            float: Длина окружности.
        """
        return 2 * math.pi * self.radius
    
    def areaOfCircle(self):
        """Данный метод вычисляет площадь окружности.

        Returns:
            float: Площадь окружности.
        """
        return math.pi * (self.radius ** 2)
    
    def areaOfSector(self, angle):
        """Данный метод вычисляет площадь сектора.

        Args:
            angle (int): Аргумент, являющийся углом от центра окружности.

        Returns:
            float: Площадь сектора.
        """
        return math.pi * (self.radius ** 2) * (angle / 360)
    
    def areaOfSegment(self, angle):
        """Данный метод вычисляет площадь сегмента, заданного углом.

        Args:
            angle (int): Аргумент, являющийся углом от центра окружности.

        Returns:
            float: Площадь сегмента.
        """
        return math.pi * (self.radius ** 2) * (angle / 360) - (((self.radius ** 2) * math.sin(angle)) / 2)



    def inputCircleData(self):
        """Данный метод позволяет редактировать поля объекта класса.
        """
        print("Input X coordinate: ")
        self.x = int(input())#Внос координаты Х
        print("Input Y coordinate: ")
        self.y = int(input())#Внос координаты Y
        print("Input radius: ")
        self.radius = int(input())#Внос радиуса окружности.

    def additionCircle(firstCircle, secondCircle):
        """Данный метод складывает два объекта класса и возвращает объект этого же класса.

        Args:
            firstCircle (Circle): Аргумент, являющийся первым слагаемым типа Circle.
            secondCircle (Circle): Аргумент, являющийся вторым слагаемым типа Circle.

        Returns:
            Circle: Объект класса Circle.
        """
        finalCircle = Circle()
        finalCircle.x = (firstCircle.x + secondCircle.x) / 2
        finalCircle.y = (firstCircle.y + secondCircle.y) / 2
        finalCircle.radius = firstCircle.radius + secondCircle.radius
        return finalCircle
    