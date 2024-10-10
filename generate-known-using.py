from typing import Final
from inspect import cleandoc as trim_margin
import yaml
from update_readme_dates import updateDays

SIZE: Final = 40
BEG_MARKER: Final = '<!-- knownUsing -->'
END_MARKER: Final = '<!-- knownUsing-end -->'


def read(name: str) -> str:
    with open(name, 'r') as f:
        return f.read()


def makesrc(name: str) -> str:
    return f'https://raw.githubusercontent.com/github/explore/master/topics/{name}/{name}.png'


def template(*, url: str, name: str, src: str = None) -> str:
    if src is None:
        src = makesrc(name)

    return '\n' + trim_margin(f"""
        <a title="{name.capitalize()}" href="{url}">
            <img height="{SIZE}" src="{src}" alt="{name.capitalize()}\'s logo" />
        </a>""") + '\n'


known_technologies = read('known-technologies.yml')
known_technologies = yaml.load(known_technologies, Loader=yaml.Loader)

readme = read('readme-template.md')
beg_pos = readme.find(BEG_MARKER)
end_pos = readme.find(END_MARKER) + len(END_MARKER)

processed_readme = readme[:beg_pos]

for tech_name in known_technologies:
    tech = known_technologies[tech_name]

    if type(tech) is str:
        processed_readme += template(url=tech, name=tech_name)
    else:
        assert ('url' in tech)
        name = tech['name'] if 'name' in tech else tech_name
        processed_readme += template(url=tech['url'],
                                     name=name, src=tech.get('icon'))


processed_readme += readme[end_pos:]
processed_readme = updateDays(processed_readme)

with open('README.md', 'w') as f:
    f.write(processed_readme)
