import sys
import os
import yaml
import re
from . import utils
from .marker import Marker
from .templater import Templater
from .configurator import Configurator
from .indexer import Indexer


class Builder:
    """Builds the directory to generate html files."""

    def __init__(self, ROOT_DIR_PATH):
        self.ROOT_DIR_PATH = os.path.abspath(ROOT_DIR_PATH)
        self.mrk = Marker()
        self.tmplt = Templater(self.ROOT_DIR_PATH)
        self.c = Configurator(self.ROOT_DIR_PATH)
        self.indx = Indexer(self.ROOT_DIR_PATH)
        self.nested_dir = self.indx.index_dir(self.ROOT_DIR_PATH)

    def build_dir(self, folder):
        folder_path = os.path.abspath(os.path.join(self.ROOT_DIR_PATH, folder))
        print('Building folder: ' + folder_path)
        for root, dirs, files in os.walk(folder_path):
            conf = self.c.get_conf(root)
            default_layout = self.c.get_val(root, 'layout')
            for f in files:
                # Is the post a containment inside the folder
                # i.e. same name as parent folder or not
                post_folder = False
                # only supports .md files atm
                if os.path.splitext(f)[1] == '.md':
                    # print('Considering: ' + f)
                    if os.path.splitext(f)[0] == os.path.basename(root):
                        post_folder = True
                    in_file = os.path.abspath(os.path.join(root, f))
                    with open(in_file, 'r', encoding='utf-8') as fp:
                        text = fp.read()
                    try:
                        content, metadata = self.mrk.to_html(text)
                    except:
                        print("Skipping file: " + in_file + " ; Metadata invalid.")
                        continue
                    fconf = conf.copy()
                    par_tree = self.get_parent_tree(root, post_folder=post_folder)
                    fconf['tree'] = par_tree
                    # print(par_tree)
                    fconf.update(metadata)
                    layout = fconf.get('layout', default_layout)
                    out_file = os.path.abspath(
                                os.path.join(root, \
                                'index.html' if post_folder else os.path.splitext(f)[0] + '.html'))
                    with open(out_file, 'w', encoding='utf-8', errors='replace') as fp:
                        fp.write(self.tmplt.render(content, layout, fconf))
                    # print('File written: ' + out_file)

    def build_index(self, folder):
        folder_path = os.path.abspath(os.path.join(self.ROOT_DIR_PATH, folder))
        # if consequitive directory, file.md does not exists
        #   list the folder name
        # else
        #   list the file title and date
        default_layout = 'index.html'
        folder = folder_path.rstrip(os.sep)
        start = folder.rfind(os.sep) + 1
        for root, dirs, files in os.walk(folder_path):
            conf = self.c.get_conf(root)
            index = {'posts': [], 'collections': []}
            dir_post = os.path.basename(root) + '.md'
            if 'index.md' in files or dir_post in files:
                print("Skipping index generation for post: {}".format(root))
                continue
            folders = root[start:].split(os.sep)
            parent = self.nested_dir
            for fold in folders[:-1]:
                parent = parent.get(fold)
            parent = parent[folders[-1]]
            # Find the standalone .md posts
            for f in files:
                if os.path.splitext(f)[1] == '.md' and parent[f]:
                    post = parent[f]
                    if not post.get('title', None) or not post.get('date', None):
                        continue
                    post['slug'] = os.path.splitext(f)[0]
                    index['posts'].append(post)
            # Find bulkier notes and collections
            for d in dirs:
                post = None
                try:
                    post = parent[d].get(d + '.md')
                except KeyError:
                    pass
                if post:
                    # It's a single post
                    # print('Found a post: ' + post['title'])
                    if not post.get('title', None) or not post.get('date', None):
                        continue
                    try:
                        if post['title'].startswith('"') and post['title'].endswith('"'):
                            post['title'] = post['title'][1:-1]
                    except AttributeError:
                        post['title'] = str(post['title'])
                    post['slug'] = d
                    index['posts'].append(post)
                elif not d.startswith('_') or d != 'res':
                    # It's a collection of posts
                    # print('Found a collection: ' + d)
                    index['collections'].append({'title': d, 'slug': d})
            if index['posts'] or index['collections']:
                # print(root, utils.sort_list_dict(index['posts']))
                out_file = os.path.abspath(os.path.join(root, 'index.html'))
                aconf = {}
                aconf.update(conf)
                aconf.update({'posts': utils.sort_list_dict(index['posts']), 'collections': index['collections']})
                with open(out_file, 'w', encoding='utf-8', errors='replace') as fp:
                    fp.write(self.tmplt.render('', 'index', aconf))
                # print('Index written: ' + out_file)
        return index

    def get_parent_tree(self, fn, post_folder=False):
        fn = os.path.abspath(fn)
        parfn = os.path.join(fn, os.pardir) if post_folder else os.path.dirname(fn)
        flist = os.listdir(parfn)
        reg = re.compile('.*\.md$')

        startpath = os.path.relpath(
                parfn,
                os.path.join(self.ROOT_DIR_PATH, os.pardir))

        par_tree = {'posts': [], 'collections': []}
        for f in flist:
            if reg.match(f) or f == 'res' or f.startswith('.') or f.startswith('_'):
                continue
            elif os.path.isdir(f):
                par_tree['collections'].append(os.path.join(startpath, f))
            else:
                par_tree['posts'].append(os.path.join(startpath, f))

        return par_tree


if __name__ == '__main__':
    folder = 'Aphrodite'
    Builder('./personalBlog').build_dir(folder)
    Builder('./personalBlog').build_index(folder)
