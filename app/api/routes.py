import json

from starlette.requests import Request
from starlette.responses import JSONResponse

from app.orchestrator.orchestrator import Orchestrator


orchestrator = Orchestrator()


async def health_check(request: Request):
    return JSONResponse({
        "status": "success",
        "message": "Avery 2.0 API is running"
    })


async def json_rpc(request: Request):
    try:
        body = await request.json()

        result = await orchestrator.handle_request(body)

        return JSONResponse(result)

    except json.JSONDecodeError:
        return JSONResponse(
            {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32700,
                    "message": "Invalid JSON"
                }
            },
            status_code=400
        )

    except Exception as exc:
        return JSONResponse(
            {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": str(exc)
                }
            },
            status_code=500
        )