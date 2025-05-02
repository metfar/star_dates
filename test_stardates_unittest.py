import unittest;
from star_dates_module import StarDates;
from datetime import datetime;

class TestStarDates(unittest.TestCase):
    def test_stardate_conversion(self):
        fecha = datetime(2006, 7, 24, 3, 50, 24);
        sd = StarDates(fecha);
        self.assertAlmostEqual(sd.stardate(), 2398.3, places=1);

    def test_from_stardate(self):
        sd = StarDates.from_stardate(2398.3);
        self.assertEqual(sd.fecha.year, 2006);
        self.assertEqual(sd.fecha.month, 7);
        self.assertEqual(sd.fecha.day, 24);

if __name__ == '__main__':
    unittest.main();
