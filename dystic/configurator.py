"""
manages _config.yml file in root folder.
"""
import os
import yaml


class Configurator:
    def __init__(self, ROOT_DIR_PATH):
        self.ROOT_DIR_PATH = ROOT_DIR_PATH
        self.conf = {}
        self.aconf = {}

    def get_conf(self, folder_path):
        print(folder_path)
        try:
            with open(os.path.abspath(os.path.join(folder_path,
                                                   '_config.yml'))) as fp:
                fconf = yaml.load(fp)
            self.conf[os.path.split(folder_path)[1]] = fconf
            for k in fconf:
                if k not in self.aconf:
                    self.aconf[k] = fconf[k]
        except FileNotFoundError:
            pass
        # recursively get conf for every folder until ROOT folder.
        if folder_path == self.ROOT_DIR_PATH:
            # can lead to problems if a folder named 'site' is present
            self.conf['site'] = self.conf.pop(os.path.split(
                self.ROOT_DIR_PATH)[1])
            return self.aconf
        else:
            # make sure that ROOT_DIR_PATH is set correctly
            return self.get_conf(os.path.abspath(os.path.join(folder_path,
                                                              os.pardir)))

    def get_val(self, folder_path, key):
        folder_path = os.path.abspath(folder_path)
        try:
            if folder_path == self.ROOT_DIR_PATH:
                return self.conf['site'][key]
            return self.conf[os.path.split(folder_path)[1]][key]
        except KeyError:
            if folder_path == self.ROOT_DIR_PATH:
                raise SystemExit('The variable {' + key +
                                 '} you\'re trying to access is not defined.')
            return self.get_val(
                os.path.abspath(os.path.join(folder_path, os.pardir)), key)
        except TypeError:
            raise SystemExit(
                'A base configuration file could not be found!\nMake sure _config.yml file is not empty in your root directory.')


if __name__ == '__main__':
    ROOT_DIR_PATH = os.path.join(os.getcwd(), 'personalBlog')
    c = Configurator(ROOT_DIR_PATH)
    # d = c.get_conf(os.path.join(ROOT_DIR_PATH, 'blog', 'june-15'))
    # e = c.get_val(os.path.join('personalBlog', 'blog', 'june-15'), 'layout')
    d = c.get_conf(os.path.join(ROOT_DIR_PATH, 'blog', 'experiments'))
    print(d)
    print(c.conf)
