import sys
import os
from .indexer import Indexer

S_HEADER = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

S_PAGE = """\
<url>
    <loc>{0}</loc>
    <lastmod>{1}</lastmod>
</url>
"""

S_DIR = """\
<url>
    <loc>{0}</loc>
</url>
"""

S_FOOTER = """\
</urlset>
"""

class Sitemap:
    def __init__(self, ROOT_DIR_PATH):
        self.pages = []
        self.dirs = []
        self.ROOT_DIR_PATH = ROOT_DIR_PATH
        self.indxr = Indexer(self.ROOT_DIR_PATH)

    def generate(self):
        self._gather()
        self._assemble()
        self._write()

    def _gather(self):
        """
        Gather all the paths from the root folder.
        All content/pages/posts are added to `self.pages`
        All directories/collection are added to `self.dirs`
        """
        self.index = self.indxr.index_dir(self.ROOT_DIR_PATH)
        folder = self.ROOT_DIR_PATH.rstrip(os.sep)
        start = folder.rfind(os.sep) + 1
        for root, dirs, files in os.walk(self.ROOT_DIR_PATH):
            folders = root[start:].split(os.sep)
            if not dirs and not files:
                # The directory is completely empty
                # hence not included in sitemap
                continue

            meta = {}
            # print(folders)
            for fold in folders[:-1]:
                meta = self.index.get(fold)

            root_name = os.path.basename(root)
            if root_name + '.md' in files:
                # This is a bulky post
                try:
                    cdate = meta[root_name + '.md']['date']
                    self.pages.append((root, cdate))
                except KeyError:
                    self.dirs.append(root)
                except:
                    print('Error in folder: ' + root)
                    sys.exc_info()[0]

            for f in files:
                if f.endswith('.md'):
                    fpath = os.path.join(root, f)
                    try:
                        self.pages.append((fpath, meta[f].get('date')))
                        print(meta[f])
                    except KeyError:
                        self.dirs.append(fpath)
                    except:
                        print('Error in file: ' + fpath)
                        sys.exc_info()[0]

    def _assemble(self):
        print(self.pages)
        print(self.dirs)

    def _write(self):
        pass


if __name__ == '__main__':
    s = Sitemap('/notes/')
    s.generate()
