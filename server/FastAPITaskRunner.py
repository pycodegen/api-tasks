from fastapi import (
    FastAPI,
    WebSocket,
)

app = FastAPI()


@app.websocket('/upload/{file_id}')
async def websocket_endpoint(
        websocket: WebSocket,
        file_id: str,
):
    pass