import unittest
from datetime import date

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 90000
        last_service_mileage = 11000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 45000
        last_service_mileage = 40000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
