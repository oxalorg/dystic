import sys
import os
import yaml
import argparse

config = {
    'ROOT_DIR_PATH': os.path.abspath(os.path.dirname(sys.argv[1]))
}

def cli():
    parser = argparse.ArgumentParser(
    description='Simple dynamically static blog generator.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def main():
    with open('_config.yml', 'r') as f:
        config.update(yaml.load(f))
    # cli()


if __name__ == '__main__':
    main()
