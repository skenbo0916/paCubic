import AdvancedHTMLParser
import re
import json


class VideoUris:

    parsable_uri_list = [
        r".*videomega.*"
    ]

    def __init__(self, http_req, date):
        self.http_req = http_req
        self.date = date


    def fetch(self):
        html_raw = self.fetch_html_raw()

        return self.parse_html_raw(html_raw)


    def parse_html_raw(self, html_raw):
        uri_set = set()

        parser = AdvancedHTMLParser.AdvancedHTMLParser()
        parser.parseStr(html_raw)

        for script in parser.getElementsByTagName('script'):
            json_extractor = re.match(r"<script >var video = (.*);</script>", str(script))

            if json_extractor:
                uri_pack_raw = json.loads(json_extractor.group(1))

                for each_uri_data in uri_pack_raw:
                    for number in [1, 2]:
                        testing_uri = each_uri_data['src' + str(number)]
                        if self.is_parsable_uri(testing_uri):
                            uri_set.add(testing_uri)


        return uri_set


    def fetch_html_raw(self):
        return self.http_req.send(
            'get',
            {'d': self.date},
            None).text


    def is_parsable_uri(self, uri):
        for uri_regex in self.parsable_uri_list:
            return True if re.match(uri_regex, uri) else False
