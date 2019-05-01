import mistletoe
from jinja2 import environmentfilter
from markupsafe import Markup

from sarna.report_generator.docx_renderer import DOCXRenderer


@environmentfilter
def markdown(env, text, style='default'):
    render_styles = env.globals['docx_render_styles']
    render = env.globals['docx_render']
    lang = env.globals['language']
    render.set_style(render_styles.get_style(style))
    render.set_language(lang)
    return Markup(_markdown_to_docx(text, render))


def _markdown_to_docx(md_data, render: DOCXRenderer):
    ret = mistletoe.markdown(md_data + "\r\n", render)
    for warn in render.warnings:
        # TODO: something
        print(warn)

    return ret
