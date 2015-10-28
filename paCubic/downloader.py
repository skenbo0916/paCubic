from __future__ import unicode_literals
import youtube_dl
import sys


class Logger(object):

    def debug(self, msg):
        print("[debug]:\t" + msg)

    def warning(self, msg):
        print("[warning]:\t" + msg)

    def error(self, msg):
        print("[error]:\t" + msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def downloader(uri):
    print("down: " + uri )

    ydl_opts = {
        'postprocessors': [
        ],
        'logger': Logger(),
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([uri])
