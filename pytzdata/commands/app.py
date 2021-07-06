# -*- coding: utf-8 -*-

from cleo import Application

from .make import MakeCommand
from .zones import ZonesCommand

app = Application('pytxdata')

app.add(MakeCommand())
app.add(ZonesCommand())


if __name__ == '__main__':
    app.run()
