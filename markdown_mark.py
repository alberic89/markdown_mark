from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor

MARK_RE =r'(\?{3}|={2})(.*?)(\?{3}|={2})'

class MarkdownMark(Extension):
    def extendMarkdown(self, md):
        del_proc = SimpleTagInlineProcessor(MARK_RE, 'mark')
        md.inlinePatterns.register(del_proc, 'mark', 200)


def makeExtension(**kwargs):
    return MarkdownMark(**kwargs)


if __name__ == '__main__':
    import doctest
    doctest.testfile('README.md')
