from datetime import datetime


def updateDays(s: str):
    programming_beg = datetime(2016, 10, 14)
    timestamp = datetime.now() - programming_beg

    return s.replace(r'{{ DAYS }}', str(timestamp.days))


if __name__ == '__main__':
    with open('README.md', 'w') as readme_file, open('readme-template.md', 'r') as tmpl:
        readme = tmpl.read()
        readme_file.write(updateDays(readme))
