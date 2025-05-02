#!/bin/bash
# Desde Stardate
python star_dates_module.py --stardate 2398.3

# Desde fecha con hora (espacio o T)
python star_dates_module.py --date "2006-07-24 03:50:24"
python star_dates_module.py --date "2006-07-24T03:50:24"

# Desde fecha sin hora (se asume 00:00:00)
python star_dates_module.py --date 2006-07-24

