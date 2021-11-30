from base64 import b64encode, b64decode
from multiprocessing import Queue
from multiprocessing.queues import Empty
from threading import Thread
import logging
import pickle
import requests

from flask import Flask, request, jsonify

class Client:
    """Sets up a connection to a mixnet, receives and sends messages"""
    dummy_upload = {
        'index': 0,
        'data': None
    }
    dummy_download = 0

    def __init__(self, host):
        """Join a riffle group.

        Parameters
        ----------
        host: str
            Entrypoint of the mixnet

        """
        self.host = host
        self.download_requests = Queue()
        self.upload_requests = Queue()
        self.download_responses = Queue()
        if requests.get('http://' + host + '/login').status_code != 200:
            raise Exception('Failed to login')
        self.listen()

    def upload(self, data, index):
        """Send some data to the mixnet.

        Does not send automatically, but puts it in a queue
        to be sent on the next round

        Parameters
        ----------
        data: object
            Object that can be pickled
        index: int
            Index that identifies data

        """
        upload_data = {
            'index': str(index),
            'data': b64encode(pickle.dumps(data)).decode()
        }
        self.upload_requests.put(upload_data)

    def download(self, index):
        """Retrieve data from mixnet.

        Does not retrieve automatically, rather waits for
        the download stage

        Parameters
        ----------
        index: int
            Index of file to be retrieved

        """
        index = str(index)
        self.download_requests.put(index)
        last_download = self.download_responses.get()
        print(last_download)

        data = last_download.get(index)
        if data:
            data = pickle.loads(b64decode(data))
        return data

    def listen(self):
        """Thread that keeps connection alive"""
        app = Flask(__name__)
        log = logging.getLogger('werkzeug')
        log.disabled = True

        @app.route('/ask')
        def upload():
            try:
                upload = self.upload_requests.get_nowait()
            except Empty:
                upload = self.dummy_upload
            try:
                download = self.download_requests.get_nowait()
            except Empty:
                download = self.dummy_download

            data = {
                'upload': upload,
                'download': download
            }
            return jsonify(data)

        @app.route('/download', methods=['POST'])
        def download():
            data = request.json
            if data:
                self.download_responses.put(data)
            return jsonify(success=True)

        Thread(target=lambda: app.run(
            host='0.0.0.0',
            port=8081,
            debug=True,
            use_reloader=False
        )).start()
