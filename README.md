# dystic

Intuitive static site generator. What you see is what you get.

No specific `content`, `media`, or `static` folders. Just take
any existing directory on your system and turn it into a static
web site.

So in the following directory:

```
website ➴ tree .
.
├── notes
│   └── my-name-is-john-cena.md
├── recipies
│   ├── my-top-3-vegan-snacks.md
│   └── yummy-veg-wraps.md
└── reviews
    ├── hardware
    │   └── mac-book-air-13-review.md
    ├── software
    │   └── dystic-static-generator-is-awesome.md
    └── triple-cheese-pizza-420.md
```

The *page* for yummy veg wrap recipies will get built at 
`www.website.com/recipies/yummy-veg-wraps`

The *page* for the mac book review will be viewable at
`www.website.com/reviews/hardware/mac-book-air-13-review`

and finally the page for the review of that delicious tripple
cheese pizza I had last week will be generated at:
`www.website.com/reviews/triple-cheese-pizza-420`

Configurations for ***any*** part of the website can be
changed by adding a `_config.yml` in the respective folders.

So I could add `_config.yml` with `layout: review` inside the
`website/reviews` directory, and then add another `_config.yml`
with `layout: fancy-reviews` inside `webiste/reviews/hardware`
to overwrite the layout values for all content under hardware.

This recursive configuration makes it very easy to maintain
certain parts of your website. Giving each part a different
look, feel, and configuration.

Some uses of `dystic`:

- ANY static website.
- Notes. I replaced *EverNote* with *dystic* on my `~/notes`
  directory
- Blogs. Works amazingly for blogs since it auto indexes
  a collection of posts.

Read more about the *philosophy*: [development_references-v1](https://github.com/oxalorg/dystic/blob/master/development_reference-v1.md)

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

Example file system structure of my personal blog:

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
