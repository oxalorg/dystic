import main
import sys
import os
import yaml
from marker import Marker
from templater import Templater
ROOT_DIR = main.config['ROOT_DIR_PATH']

class Builder:
    """Builds the directory to generate html files."""

    def __init__(self):
        self.tmplt = Templater()
        self.mrk = Marker()

    def build_dir(self, folder):
        folder_path = os.path.join(ROOT_DIR, folder)
        try:
            default_layout = None
            with open(os.path.join(folder_path, '_config.yml')) as fp:
                fconf = yaml.load(fp)
            default_layout = fconf['layout']
        except FileNotFoundError:
            pass
        if not default_layout:
            default_layout = 'post.html'
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
                    print(out_file)
                    with open(out_file, 'w') as fp:
                        fp.write(self.tmplt.render(content, layout, metadata))


if __name__ == '__main__':
    folder = 'blog'
    Builder().build_dir(folder)
