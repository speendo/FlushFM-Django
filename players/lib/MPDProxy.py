import mpd


class MPDProxy:
	def __init__(self, host="localhost", port=6600, timeout=10):
		self.client = mpd.MPDClient()
		self.host = host
		self.port = port

		self.client.timeout = timeout
		self.connect(host, port)

	def __getattr__(self, name):
		return self._call_with_reconnect(getattr(self.client, name))

	def connect(self, host, port):
		self.client.connect(host, port)

	def _call_with_reconnect(self, func):
		def wrapper(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			except mpd.ConnectionError:
				self.connect(self.host, self.port)
				return func(*args, **kwargs)
		return wrapper

mpd_proxy = MPDProxy()
