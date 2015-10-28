import urllib
import requests


class HttpReq:

    def __init__(self, end_point):

        self.s = requests.Session()
        self.end_point = end_point
        self.cookie = None
        self.header = {
            'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) ' \
                'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                'Chrome/46.0.2490.71 Safari/537.36'
        }

        self.s.get(self.end_point)
        self.cookie = self.s.cookies

    def get(self, params = None, auth = None):

        if params:
            end_point = self.end_point + "?" + urllib.parse.urlencode(params)
        return self.s.get(
            end_point,
            headers = self.header,
            auth = auth,
            cookies = self.cookie)


    def post(self, params = None, auth = None):
        return requests.post(
            self.end_point,
            headers = self.header,
            auth = auth,
            cookies = self.cookie)


    def send(self, method, params=None, auth=None):
        return self.get(params, auth) if method == 'get' else self.post(param, auth)
