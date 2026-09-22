import pytest

from app.orchestrator.orchestrator import Orchestrator


@pytest.mark.asyncio
async def test_missing_message():

    orchestrator = Orchestrator()

    result = await orchestrator.handle_request({
        "jsonrpc": "2.0",
        "id": 1,
        "params": {}
    })

    assert result["error"]["code"] == -32602