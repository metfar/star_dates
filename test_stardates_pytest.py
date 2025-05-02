from star_dates_module import StarDates;
from datetime import datetime;

def test_stardate_conversion():
    fecha = datetime(2006, 7, 24, 3, 50, 24);
    sd = StarDates(fecha);
    assert abs(sd.stardate() - 2398.3) < 0.05;

def test_from_stardate():
    sd = StarDates.from_stardate(2398.3);
    assert sd.fecha.year == 2006;
    assert sd.fecha.month == 7;
    assert sd.fecha.day == 24;
