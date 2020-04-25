# -*- coding: UTF-8 -*-
import configparser
import os


class reviewconfig:
    def __init__(self):
        self.inidocument = configparser.ConfigParser()
        self.writedocumet = configparser.RawConfigParser()

    def learnreview(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        inipath = os.path.join(path, 'abc.ini')
        return inipath

    def readini(self, path):
        self.inidocument.read(path)


if __name__ == '__main__':
    a = reviewconfig()
    path1 = a.learnreview()
    print(path1)
    a.readini(path1)
    print(a.inidocument.get("LANG", "language"))

    a.inidocument.set("LANG", "home_dir1", "/Userss")
    a.inidocument.add_section("section1")
    with open(path1, 'wb') as f:
        a.writedocumet.write(f)
