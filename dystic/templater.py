from jinja2 import Environment, FileSystemLoader
import os
import datetime
from collections import defaultdict
from . import config


def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    # value = datetime.datetime.strptime(value, '%Y-%m-%d')
    return value.strftime(format)


class Templater:
    TEMPLATE_DIR = '_layouts'

    def __init__(self, ROOT_DIR_PATH):
        self.ROOT_DIR_PATH = ROOT_DIR_PATH
        self.TEMPLATE_DIR_PATH = os.path.abspath(os.path.join(ROOT_DIR_PATH, self.TEMPLATE_DIR))
        self.loader = FileSystemLoader(self.TEMPLATE_DIR_PATH)
        self.env = Environment(loader=self.loader)
        self.env.filters['datetimeformat'] = datetimeformat

    def render(self, text, tmplt, post=defaultdict(), site=defaultdict(), **kwargs):
        # the following line is ugly but works 99% of the time.
        try:
            tmplt = tmplt if tmplt.rsplit('.', 1)[1] == 'html' else tmplt + '.html'
        except IndexError:
            tmplt = tmplt + '.html'
        self.template = self.env.get_template(tmplt)
        return self.template.render(content=text, post=post, site=site, **kwargs)
