from jinja2 import environmentfilter


@environmentfilter
def locale(env, choice):
    return choice.translate_to(env.globals['language'])
