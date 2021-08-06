from docutils import nodes
from docutils.parsers.rst import directives, Directive
from sphinx.directives.code import CodeBlock



def setup(app):
    app.add_config_value('replit_user', '', 'html')
    app.add_directive('replit', ReplIt)
    return {'version': '0.1'}


class ReplIt(CodeBlock):

    option_spec = {
        'linenos': directives.flag,
        'slug': directives.unchanged
    }

    url_template = "https://repl.it/@%s/%s"

    def run(self):
        replit_user = self.state.document.settings.env.app.config['replit_user']
        code_node = super(ReplIt, self).run()[0]
        ref_node = nodes.reference('', '')
        ref_node['refuri'] = self.url_template % (replit_user, self.options['slug'])
        ref_node += nodes.Text('repl.it', 'repl.it')
        para_nodes = nodes.paragraph()
        para_nodes += ref_node
        para_nodes['classes'] = ['repl-link']
        return [code_node, para_nodes]
