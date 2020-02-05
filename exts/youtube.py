from docutils import nodes
from docutils.parsers.rst import directives, Directive


def setup(app):
    app.add_config_value('youtube_user', '', 'html')
    app.add_directive('youtube', YouTube)
    return {'version': '0.1'}


class YouTube(Directive):

    GITHUB_URL_TEMPLATE = "https://github.com/{github_user}/{repo}/tree/{branch}"
    YOUTUBE_EMBED_TEMPLATE = """
<div style="text-align:center;"><iframe width="800" height="450" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
"""

    required_arguments = 0
    final_argument_whitespace = True
    has_content = False

    option_spec = {
        'video_id': directives.unchanged,
        'gh_path': directives.unchanged,
    }

    url_template = "https://repl.it/@%s/%s"

    def run(self):

        vid_params = {
            'video_id': self.options['video_id'],
        }

        if 'gh_path' in self.options and len(self.options['gh_path'].split('/')) == 3:
            parts = self.options['gh_path'].split('/')
            gh_params = {
                'github_user': parts[0],
                'repo': parts[1],
                'branch': parts[2],
            }
        else:
            gh_params = {}

        params = {**vid_params, **gh_params}

        text = self.YOUTUBE_EMBED_TEMPLATE.format(**params)

        para_nodes = nodes.paragraph()

        if 'github_user' in params:
            ref_node = nodes.reference('', '')
            ref_node['refuri'] = self.GITHUB_URL_TEMPLATE.format(**params)
            ref_node_text = "{branch} branch".format(**params)
            ref_node += nodes.Text(ref_node_text, ref_node_text)
            para_nodes += nodes.Text("The final code from this video is in the ", "The final code from this video is in the ")
            para_nodes += ref_node
            para_nodes += nodes.Text(params['repo'])

        video_node = nodes.raw('', text, format='html')
        (video_node.source,
            video_node.line) = self.state_machine.get_source_and_line(self.lineno)
        return [video_node, para_nodes]
