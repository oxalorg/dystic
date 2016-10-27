# dystic v1

Dystic is currently rollin in v0.x.x, which is soon
about to change. I've thought about some major changes
I want to introduce for v1.

## Why?

When I first built dystic, I had a very specific task
which I wanted to accomplish: Blogging from the
filesystem, which is intuitive on a webserver. My needs
since then have changed quite a bit. I've realised that
the current structuring layout used by dystic is rather
unintuitive (even though it's way more intuitive than
almost any other static engine I've used).

### Current structuing

Right now there are two main classifications:

* Posts
    * a post is a self contained folder
    * it includes the markdown source
    * it includes all the media assets
* Collections
    * It's a group of posts under the same directory

Something liks this:

```
.
├── albums
│   ├── _config.yml
│   └── my-birthday-adventures
│       ├── my-birthday-adventures.md
│       ├── pic1.png
│       ├── pic2.png
│       ├── some_random_cake_slaughtering.mp4
│       └── zombies.png
├── blog
│   ├── my-first-post
│   │   └── my-first-post.md
│   └── my-new-blogging-system
│       ├── my-new-blogging-system.md
│       └── screenshots.png
├── recipes
│   ├── vegan
│   │   ├── vegan-chipotle
│   │       ├── ...
│   │       └── ...
│   │   └── yummy-vegan-wraps
│   └── ...
└── _site
```

Here `albums`, `blog`, `recipes`, and `vegan` are collections.
Rest all are posts. We can see that `vegan` is a nested
collection.

### Classification

I feel that this is a much intuitive structure because we are
treating the filesystem as a first class citizen. We do this
my making distinction between posts and collections as follows:

* If a folder (lets say `veg-recipes`) has a file called
  `veg-recipes.md` then it's a **post**.
* If a folder doesn't have any file with the extenstion `.md`
  then it is a **collection**.

Now I need something more powerful.

## What?

So what changes have I thought?

First. Let's make our *posts* a little less bulkier:

* Any file ending in a set of pre-defined extenstions (currently
  only `.md`) is a post in itself.
* If a folder has a file with the same name then also it's a
  post (same as dystic-v0)
* **EXCEPTION**: `index.md` is not a post, it's an index.

Now lets make our *collections* more powerful:

* Any folder with an `index.md` file is a collection.
* Any folder without any file in our extenstion list
  is also a collection (same as dystic v0)
* If a folder doesn't contain a file with the same name 
  then also it's a collection. 

---

That's about it I guess. One more change I wish to add would be
to build the site inside `_site` directory. Right now (in
dysticv0) it gets written in-place.

Contact me at [rogue@oxal.org](mailto:rogueoxal.org).


