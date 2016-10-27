import re
import mistune
import yaml
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class HighlightRenderer(mistune.Renderer):
    """
    Using pygments on code blocks.
    """
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


class Marker:
    """
    Takes in markdown text, returns metadata and html contents.
    """

    def __init__(self):
        self.renderer = HighlightRenderer()
        self.markdown = mistune.Markdown(renderer=self.renderer)

    def to_html(self, text):
        text, metadata = self.extract_meta(text)
        marked = self.markdown(text)
        return marked, metadata

    def extract_meta(self, text):
        """
        Takes input as the entire file.
        Reads the first yaml document as metadata,
        and the rest of the document as text
        """
        first_line = True
        metadata = []
        content = []
        metadata_parsed = False

        for line in text.split('\n'):
            if line.strip() == '' and not metadata_parsed:
                continue
            if line.strip() == '---' and not metadata_parsed:
                if first_line:
                    first_line = False
                    continue
                # reached the last line
                metadata_parsed = True
            elif not metadata_parsed:
                metadata.append(line)
            else:
                content.append(line)

        metadata = yaml.load('\n'.join(metadata))
        return '\n'.join(content), metadata 


if __name__ == '__main__':
    t = """
---
date: 2015-06-14
title: Experiments [alpha]
category: life
---

I like experiments. 
They are fun. 
They give you data. 

---

This is a generic list of the experiments I wish to conduct.
"""
    a, b = Marker().extract_meta(t)
    print(b)
