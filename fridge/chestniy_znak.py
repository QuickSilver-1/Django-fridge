
import requests, urllib

class Lib:
	def __init__(self):
		pass

	def _get(self, content, types):
		return requests.get(f"https://mobile.api.crpt.ru/mobile/check?code={content}&codeType={types}").json()

	def infoFromDataMatrix(self, xyematrix):
		return self._get(xyematrix, "datamatrix")

	def infoFromEAN13(self, ean13):
		return self._get(ean13, "ean13")
	def infoFromQr(self, qr):
		return self._get(qr, "qr")