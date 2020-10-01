# [`uwat.cc`][1] [![Jenkins](https://img.shields.io/jenkins/s/https/ci.quantum2.xyz/job/uwat.cc.svg)](https://ci.quantum2.xyz/job/uwat.cc/) [![GitHub](https://img.shields.io/github/license/quantum5/uwat.cc.svg)](LICENSE)

[`uwat.cc`][1] is a gateway to various resources related to the University of
Waterloo, made by Waterloo students for Waterloo students.

We provide shortcut links to make your life easier. Instead of scrambling to
remember that site where it shows your exam schedule and seating, simply go to
[uwat.cc/exams][2]. The [homepage][1] is a list of these shortcuts.

## Contributing

Everyone is heartily welcomed to contribute! Simply send in a pull request with your
useful link, and if it passes quality control, it will be merged and made
available to the public.

To add a link, add find the relevant section in under [`src/links.yml`][3],
and under the `links` key, add a new item for your link. This item should be a
mapping with three keys:

* `name`: the shortcut link, starting with `/`, followed by letters, numbers,
  and `-`;
* `target`: the URL to redirect to; and
* `description`: the description of the link shown on the home page.

To be able to run the python scripts locally, run
`pip install -r requirements.txt` to install our dependencies.

To verify that your changes follow the correct format, run automatic sanity
checks with [`python3 check.py`][4].

To generate the HTML for the site, run [`python3 build.py`][5]. Output will be
generated in a directory called `dist`.

Pull requests will be checked with Mr.Travis, by running [`check.py`][4] and
[`build.py`][5]. Please ensure that builds pass. :)

Thank you for contributing.

  [1]: https://uwat.cc
  [2]: https://uwat.cc/exams
  [3]: src/links.yml
  [4]: check.py
  [5]: build.py
