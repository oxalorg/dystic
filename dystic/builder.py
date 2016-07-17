import main
import sys
import os
import yaml
from marker import Marker
from templater import Templater
from configurator import Configurator
ROOT_DIR = main.config['ROOT_DIR_PATH']

class Builder:
    """Builds the directory to generate html files."""

    def __init__(self):
        self.tmplt = Templater()
        self.mrk = Marker()
        self.c = Configurator()

    def build_dir(self, folder):
        folder_path = os.path.join(ROOT_DIR, folder)
        conf = self.c.get_conf(folder_path)
        default_layout = self.c.get_val(folder_path, 'layout')
        return
        for root, dirs, files in os.walk(folder_path):
            for f in files:
                # only supports .md files atm
                if os.path.splitext(f) == (os.path.basename(root), '.md'):
                    in_file = os.path.abspath(os.path.join(root, f))
                    with open(in_file, 'r') as fp:
                        text = fp.read()
                    content, metadata = self.mrk.to_html(text)
                    layout = metadata.get('layout', default_layout)
                    out_file = os.path.abspath(os.path.join(root, 'index.html'))
                    with open(out_file, 'w') as fp:
                        fp.write(self.tmplt.render(content, layout, metadata))


if __name__ == '__main__':
    folder = 'blog/june-15'
    Builder().build_dir(folder)
