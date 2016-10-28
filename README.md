# dystic

Minimal static site generator specialized for blogging.

**NOTE**

* v0.X.X  
    - Supports a subset of functionality.  
* v1.X.X  
    - Will introduce major changes, mainly to the structure
      and index generation.  
    - Read [development_references-v1](https://github.com/oxalorg/dystic/blob/master/development_reference-v1.md) for changes is dystic-v1.

## Quickstart

**Installation**:

```
pip3 install dystic
```

*Currently tested on Ubuntu 14.04, 16.04, and OSX.*

**Setup**:

```
mkdir my-notes
cd my-notes

```



## Usage

```
dystic -r <root folder of your blog> -b <the folder you want to build relative to root>
```

**Examples:**

```
# Build entire root folder
dystic -r ~/my-blog -b .

# Builds a only dummy.com/blog
dystic -r ~/my-blog -b blog

# Builds only a specific post of a nested collection
dystic -r ~/my-blog -b o/reviews/food/dunkin-donuts/simply-potato
```

## Example

Example directory:

```
.
├── _config.yml
├── _includes
│   ├── analytics.html
│   ├── comments.html
│   └── svg-icons.html
├── _layouts
│   ├── aside.py
│   ├── base.html
│   ├── index.html
│   └── post.html
├── albums
│   ├── index.html
│   ├── my-birthday-adventures
│   │   ├── index.html
│   │   ├── my-birthday-adventures.md
│   │   ├── pic1.png
│   │   ├── pic2.png
│   │   ├── some_random_cake_slaughtering.mp4
│   │   └── zombies.png
│   └── rainy-drainy
│       ├── clouds.png
│       ├── floods.mp4
│       ├── index.html
│       ├── rainy-drainy.md
│       └── water.jpg
├── blog
│   ├── _config.yml
│   ├── mushroom-cheese-toast
│   │   ├── index.html
│   │   └── mushroom-cheese-toast.md
│   ├── my-first-post
│   │   ├── index.html
│   │   └── my-first-post.md
│   └── why-i-failed-at-blogging
│       ├── _config.yml
│       ├── index.html
│       └── why-i-failed-at-blogging.md
├── index.html
├── o
│   ├── index.html
│   ├── reviews
│   │   ├── food
│   │   │   ├── dunkin-donuts
│   │   │   │   ├── index.html
│   │   │   │   └── simply-potato
│   │   │   │       ├── index.html
│   │   │   │       └── simply-potato.md
│   │   │   └── index.html
│   │   └── index.html
└── recipes
    ├── index.html
    └── this-is-a-test
        ├── index.html
        └── this-is-a-test.md
```

This is a sample directory of how dystic looks. You
simply create the directory based on how you want to see
the URL. It will automatically parse all ".md" files
and add a "index.html" file in the same directory. To
understand the philosophy behind it please read the
[development_references](https://github.com/oxalorg/dystic/blob/master/development_reference.md).

**NOTE**: Read [development_references-v1](https://github.com/oxalorg/dystic/blob/master/development_reference-v1.md) for changes is
dystic-v1.

You can mention configuration options in `_config.yml` in any
post or collection, and it will be local to it. This leads to
nested overwrittable configurations.

## Contributors

- oxalorg - [https://oxal.org](https://oxal.org)

## License

MIT License

Copyright (c) 2016 Mitesh Shah
