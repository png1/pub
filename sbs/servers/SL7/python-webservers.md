## Gunicorn

- ``sudo pip install gunicorn``  # **install** Gunicorn

```
Collecting gunicorn
    100% || 122kB 2.2MB/s 
Installing collected packages: gunicorn
Successfully installed gunicorn-19.6.0
```

## Flask

- ``sudo pip install flask``  # **install** Flask

```
Installing collected packages: click, MarkupSafe, Jinja2, Werkzeug, itsdangerous, flask
  Running setup.py install for click ... done
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for itsdangerous ... done
```

----

## Flask - TEST

- ``flask_test.py``

```python
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04

from flask import Flask
application = Flask(__name__)

@application.route("/flask_test")
def hello():
  return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
  application.run(host='0.0.0.0')
```

- Run **gunicorn** (``--bind localhost:8550``)

```bash
gunicorn -w 3 --bind localhost:8550 flask_test:application
```

- Check with **wget**: ``http://localhost:8550/flask_test``

```bash
wget http://localhost:8550/flask_test -O - | less
```

- [ ] Need to modify 'firewall' (re: ports) for httpS ??

```bash
# Run GUNICORN
gunicorn -w 3 --certfile=/etc/pki/tls/certs/___.crt --keyfile=/etc/pki/tls/private/___key --bind sec___ flask_test:application

# CHECK
wget --no-check-certificate https://sec___:8000/flask_test -O - | less
```
