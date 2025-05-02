#!/bin/bash
echo '🔎 Ejecutando tests con unittest...'
python3 test_stardates_unittest.py || exit 1
echo '✅ unittest finalizado con éxito'

echo '🔎 Ejecutando tests con pytest...'
pytest -v test_stardates_pytest.py || exit 1
echo '✅ pytest finalizado con éxito'
