from Circle import Circle
import math
class Cylinder(Circle):
    def __init__(self, x = 1, y = 1, radius = 1, height = 1):
        """Конструктор объекта класса

        Args:
            x (int, optional): Координата X - положение центра окружности, лежащей в основании цилиндра, на оси X. Стандартное значение = 1.
            y (int, optional): Координата Y - положение центра окружности, лежащей в основании цилиндра, на оси Y. Стандартное значение = 1.
            radius (int, optional): Радиус окружности, лежащей в основании цилинда. Стандартное значение = 1.
            height (int, optional): Высота цилиндра(расстояние от центра окружности в основании до центра параллельной ей окружности). Стандартное значение = 1.
        """
        Circle.__init__(self, x, y, radius)
        self.height = height

    def calculateRadiusVector(self):
        """Данный метод высчитывает радиус-вектор до центра цилиндра.

        Returns:
            int, float: Расстояние от центра координат до центра цилиндра.
        """
        stub = math.sqrt((self.x ** 2) + (self.y ** 2))
        return math.sqrt((stub ** 2) + (self.height ** 2))
    
    def __str__(self):
        """Строковый вывод полей объекта класса

        Returns:
            string: Строка, содержащая значения полей данного объекта класса.
        """
        return f"X = {self.x} | Y = {self.y} | radius = {self.radius} | height = {self.height}"
    
    def volumeOfCylinder(self):
        """Данный метод вычисляет объем цилиндра.

        Returns:
            float: Объем цилиндра.
        """
        return math.pi * (self.radius ** 2) * self.height
    
    def lateralSurfaceArea(self):
        """Данный метод вычисляет площадь боковой стороны цилиндра.

        Returns:
            float: Площадь боковой стороны цилиндра
        """
        return 2 * math.pi * self.radius * self.height
    
    def fullSurfaceArea(self):
        """Данный метод вычисляет полную площадь сторон цилиндра, включая нижнюю и верхнюю.

        Returns:
            float: Площадь всех сторон цилиндра.
        """
        return 2 * math.pi * self.radius * (self.height + self.radius)
    