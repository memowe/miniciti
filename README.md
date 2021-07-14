# miniciti

A small [city][city]

[![Unit tests](https://github.com/memowe/miniciti/actions/workflows/test.yml/badge.svg)](https://github.com/memowe/miniciti/actions/workflows/test.yml)

## Run tests

```bash
$ pip3 install pipenv
$ pipenv install --dev
$ pipenv run pytest
```

## Use as dependency

`Pipfile`:

```toml
[packages]
miniciti = { git = 'https://github.com/memowe/miniciti.git', ref = 'main' }
...
```

## Author and license

(c) 2021 [Mirko Westermeier][memowe] <[mirko@westermeier.de][mail]>

Licensed under the MIT license (see [LICENSE][license] for details)

[city]: https://github.com/scdh/city
[memowe]: https://github.com/memowe
[mail]: mailto:mirko@westermeier.de
[license]: LICENSE
