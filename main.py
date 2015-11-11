import sys
import os
from paCubic.config import Config
from paCubic.video_uris import VideoUris
from paCubic.http_req import HttpReq
from paCubic.fetch_video import FetchVideo

def main():
    query_date = sys.argv[1]

    config = Config().get_config()
    save_folder = config['path']['save_folder'] + query_date

    http_req = HttpReq(config['end_point']['web_page'])

    video_uris = VideoUris(
        http_req,
        query_date).fetch()

    if video_uris:
        if not os.path.exists(save_folder):
            os.mkdir(save_folder)
            os.chdir(save_folder)
        os.chdir(save_folder)
        FetchVideo(video_uris).run()


if __name__ == '__main__':
    main()

