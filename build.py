import errno
import os
from hashlib import sha256

from rcssmin import cssmin

DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(DIR, 'src')
DIST_DIR = os.path.join(DIR, 'dist')
ASSETS_SRC = os.path.join(SRC_DIR, 'assets')
ASSETS_DIST = os.path.join(DIST_DIR, 'assets')

bytes = type(b'')


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
            content = cssmin(content)

        with open(os.path.join(ASSETS_DIST, dist_name), 'wb') as f:
            f.write(content)
        name_map.append((bytes(asset), bytes(dist_name)))
    return name_map


def build_files(html_replace):
    for name in os.listdir(SRC_DIR):
        src_path = os.path.join(SRC_DIR, name)
        if not os.path.isfile(src_path):
            continue

        with open(os.path.join(SRC_DIR, name), 'rb') as f:
            content = f.read()

        if name.endswith('.html'):
            for old, new in html_replace:
                content = content.replace(old, new)

        with open(os.path.join(DIST_DIR, name), 'wb') as f:
            f.write(content)


def main():
    try:
        os.makedirs(ASSETS_DIST)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    name_map = build_assets()
    build_files(name_map)

if __name__ == '__main__':
    main()
