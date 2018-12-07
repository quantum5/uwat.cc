# `uwat.cf` [![Jenkins](https://img.shields.io/jenkins/s/https/ci.quantum2.xyz/job/uwat.cf.svg)](https://ci.quantum2.xyz/job/uwat.cf/) [![GitHub](https://img.shields.io/github/license/quantum5/uwat.cf.svg)](LICENSE)

`uwat.cf` is a gateway to various resources related to the University of
Waterloo, made by Waterloo students for Waterloo students.

We provide shortcut links to make your life easier. Instead of scrambling to
remember that site where it shows your exam schedule and seating, simply go to
[uwat.cf/exams][1]. The [homepage][2] is a list of these shortcuts.

## Contributing

Everyone is welcome to contribute! Simply send in a pull request with your
useful link, and if it passes quality control, it will be merged and made
available to the public.

To add a link, add the shortcut link and description to the relevant section in
[`src/index.html`][3]. You can also add new sections if none of the existing
sections fit the bill.

To add the redirect, add it to [`src/redirects.conf`][4], into the same place
as you did in `src/index.html`. `redirects.conf` is included inside an
[nginx `map` block][5], and the syntax is:

```
/shortcut "https://example.com/long/url";
```

Thank you for contributing.

  [1]: https://uwat.cf/exams
  [2]: https://uwat.cf
  [3]: src/index.html
  [4]: src/redirects.conf
  [5]: https://nginx.org/en/docs/http/ngx_http_map_module.html
