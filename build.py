#!/usr/bin/env python3
import errno
import os
from html import escape
from hashlib import sha256
from shutil import copyfile

import yaml
from rcssmin import cssmin

DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(DIR, 'src')
DIST_DIR = os.path.join(DIR, 'dist')
ASSETS_SRC = os.path.join(SRC_DIR, 'assets')
ASSETS_DIST = os.path.join(DIST_DIR, 'assets')
ICONS_SRC = os.path.join(SRC_DIR, 'icons')


def build_assets():
    name_map = []
    for asset in os.listdir(ASSETS_SRC):
        name, ext = os.path.splitext(asset)
        if not ext:
            continue

        with open(os.path.join(ASSETS_SRC, asset), 'rb') as f:
            content = f.read()
        hash = sha256(content).hexdigest()[:20]
        dist_name = '%s-%s%s' % (name, hash, ext)

        if ext == '.css':
            content = cssmin(content.decode('utf-8')).encode('utf-8')

        with open(os.path.join(ASSETS_DIST, dist_name), 'wb') as f:
            f.write(content)
        name_map.append((asset, dist_name))
    return name_map


def build_icons():
    for icon in os.listdir(ICONS_SRC):
        copyfile(os.path.join(ICONS_SRC, icon), os.path.join(DIST_DIR, icon))


def build_links(links):
    output = []
    for section in links['sections']:
        output.append('    <h2 id="%s">%s</h2>' % (section['id'], escape(section['name'])))
        output.append('    <ul>')

        for link in section['links']:
            output.append('        <li><a href="{url}">{url}</a> &mdash; {description}</li>'.format(
                url=escape(link['name']), description=escape(link['description'])
            ))

        output.append('    </ul>')
        output.append('')

    return '\n'.join(output)


def build_redirects(links):
    output = []

    def build_link(link):
        output.append('%s "%s";' % (link['name'], link['target']))

    if 'other_links' in links:
        for link in links['other_links']:
            build_link(link)
        output.append('')

    for section in links['sections']:
        output.append('# %s' % (section['name'],))
        for link in section['links']:
            build_link(link)
        output.append('')

    with open(os.path.join(DIST_DIR, 'redirects.conf'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))


def build_index(html_replace, links):
    with open(os.path.join(SRC_DIR, 'index.html'), encoding='utf-8') as f:
        content = f.read()

    for old, new in html_replace:
        content = content.replace(old, new)
    content = content.replace('{listing}', build_links(links))

    with open(os.path.join(DIST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    try:
        os.makedirs(ASSETS_DIST)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    with open(os.path.join(SRC_DIR, 'links.yml'), encoding='utf-8') as f:
        links = yaml.safe_load(f)

    name_map = build_assets()
    build_icons()
    build_index(name_map, links)
    build_redirects(links)


if __name__ == '__main__':
    main()
