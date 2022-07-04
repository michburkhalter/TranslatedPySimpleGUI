@ECHO OFF

ECHO Creating and Updating Translations
ECHO Initiating directory locale if necessary
if not exist locale\ (
    mkdir locale\
)

ECHO Initiating base translation file
venv\Scripts\pybabel extract . -o locale/base.pot

if not exist locale\de\ (
  echo Init Language DE
  venv\Scripts\pybabel init -l de -i locale/base.pot -d locale
)
if not exist locale\en\ (
  echo Init Language EN
  venv\Scripts\pybabel init -l en -i locale/base.pot -d locale
)

ECHO Create and compile translations
venv\Scripts\pybabel update -i locale/base.pot -d locale/
:: Between these 2 steps you have to add the translations manually to e.g. locale/de/messages.po
venv\Scripts\pybabel compile -d locale
