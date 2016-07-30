import sys
import os
import yaml
import argparse


def build(folder):
    from . import builder
    b = builder.Builder()
    b.build_dir(folder)
    b.build_index(folder)
    b.build_index(os.path.join(folder, os.pardir))


def cli():
    parser = argparse.ArgumentParser(
        description='Simple dynamically static blog generator.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b',
                        '--build',
                        dest='folder',
                        help="build the specified folder.",
                        required=True)
    args = parser.parse_args()
    if args.folder:
        build(args.folder)
    else:
        raise SystemExit('Please specify a directory.')


def main():
    # with open('_config.yml', 'r') as f:
    #     config.update(yaml.load(f))
    cli()


if __name__ == '__main__':
    main()
