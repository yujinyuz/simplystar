from pathlib import Path
from litestar import get, Litestar
from litestar.response import Template
from litestar.template import TemplateConfig

from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.contrib.htmx.request import HTMXRequest
from litestar.contrib.htmx.response import HTMXTemplate


@get("/")
async def index() -> Template:
    return Template(template_name="pages/index.html")


@get(path="/form")
async def get_form(request: HTMXRequest) -> Template:
    htmx = request.htmx  #  if true will return HTMXDetails class object
    if htmx:
        print(htmx.current_url)

    context = {}
    return HTMXTemplate(
        template_name="partials/sample.html",
        context=context,
        push_url="/form",
    )


template_config = TemplateConfig(
    directory=Path(__file__).parent / "templates",
    engine=JinjaTemplateEngine,
)


app = Litestar(
    route_handlers=[index, get_form],
    template_config=template_config,
)
