import sys
import os
import yaml
import argparse


def cli():
    parser = argparse.ArgumentParser(
        description='Simple dynamically static blog generator.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b',
                        '--build',
                        dest='folder',
                        help="build the specified folder.",
                        required=True)
    parser.add_argument(
        '-r',
        '--root',
        dest='root',
        help="specify the root folder, defaults to current working directory.",
        default=os.getcwd())
    args = parser.parse_args()
    if args.folder:
        build(args.root, args.folder)
    else:
        raise SystemExit('Please specify a directory.')


def build(root, folder):
    from . import builder
    b = builder.Builder(root)
    b.build_dir(folder)
    b.build_index(folder)
    b.build_index(os.path.join(folder, os.pardir))


if __name__ == '__main__':
    cli()
