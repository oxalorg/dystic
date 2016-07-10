import re
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
from jinja2 import FileSystemLoader


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

    def __init__(self, text):
        self.metadata, self.text = self.parse_meta(text)


    def to_html(self):
        renderer = HighlightRenderer()
        markdown = mistune.Markdown(renderer=renderer)
        marked = markdown(self.text)
        return marked


    def parse_meta(text):
        """Parse the given text into metadata and strip it for a Markdown parser.

        :param text: text to be parsed
        """
        rv = {}
        m = META.match(text)

        while m:
            key = m.group(1)
            value = m.group(2)
            value = INDENTATION.sub('\n', value.strip())
            rv[key] = value
            text = text[len(m.group(0)):]
            m = META.match(text)

        return rv, text
