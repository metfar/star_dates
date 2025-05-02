# StarDates

A date converter to/from *Stardates* (inspired by Star Trek), using an absolute linear time scale starting from the year 2000.

## 🚀 Description

This module converts terrestrial datetime (including hours, minutes, and seconds) to a continuous *Stardate* scale, based on absolute elapsed time since January 1, 2000. It also allows conversion back from stardates to standard datetime.

- Absolute linear time scale
- Supports full datetime precision
- Command-line interface and programmatic API
- MIT license

## 📦 Installation

```bash
pip install .
```

or for development:

```bash
python3 -m build
pip install dist/*.whl
```

## 🛠 Usage

### From the command line

```bash
# Convert Stardate to datetime
stardate --stardate 2398.3

# Convert datetime to Stardate
stardate --date "2006-07-24 03:50:24"

# Default: show current Stardate
stardate
```

You can also run the module directly:

```bash
python star_dates_module.py --stardate 2398.3
python star_dates_module.py --date "2006-07-24T03:50:24"
```

### 🧪 Example output

```
=== Stardate system time ===
📅 Terran datetime: 2025.05.02 21:43:00
🌌 Stardate: 9368.35
=================================
```

## 🧮 Formula used

```text
Stardate = (Year - 2000) × 365.25
         + (Month - 1) × 30.44
         + Day
         + Hour / 24
         + Minute / 1440
         + Second / 86400
```

## 🧑‍💻 Development & Tests

Run all tests:

```bash
./test.sh
```

Or individually:

```bash
python test_stardates_unittest.py
pytest test_stardates_pytest.py
```

## 📜 License

MIT © William Martinez Bas
