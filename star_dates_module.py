import sys;
from datetime import date, timedelta;

# Constante: duración de un sol marciano en días terrestres
SOL_MARC = 1.02749125;

class StarDates:
    def __init__(self, fecha: date):
        self.fecha = fecha;
        self.inicio_sol = date(2021, 4, 19);
        self.base_stardate = 2323;

    def terran_date(self) -> str:
        return self.fecha.strftime('%Y.%m.%d');

    def terran_sol(self) -> int:
        return (self.fecha - self.inicio_sol).days;

    def martian_sol(self) -> int:
        dias_terrestres = self.terran_sol();
        return int(dias_terrestres / SOL_MARC);

    def stardate(self) -> float:
        year = self.fecha.year;
        day_of_year = (self.fecha - date(year, 1, 1)).days + 1;
        is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0);
        total_days = 366 if is_leap else 365;
        return round(1000 * (year - self.base_stardate) + (day_of_year / total_days) * 1000, 1);

    def bitacora(self, titulo: str = 'Registro de Bitácora Estelar') -> str:
        barra = '=' * (len(titulo) + 8);
        return (
            f"=== {titulo} ===\n"
            f"📅 Fecha terrestre: {self.terran_date()}\n"
            f"🪐 Terran Sol: {self.terran_sol()}\n"
            f"🚀 Martian Sol: {self.martian_sol()}\n"
            f"🌌 Stardate: {self.stardate()}\n"
            f"{barra}\n"
        );

# Información para instalación como paquete
__version__ = '0.7.3';
__author__ = 'William Martinez Bas';
__email__ = 'metfar@gmail.com';
__license__ = 'MIT';
__description__ = 'Conversor y formateador de fechas terrestres, marcianas y stardates estilo Star Trek';

def main():
        print(StarDates.stardate(float(sys.argv[1:])));
        sys.exit(0);

if __name__ == '__main__':
    main();
