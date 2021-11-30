from json import JSONDecodeError
from time import sleep
from threading import Thread
import logging
import requests

from flask import Flask, request, jsonify

class Server:
    """Server (no mixnet)"""
    def __init__(self):
        """Sets up server"""
        self.clients = []
        self.database = {}
        Thread(target=lambda: self.round()).start()
        self.listen_login()

    def round(self):
        """Run upload and download stages"""
        while True:
            files_to_send = {}
            for c in self.clients:
                try:
                    c_data = requests.get('http://' + c + '/ask')
                    c_data = c_data.json()
                    upload = c_data.get('upload')
                    download = c_data.get('download')
                except JSONDecodeError:
                    upload = None
                    download = None
                if upload:
                    self.database.update({upload['index']: upload['data']})
                if download:
                    files_to_send[download] = self.database.get(download)
            for c in self.clients:
                r = requests.post('http://' + c + '/download', json=files_to_send)
            sleep(5)

    def listen_login(self):
        """Handles login requests"""
        app = Flask(__name__)

        @app.route('/login')
        def listen_login():
            self.clients.append(f'{request.environ["REMOTE_ADDR"]}:8081')
            return jsonify(success=True)

        Thread(target=lambda: app.run(
            host='0.0.0.0',
            port=8080,
            debug=True,
            use_reloader=False
        )).start()

if __name__ == '__main__':
    Server()
