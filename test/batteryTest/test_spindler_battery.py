import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date("2020-05-15")
        last_service_date = date("2015-05-15")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date("2020-05-15")
        last_service_date = date("2019-05-15")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())