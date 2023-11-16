echo "BUILD START"
python3.9 -m pip install -r requirements.txt

# Ajout de cette ligne pour créer le répertoire staticfiles s'il n'existe pas
mkdir -p staticfiles

python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
