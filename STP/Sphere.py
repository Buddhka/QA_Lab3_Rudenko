from Circle import Circle
import math
class Sphere(Circle):
    def __init__(self, x = 1, y = 1, radius = 1):
        """Конструктор объекта класса

        Args:
            x (int, optional): Координата X - положение центра окружности, лежащей в основании сферы, на оси X. Стандартное значение = 1.
            y (int, optional): Координата Y - положение центра окружности, лежащей в основании сферы, на оси Y. Стандартное значение = 1.
            radius (int, optional): Радиус окружности, лежащей в основании сферы. Стандартное значение = 1.
        """
        Circle.__init__(self, x, y , radius)
    
    def areaOfSphere(self):
        """Данный метод вычисляет площадь сферы

        Returns:
            float: Площадь сферы.
        """
        return 4 * math.pi * (self.radius ** 2)
    
    def volumeOfSphere(self):
        """Данный метод вычисляет объем сферы

        Returns:
            float: Объем сферы
        """
        return (4 * math.pi * (self.radius ** 3)) / 3
