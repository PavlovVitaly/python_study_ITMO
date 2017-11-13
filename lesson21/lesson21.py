# Unit-тестирование


from unittest import TestCase

from Vector import Vector


# fixtures - окружение для тестирования.
#
# TestCase - тестовый случай
# - setUp()/tearDown()
# - setUpClass()/tearDownClass()
# - setUpModule()/tearDownModule()
#
# test suit - набор тестов
#
# test runner - исполнитель тестов


class VectorTests(TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2)
        self.v2 = Vector(2, 1)

    def tearDown(self):
        del self.v1
        del self.v2

    def test_summa(self):
        """Тестирует суммирование векторов"""
        v3 = self.v1 + self.v2

        answer = (v3.x, v3.y)
        result = (3, 3)
        self.assertTupleEqual(answer, result)

    def test_minus(self):
        """Тестирует разность векторов"""
        v3 = self.v1 - self.v2

        answer = (v3.x, v3.y)
        result = (-1, 1)
        self.assertTupleEqual(answer, result)
