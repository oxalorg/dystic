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
    INDENTATION = re.compile(r'\n\s{2,}')
    META = re.compile(r'^(\w+):\s*(.*(?:\n\s{2,}.*)*)\n')

    def __init__(self):
        self.renderer = HighlightRenderer()
        self.markdown = mistune.Markdown(renderer=self.renderer)


    def to_html(self, text):
        text, metadata = self.extract_meta(text)
        marked = self.markdown(text)
        return marked, metadata

    def extract_meta(self, text):
        """Parse the given text into metadata and strip it for a Markdown parser.

        :param text: text to be parsed
        """
        try:
            META = re.compile(r'^((.+\n)*)(\s*\n\s*)+')
            m = re.split('\n\s*\n', text, maxsplit=1)
            try:
                rv = yaml.load(m[0])
            except:
                rv = {}
            text = m[1].strip()
            return text, rv
        except (IndexError, AttributeError):
            raise SystemExit('A file contains illegal metadata/body text. The file looks like:\n' + text[:500])

    def extract_meta2(self, text):
        """Parse the given text into metadata and strip it for a Markdown parser.

        :param text: text to be parsed
        """
        rv = {}
        m = self.META.match(text)

        while m:
            key = m.group(1)
            value = m.group(2)
            value = self.INDENTATION.sub('\n', value.strip())
            rv[key.lower()] = value
            text = text[len(m.group(0)):]
            m = self.META.match(text)

        return text, rv

if __name__ == '__main__':
    t = """date: 2015-06-14
title: Experiments [alpha]
category: life

I like experiments. They are fun. They give you data. That data gives you an insight into something which would otherwise be extremely hard to recognise.

This is a generic list of the experiments I wish to conduct.
"""
    Marker().extract_meta(t)
