This is what I have in mind at the moment.

Firstly, I need a static *blog* generator for personal use. I want to build it from ground like a dynamic website. Here the server filesystem becomes my database.

Most of the current static generators complicate the code to include caching and incremenatal builds, or simply rebuild the website every time something is changed. I feel this is redundancy in it's purest form, but that happens in software, specially when it's not targeted at one specific functionality.

I aim to remove this redundancy by making a blog generator, not a site generator.

Blog is nothing but a web log. Every entry in a log usually has a unique way of differentiating itself. It's, almost always, *time* of posting in a blog. Most of the time the entries can exist as a sole entity without any requirements.

So this minimalBlog exploits this to create, update, and delete only specific blog posts at a time. We provide a libary api for this such that it can easily be coupled with Flask and be deployed as a dynamically static blog, i.e. having benefits of both dynamic blogs and static blogs.

The current structuring of the blog I have envisioned is something like this:
```
.
├── _config.yml
├── _layouts
│   ├── base.html
│   └── post.html
└── _site
```

`_layouts` obviously containts the html layouts needed for the blog posts.
`_site` will contain the generated static site.

Now what if I have more than one type of posts on my blog. I want something like albums to be separated from typical posts.

So I can let the program search for every directory (not beginning with an underscore) and each of these have it's own `_config.yml` which will dictate how and where *posts* inside this directory show up.

So something like this:

```
.
├── albums
│   ├── _config.yml
│   ├── my-birthday-adventures
│   │   ├── my-birthday-adventures.md
│   │   ├── pic1.png
│   │   ├── pic2.png
│   │   ├── some_random_cake_slaughtering.mp4
│   │   └── zombies.png
│   └── rainy-drainy
│       ├── clouds.png
│       ├── floods.mp4
│       ├── rainy-drainy.md
│       └── water.jpg
├── _config.yml
├── _layouts
│   ├── base.html
│   └── post.html
├── blog
│   ├── my-first-post
│   │   └── my-first-post.md
│   └── my-new-blogging-system
│       ├── my-new-blogging-system.md
│       └── screenshots.png
├── recipes
│   ├─ ...
│   └── ...
└── _site
```
