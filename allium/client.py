class Client:
    """Sets up a connection to a mixnet, receives and sends messages"""
    def __init__(self, host):
        """Join a riffle group.

        Parameters
        ----------
        host: str
            Entrypoint of the mixnet

        """

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

    def download(self, index):
        """Retrieve data from mixnet.

        Does not retrieve automatically, rather waits for
        the download stage

        Parameters
        ----------
        index: int
            Index of file to be retrieved

        """

    def listen(self):
        """Thread that keeps connection alive"""
