import main
import sys
import os
import yaml
from .marker import Marker
from .templater import Templater
from .configurator import Configurator
from .config import ROOT_DIR_PATH


class Indexer:
    """Indexes the directory to generate list files."""

    def __init__(self):
        self.tmplt = Templater()
        self.mrk = Marker()
        self.c = Configurator()

    # def index_dir(self, folder):
    #     folder_path = os.path.join(ROOT_DIR_PATH, folder)
    #     print('Indexing folder: ' + folder_path)
    #     for root, dirs, files in os.walk(folder_path):
    #         if os.path.basename(root) + '.md' not in files:
    #             # calculate index titles and dates
    #
    #             layout = 'index.html'
    #             out_file = os.path.abspath(os.path.join(root, 'index.html'))
    #             with open(out_file, 'w') as fp:
    #                 fp.write(self.tmplt.render('', layout, metadata))
    #                 print('Index written: ' + os.path.basename(root))
    #
    #                 in_file = os.path.abspath(os.path.join(root, f))
    #                 with open(in_file, 'r') as fp:
    #                     text = fp.read()
    #                 content, metadata = self.mrk.to_html(text)
    #                 layout = metadata.get('layout', default_layout)

    def index_dir(self, folder):
        """
        Creates a nested dictionary that represents the folder structure of folder.
        Also extracts meta data from all markdown posts and adds to the dictionary.
        """
        folder_path = os.path.join(ROOT_DIR_PATH, folder)
        print('Indexing folder: ' + folder_path)
        nested_dir = {}
        folder = folder.rstrip(os.sep)
        start = folder.rfind(os.sep) + 1
        for root, dirs, files in os.walk(folder):
            folders = root[start:].split(os.sep)
            # subdir = dict.fromkeys(files)
            subdir = {}
            for f in files:
                if f == os.path.basename(root) + '.md':
                    with open(os.path.abspath(os.path.join(root, f))) as fp:
                        _, meta = self.mrk.extract_meta(fp.read())
                    subdir[f] = meta
            parent = nested_dir
            for fold in folders[:-1]:
                parent = parent.get(fold)
            parent[folders[-1]] = subdir
        return nested_dir


if __name__ == '__main__':
    import pprint
    pprint.pprint(Indexer().index_dir('.'))
