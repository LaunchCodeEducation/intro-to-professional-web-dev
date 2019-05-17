import re
from docutils.nodes import Admonition, admonition, raw, title, warning, note, tip


def setup(app):
    app.connect('doctree-resolved', doctree_resolved)
    app.connect('doctree-read', doctree_read)
    return {'version': '0.1'}


ICONS_CLASSES = {
    "note": "sticky-note",
    "warning": "exclamation-triangle",
    "tip": "lightbulb",
    "example": "binoculars",
    "examples": "binoculars",
    "question": "question",
    "try-it": "puzzle-piece",
    "fun-fact": "rocket"
  }

TEMPLATE = '<i class="fas fa-%s" aria-hidden="true"></i>'


# Convert builtin admonitions to generic ones, for easier icon insertion
def doctree_read(app, doctree):
    for node in doctree.traverse(is_builtin_admonition):
        new_node = admonition()
        name = node.__class__.__name__.title()
        title_node = title(name, name)
        new_node += title_node
        for child in node.children:
            new_node += child
            node.remove(child)
        node.replace_self(new_node)


def is_builtin_admonition(node):
    return node.__class__ in [warning, note, tip]


# insert icons
def doctree_resolved(app, doctree, document):
    for node in doctree.traverse(title):
        if isinstance(node.parent, Admonition):
            node_title = node.children[0].astext()
            slug = node_title.lower().replace(' ', '-')
            slug = re.sub(r'[^a-z\-]', '', slug)
            if slug in ICONS_CLASSES:
                icon = TEMPLATE % ICONS_CLASSES[slug]
                node.insert(0, raw(icon, icon, format='html'))
