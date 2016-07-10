from jinja2 import Environment, FileSystemLoader
import os
import main
import datetime
from collections import defaultdict

TEMPLATE_DIR = '_layouts'
TEMPLATE_DIR_PATH = os.path.abspath(os.path.join(main.config['ROOT_DIR_PATH'], TEMPLATE_DIR))

def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    value = datetime.datetime.strptime(value, '%Y-%m-%d')
    return value.strftime(format)


class Templater:
    def __init__(self):
        print(TEMPLATE_DIR_PATH)
        self.loader = FileSystemLoader(TEMPLATE_DIR_PATH)
        self.env = Environment(loader=self.loader)
        self.env.filters['datetimeformat'] = datetimeformat


    def render(self, text, tmplt, post=defaultdict(), site=defaultdict()):
        # the following line is ugly but works 99% of the time.
        tmplt = tmplt if tmplt.rsplit('.', 1)[1] == 'html' else tmplt + '.html'
        self.template = self.env.get_template(tmplt)
        return self.template.render(content=text, post=post, site=site)
