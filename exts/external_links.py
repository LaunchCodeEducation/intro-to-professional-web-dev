from docutils.nodes import reference, raw


def setup(app):
    app.connect('doctree-resolved', doctree_resolved)
    return {'version': '0.1'}


def doctree_resolved(app, doctree, document):
    for node in doctree.traverse(reference):
        if not node.get('internal'):
            node['target'] = '_blank'
            text = '<i class="fas fa-external-link-alt" aria-hidden="true"></i>'
            node += raw(text, text, format='html')
