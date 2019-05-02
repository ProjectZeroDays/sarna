import tempfile

import matplotlib.pyplot as plt
from jinja2 import environmentfilter
from markupsafe import Markup
from matplotlib.ticker import MaxNLocator

from sarna.report_generator.docx_renderer import _get_img_prefered_size

_colors = (
    '#5bc0de',
    '#5cb85c',
    '#f0ad4e',
    '#d9534f',
    '#020202'
)


@environmentfilter
def bars(env, data, title='', xlabel='', ylabel=''):
    template = env.globals['docx_render'].get_template()
    lang = env.globals['language']

    bars_names = tuple(x[0].translate_to(lang) for x in data)
    heights = tuple(x[1] for x in data)
    y_pos = range(len(bars_names))

    fig, ax = plt.subplots()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linestyle(":")
    ax.spines['left'].set_linestyle(":")

    bars = ax.bar(y_pos, heights)
    for i, bar in enumerate(bars):
        height = bar.get_height()
        width = bar.get_width()
        bar.set_color(_colors[i])
        ax.text(bar.get_x() + width / 2., height, "{:d}".format(height), ha='center', va='bottom')

    # Add title and axis names
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

    # Limits for the Y axis
    plt.ylim(0, max(heights) * 1.10)

    # Create names
    plt.xticks(y_pos, bars_names)

    fig.set_size_inches(6, 3.5)
    fig.tight_layout()

    with tempfile.NamedTemporaryFile(suffix='.png') as png:
        fig.savefig(png)
        section = template.docx.sections[0]

        width, height = _get_img_prefered_size(png, section)
        pic = template.docx._part.new_pic_inline(
            png, width, height
        ).xml
        return Markup('<w:r><w:drawing>{pic}</w:drawing></w:r><w:br/>'.format(pic=pic))
