#!/usr/bin/env python3
import os
import re

import yaml

SRC_DIR = os.path.join(os.path.dirname(__file__), 'src')


def ensure(cond, output):
    if not cond:
        raise SystemExit(output)


def check_link(link, description=True):
    ensure(isinstance(link, dict), 'a link must be dict, not: %s' % (link,))

    ensure('name' in link, 'a link must contain a name: %s' % (link,))
    ensure(isinstance(link['name'], str), 'key "name" under link must be string: %s' % (link,))
    ensure(link['name'].startswith('/'), 'the name of a link must start with /: %s' % (link,))
    ensure(re.match('^/[a-z0-9-]+$', link['name']),
           'the name of a link must be / followed by letters, numbers, and -, not %s' % (link['name'],))

    ensure('target' in link, 'link "%s" must contain a target' % (link['name'],))
    ensure(isinstance(link['target'], str), 'key "target" under link "%s" must be string' % (link['name'],))

    if description:
        ensure('description' in link, 'link "%s" must contain a description' % (link['name'],))
        ensure(isinstance(link['description'], str),
               'key "description" under link "%s" must be string' % (link['name'],))


def main():
    with open(os.path.join(SRC_DIR, 'links.yml'), encoding='utf-8') as f:
        links = yaml.safe_load(f)

    unique = set()

    ensure('sections' in links, 'links.yml should contain key "sections"')
    ensure(isinstance(links['sections'], list), 'key "sections" should map to a list')

    for section in links['sections']:
        ensure(isinstance(section, dict), 'every item in "sections" should be a dict')

        ensure('id' in section, 'every section must have an id')
        ensure(isinstance(section['id'], str), 'section IDs must be strings')
        ensure(re.match('^[a-z-]+$', section['id']), 'section IDs should only contain lowercase letters and -')

        ensure('name' in section, 'every section must have a name')
        ensure(isinstance(section['name'], str), 'section names must be strings')

        ensure('links' in section, 'every section must have links')
        ensure(isinstance(section['links'], list), 'links under %s must be a list' % (section['id'],))

        for link in section['links']:
            check_link(link)

            if link['name'] in unique:
                raise SystemExit('duplicate link "%s"' % link['name'])
            unique.add(link['name'])

    if 'other_links' in links:
        ensure(isinstance(links['other_links'], list), 'other_links must be a list')

        for link in links['other_links']:
            check_link(link, description=False)

            if link['name'] in unique:
                raise SystemExit('duplicate link "%s"' % link['name'])
            unique.add(link['name'])

    with open(os.path.join(SRC_DIR, 'index.html'), encoding='utf-8') as f:
        contents = f.read()
        ensure('{listing}' in contents, 'index.html should have {listing}')


if __name__ == '__main__':
    main()
