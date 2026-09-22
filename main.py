from starlette.applications import Starlette
from starlette.routing import Route

from app.api.routes import health_check, json_rpc


routes = [
    Route("/health", health_check, methods=["GET"]),
    Route("/rpc", json_rpc, methods=["POST"]),
]

app = Starlette(
    debug=True,
    routes=routes
)