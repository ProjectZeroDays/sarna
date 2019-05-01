from jinja2 import environmentfilter


@environmentfilter
def locale(env, choice):
    return choice.translation_to(env.globals['language'])
