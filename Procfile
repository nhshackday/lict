web: python lict/manage.py run_gunicorn -b "0.0.0.0:$PORT" -c gunicorn_conf.py
worker: python lict/manage.py celeryd -l info
