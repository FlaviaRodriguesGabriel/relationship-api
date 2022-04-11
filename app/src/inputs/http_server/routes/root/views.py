import json

from django.conf import settings
from django.http import HttpRequest, HttpResponse

from outputs.gremlin_server import GremlinServer

# gremlim_server = GremlinServer()


def index(request: HttpRequest) -> HttpResponse:
    data = json.dumps(
        {
            "app_name": settings.APP_NAME,
            "environment": settings.ENVIRONMENT,
            "version": settings.VERSION,
            # "gremlin_server": id(gremlim_server),
            # "graph_db": str(gremlim_server.graph_db),
        }
    )
    return HttpResponse(data, content_type="application/json")
