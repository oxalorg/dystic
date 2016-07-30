import sys
import os
import yaml
from . import utils
from .marker import Marker
from .templater import Templater
from .configurator import Configurator
from .indexer import Indexer
from .config import ROOT_DIR_PATH


class Builder:
    """Builds the directory to generate html files."""

    def __init__(self):
        self.tmplt = Templater()
        self.mrk = Marker()
        self.c = Configurator()
        self.indx = Indexer()

    def build_dir(self, folder):
        folder_path = os.path.join(ROOT_DIR_PATH, folder)
        print('Building folder: ' + folder_path)
        conf = self.c.get_conf(folder_path)
        default_layout = self.c.get_val(folder_path, 'layout')
        for root, dirs, files in os.walk(folder_path):
            for f in files:
                # only supports .md files atm
                if os.path.splitext(f) == (os.path.basename(root), '.md'):
                    in_file = os.path.abspath(os.path.join(root, f))
                    with open(in_file, 'r') as fp:
                        text = fp.read()
                    content, metadata = self.mrk.to_html(text)
                    layout = metadata.get('layout', default_layout)
                    out_file = os.path.abspath(os.path.join(root,
                                                            'index.html'))
                    with open(out_file, 'w') as fp:
                        fp.write(self.tmplt.render(content, layout, metadata))
                    print('File written: ' + os.path.basename(root))

    def build_index(self, folder):
        from pprint import pprint
        folder_path = os.path.join(ROOT_DIR_PATH, folder)
        nested_dir = self.indx.index_dir(folder_path)
        # if consequitive directory, file.md does not exists
        #   list the folder name
        # else
        #   list the file title and date
        default_layout = 'index.html'
        folder = folder_path.rstrip(os.sep)
        start = folder.rfind(os.sep) + 1
        pprint(folder + '' + str(start))
        for root, dirs, files in os.walk(folder_path):
            index = {'posts': [], 'collections': []}
            folders = root[start:].split(os.sep)
            parent = nested_dir
            for fold in folders[:-1]:
                parent = parent.get(fold)
            parent = parent[folders[-1]]
            for d in dirs:
                post = None
                try:
                    post = parent[d].get(d + '.md')
                except KeyError:
                    pass
                if post:
                    # It's a single post
                    print('Found a post: ' + post['title'])
                    if post['title'].startswith('"') and post[
                            'title'].endswith('"'):
                        post['title'] = post['title'][1:-1]
                    post['slug'] = d
                    index['posts'].append(post)
                elif not d.startswith('_'):
                    # It's a collection of posts
                    print('Found a collection: ' + d)
                    index['collections'].append({'title': d, 'slug': d})
            if index['posts'] or index['collections']:
                # print(root, utils.sort_list_dict(index['posts']))
                out_file = os.path.abspath(os.path.join(root, 'index.html'))
                with open(out_file, 'w') as fp:
                    fp.write(self.tmplt.render(
                        '',
                        'index',
                        posts=utils.sort_list_dict(index['posts']),
                        collections=index['collections']))
                print('File written: ' + os.path.abspath(os.path.basename(
                    root)))
        return index


if __name__ == '__main__':
    folder = '.'
    Builder().build_dir(folder)
    Builder().build_index(folder)
