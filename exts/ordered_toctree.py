from docutils import nodes
from sphinx.addnodes import toctree
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.writers.html import HTMLWriter, HTMLTranslator


class AccessibleHTMLBuilder(StandaloneHTMLBuilder):

    name = 'html-a11y'

    @property
    def default_translator_class(self):
        return AccessibleHTMLTranslator


class AccessibleHTMLTranslator(HTMLTranslator):

    def visit_bullet_list(self, node):
        # type: (nodes.Node) -> None
        if len(node) == 1 and node[0].tagname == 'toctree':
            # avoid emitting empty <ol></ol>
            raise nodes.SkipNode
        atts = {}
        old_compact_simple = self.compact_simple
        self.context.append((self.compact_simple, self.compact_p))
        self.compact_p = None
        self.compact_simple = self.is_compactable(node)
        if self.compact_simple and not old_compact_simple:
            atts['class'] = 'simple'
        if node[0].tagname == 'toctree':
            self.body.append(self.starttag(node, 'ol', **atts))
        else:
            self.body.append(self.starttag(node, 'ul', **atts))

    def depart_bullet_list(self, node):
        self.compact_simple, self.compact_p = self.context.pop()
        if node[0].tagname == 'toctree':
            self.body.append('</ol>\n')
        else:
            self.body.append('</ul>\n')


def setup(app):
    app.add_builder(AccessibleHTMLBuilder)
