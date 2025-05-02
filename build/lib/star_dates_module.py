import sys;
import argparse;
from datetime import datetime, timedelta;
from decimal import Decimal, getcontext, ROUND_DOWN;

# Constants
BASE_YEAR = 2000;
DAYS_PER_YEAR = 365.25;
DAYS_PER_MONTH = 30.44;

class StarDates:
    def __init__(self, fecha: datetime):
        self.fecha = fecha;

    def terran_date(self) -> str:
        return self.fecha.strftime('%Y.%m.%d %H:%M:%S');

    def stardate(self) -> float:
        getcontext().prec = 9;
        y, m, d = self.fecha.year, self.fecha.month, self.fecha.day;
        h, mi, s = self.fecha.hour, self.fecha.minute, self.fecha.second;

        sd = Decimal(y - BASE_YEAR) * Decimal(DAYS_PER_YEAR);
        sd += Decimal(m - 1) * Decimal(DAYS_PER_MONTH);
        sd += Decimal(d);
        sd += Decimal(h) / Decimal(24);
        sd += Decimal(mi) / Decimal(1440);
        sd += Decimal(s) / Decimal(86400);

        return float(sd.quantize(Decimal("0.01"), rounding=ROUND_DOWN));

    def log(self, titulo: str = 'Star Log') -> str:
        barra = '=' * (len(titulo) + 8);
        return (
            f"=== {titulo} ===\n"
            f"📅 Terran Time: {self.terran_date()}\n"
            f"🌌    Stardate: {self.stardate()}\n"
            f"{barra}\n"
        );

    @staticmethod
    def from_stardate(stardate: float) -> 'StarDates':
        getcontext().prec = 9;
        sd = Decimal(str(stardate));

        years = int(sd // Decimal(DAYS_PER_YEAR));
        rem_days = sd % Decimal(DAYS_PER_YEAR);
        year = BASE_YEAR + years;

        months = int(rem_days // Decimal(DAYS_PER_MONTH));
        rem_days -= Decimal(months) * Decimal(DAYS_PER_MONTH);
        month = months + 1;

        day = int(rem_days);
        rem = rem_days - Decimal(day);

        hour = int(rem * Decimal(24));
        rem -= Decimal(hour) / Decimal(24);

        minute = int(rem * Decimal(1440));
        rem -= Decimal(minute) / Decimal(1440);

        second = int(rem * Decimal(86400));

        fecha = datetime(year, month, day, hour, minute, second);
        return StarDates(fecha);

def main():
    parser = argparse.ArgumentParser(description='Star Trek style Stardates converter from 2000 with time.');
    parser.add_argument('--version', action='version', version='StarDates 1.0.1');

    group = parser.add_mutually_exclusive_group();
    group.add_argument('--stardate', type=float, help='Stardate to convert into Terran Time');
    group.add_argument('--date', type=str, help='Earth time format YYYY-MM-DD[THH:MM:SS] or "YYYY-MM-DD HH:MM:SS"');

    args = parser.parse_args();

    if args.stardate is not None:
        sd = StarDates.from_stardate(args.stardate);
        print(sd.bitacora(f"Convert from Stardate {args.stardate}"));
    elif args.date is not None:
        try:
            try:
                fecha = datetime.fromisoformat(args.date);
            except ValueError:
                try:
                    fecha = datetime.strptime(args.date, "%Y-%m-%d %H:%M:%S");
                except ValueError:
                    fecha = datetime.strptime(args.date, "%Y-%m-%d");
            sd = StarDates(fecha);
            print(sd.bitacora(f"Convert from Terran Time {args.date}"));
        except Exception as e:
            print(f"Error interpreting time: {e}");
            sys.exit(1);
    else:
        # 🚀 Sin argumentos: usar fecha y hora actual
        now = datetime.now(); 
        sd = StarDates(now);
        print(sd.bitacora("Current Stardate (system-based)"));

if __name__ == '__main__':
    main();
