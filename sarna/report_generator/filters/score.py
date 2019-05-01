from jinja2 import environmentfilter
from markupsafe import Markup

from sarna.model.enums import Score, Language
from sarna.report_generator import make_run
from sarna.report_generator.style import RenderStyle


@environmentfilter
def score(env, text, style='default'):
    lang = env.globals['language']
    render_styles = env.globals['docx_render_styles']
    return Markup(_score_to_docx(text, render_styles.get_style(style), lang))


def _score_to_docx(score: Score, style: RenderStyle, lang: Language):
    ret = make_run(getattr(style, score.name.lower()), score.translation_to(lang))
    for warn in style._warnings:
        # TODO: something
        print(warn)

    return ret
