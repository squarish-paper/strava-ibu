virtualenv --python python3 env
source env/bin/activate

pip install flask
pip install flask-mysql
pip install requests

python app.py
