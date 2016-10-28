import sys
import os
import yaml
from . import main
from .marker import Marker
from .templater import Templater
from .configurator import Configurator


class Indexer:
    """Indexes the directory to generate list files."""

    def __init__(self, ROOT_DIR_PATH):
        self.mrk = Marker()
        self.ROOT_DIR_PATH = ROOT_DIR_PATH

    def index_dir(self, folder):
        """
        Creates a nested dictionary that represents the folder structure of folder.
        Also extracts meta data from all markdown posts and adds to the dictionary.
        """
        folder_path = folder
        print('Indexing folder: ' + folder_path)
        nested_dir = {}
        folder = folder_path.rstrip(os.sep)
        start = folder.rfind(os.sep) + 1
        for root, dirs, files in os.walk(folder):
            folders = root[start:].split(os.sep)
            # subdir = dict.fromkeys(files)
            subdir = {}
            for f in files:
                # Create an entry for every markdown file
                if os.path.splitext(f)[1] == '.md':
                    with open(os.path.abspath(os.path.join(root, f)), encoding='utf-8') as fp:
                        try:
                            _, meta = self.mrk.extract_meta(fp.read())
                        except:
                            print("Skipping indexing " + f +"; Could not parse metadata")
                            meta = {'title': f}
                            pass
                    # Value of the entry (the key) is it's metadata
                    subdir[f] = meta
            parent = nested_dir
            for fold in folders[:-1]:
                parent = parent.get(fold)
            # Attach the config of all children nodes onto the parent
            parent[folders[-1]] = subdir
        return nested_dir


if __name__ == '__main__':
    import pprint
    pb = os.path.join(os.getcwd(), 'personalBlog')
    bl = os.path.join(os.getcwd(), 'personalBlog', 'blog')
    pprint.pprint(Indexer(pb).index_dir(bl))
