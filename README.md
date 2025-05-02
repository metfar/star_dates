# StarDates

Conversor de fechas y horas a Stardates (estilo Star Trek), usando una escala absoluta desde el año 2000.

## 🚀 Descripción

Este módulo permite convertir fechas terrestres con hora (en formato `YYYY-MM-DD HH:MM:SS`) a una escala continua de "Stardate" basada en días desde el año 2000. También permite la conversión inversa.

- Escala continua y absoluta
- Soporte para horas, minutos y segundos
- Línea de comandos amigable
- Licencia MIT

## 📦 Instalación

```bash
pip install .
```

## 🛠 Uso desde línea de comandos

```bash
# Convertir Stardate a fecha
python star_dates_module.py --stardate 2398.3

# Convertir fecha a Stardate
python star_dates_module.py --date "2006-07-24 03:50:24"
```

También podés usarlo como comando:

```bash
stardate --date "2006-07-24T03:50:24"
stardate --stardate 2398.3
```

## 🧮 Fórmula usada

```text
Stardate = (Año - 2000) × 365.25
         + (Mes - 1) × 30.44
         + Día
         + Hora / 24
         + Minuto / 1440
         + Segundo / 86400
```

## 📜 Licencia

MIT © William Martinez Bas
