#!/usr/bin/python3

import tools as tools
import os, re, threading, math, requests, click, time
from tqdm import tqdm


class tachydownload():
    global text
    text = tools.textEffects()

    def __consoleMsg(self, type):
        if type=="header":
            tools.printText("Tachyon", asciiArt=True)
            tools.printText(text.formatText("BOLD", "\nThe faster than light media downloader"))
        elif type=="completion":
            tools.printText(text.formatText("BOLD", "\nSuccess! 🎉 🎉 🎉\nFile located at: ~/Desktop/" + filename))
        elif type=="sysfail":
            tools.printText(text.formatText("BOLD", "One of the modules has not been imported\nEnsure the following modules are installed:\nos, re, threading, math, requests, click, time"))

    def multithreader(self, url, name, size):
        with tqdm(total=10000, ascii=True, ncols=100) as progBar:
            for i in range(1000):
                time.sleep(0.0025)
                progBar.update(10)
        self.__consoleMsg("completion")

    def main(self, url, name, size):
        if tools.sysValidation:
            self.__consoleMsg("header")
            self.multithreader(url, name, size)
        else:
            __consoleMsg("sysfail")


@click.command()
@click.option("--name", "--n", help="The name which the downloaded file will be saved under.")
@click.argument("download_url", type=click.Path())
def executeDownload(name, download_url):
    """Tachyon — The faster than light media downloader

    (c) 2018 Akshat Bisht under the GNU GPL v3.0 license"""
    try:
        urlInfo = requests.head(download_url)
    except:
        print("URL is corrupt")
        return

    global filename
    global filesize
    if name:
        filename = name
    else:
        filename = download_url.split("/")[-1]
    filesize = int(urlInfo.headers["Content-Length"])

    run = tachydownload()
    run.main(download_url, filename, filesize)

if __name__ == '__main__':
    executeDownload()
