from zipfile import ZipFile
from io import BytesIO

import requests


class SodraClient:
    salaries_url = 'http://sodra.is.lt/Failai/Vidurkiai.zip'

    def get_salaries(self):
        response = requests.get(self.salaries_url)
        if response.status_code == requests.codes.ok:
            file = ZipFile(BytesIO(response.content))
            return self._extract_zip(file)

    @staticmethod
    def _extract_zip(file):
        return {name: file.read(name) for name in file.namelist()}

