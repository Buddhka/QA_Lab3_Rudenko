import Circle, Cylinder, Sphere, random
from Circle import Circle
from Cylinder import Cylinder
from Sphere import Sphere
import unittest
class TestCircleAndCylinderMethods(unittest.TestCase):
    def setUp(self):
        """Данный метод позволяет определить инструкции, которые будут выполняться перед и после каждого метода тестирования.
        """
        self.circle = Circle()
        self.cylinder = Cylinder()
        self.sphere = Sphere()
        self.circle.x = random.randint(1,100)#Генерируется случайное число от 1 до 100 
        self.circle.y = random.randint(1,100)
        self.cylinder.height = random.randint(1, 100)
        self.angle = random.randint(1,360)#Генерируется случайное число от 1 до 360
    
    def testCalculateRadius(self):
        """Данный метод тестирует расчет радиус-окружности, который не может быть равен 0. Вообще он может, но для складности теста не сможет.
        """
        self.assertNotEqual(self.circle.calculateRadius(), 0)

    def testLengthOfCircle(self):
        """Данный метод тестирует расчет длины окружности, которая не может быть равна 0. В данном случае(если равна 0), окружность будет являться точкой.
        """
        self.assertNotEqual(self.circle.lengthOfCircle(), 0)

    def testAreaOfCircle(self):
        """Данный метод тестирует расчет площади окружности, которая не может быть равна 0. В данном случае(если равна 0), окружность будет являться точкой.
        """
        self.assertNotEqual(self.circle.areaOfCircle(), 0)

    def testAreaOfSector(self):
        """Данный метод тестирует площадь сектора окружности, которая должна находиться в пределах от 0 до S. В нижней границе(0) сектор не будет существовать,
          в верхней(S) он будет являться всей окружностью.
        """
        self.assertTrue(0 <= self.circle.areaOfSector(self.angle) <= self.circle.areaOfCircle())

    def testAreaOfSegment(self):
        """Данный метод тестирует площадь сегмента окружности, которая должна находиться в пределах от 0 до S. В нижней границе(0) сегмент не будет существовать,
          в верхней(S) он будет являться всей окружностью.
        """
        self.assertTrue(0 <= self.circle.areaOfSegment(self.angle) <= self.circle.areaOfCircle())

    def testVolumeOfCylinder(self):
        """Данный метод тестирует расчет объема цилиндра, который не должен быть равен 0.
        """
        self.assertNotEqual(self.cylinder.volumeOfCylinder(), 0)

    def testLateralSurfaceArea(self):
        """Данный метод тестирует расчет площади боковой поверхности цилиндра, которая не может быть равна 0.
        """
        self.assertNotEqual(self.cylinder.lateralSurfaceArea(), 0)
    
    def testFullSurfaceArea(self):
        """Данный метод тестирует расчет площади всех сторон цилиндра, которая не может быть равна 0.
        """
        self.assertNotEqual(self.cylinder.fullSurfaceArea(), 0)

    def testAreaOfSphere(self):
        """Данный метод тестирует расчет площади сферы, которая не может быть меньше 0.
        """
        self.assertTrue(0 <= self.sphere.areaOfSphere())

    def testVolumeOfSphere(self):
        """Данный метод тестирует расчет объема сферы, который не может быть меньше 0.
        """
        self.assertTrue(0 <= self.sphere.volumeOfSphere())


if __name__ == "__main__":
    unittest.main()