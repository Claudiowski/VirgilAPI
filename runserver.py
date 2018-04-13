# coding: utf8

from app import create_app


def runserver():
        
    app = create_app('production')
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    runserver()