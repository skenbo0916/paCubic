import multiprocessing
from paCubic.downloader import downloader


class FetchVideo:

    def __init__(self, video_uris):
        self.video_uris = video_uris

    def run(self):

        pool = multiprocessing.Pool()

        for uri in self.video_uris:
            pool.apply_async(downloader, args=(uri, ))

        pool.close()
        pool.join()
