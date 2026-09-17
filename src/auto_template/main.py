import os
from typing import Any

from fastapi.templating import Jinja2Templates
from starlette.requests import Request


def canonical_url_processor(request: Request) -> dict[str, Any]:
    base_url = str(request.base_url).rstrip("/")

    return {"canonical_url": f"{base_url}{request.url.path}"}


def static_version(path: str) -> float:
    return os.path.getmtime(path)


def setup_templates(directory: str, **kwargs: Any) -> Jinja2Templates:
    existing_processors = kwargs.pop("context_processors", [])
    context_processors = [canonical_url_processor, *existing_processors]

    templates = Jinja2Templates(
        directory=directory,
        context_processors=context_processors,
        **kwargs,
    )

    templates.env.globals["static_version"] = static_version

    return templates
