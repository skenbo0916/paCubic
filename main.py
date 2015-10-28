import sys
import os
from paCubic.config import Config
from paCubic.video_uris import VideoUris
from paCubic.http_req import HttpReq
from paCubic.fetch_video import FetchVideo

def main():
    query_date = sys.argv[1]

    config = Config().get_config()
    http_req = HttpReq(config['end_point']['web_page'])

    video_uris = VideoUris(
        http_req,
        query_date).fetch()

    if video_uris:
        if not os.path.exists(query_date):
            os.mkdir(query_date)
        os.chdir(query_date)
        FetchVideo(video_uris).run()


if __name__ == '__main__':
    main()

