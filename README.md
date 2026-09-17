# auto_template
Auto-configures FastAPI's Jinja2Templates with canonical URL and static file cache-busting on import.

[![PyPI version](https://img.shields.io/pypi/v/auto_template.svg)](https://pypi.org/project/auto_template/)
[![Python versions](https://img.shields.io/pypi/pyversions/auto_template.svg)](https://pypi.org/project/auto_template/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What does this package do?
This package automatically assigns versions to static files and completes the canonical values.

## Installation
- Install via pip
    ```bash
    pip install auto_template
    ```
- Install via uv
    ```bash
    uv add auto_template
    ```

## Usage
- `app.py`
    ```python
    from fastapi import FastAPI
    from auto_template import setup_templates

    app = FastAPI()

    templates = setup_templates(directory="templates")
    ```
- `templates/base.html`
    ```html
    <head>
        <link rel="stylesheet" href="<path_to_css_file>v?={{ static_version('<path_to_css_file') }}">
        <link rel="canonical" href="{{ canonical_url }}">
    </head>
    ```

## License
[MIT](./LICENSE)