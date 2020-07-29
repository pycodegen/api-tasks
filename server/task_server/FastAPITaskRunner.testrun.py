from fastapi import (
    FastAPI,
    WebSocket,
)
import uvicorn

app = FastAPI()



@app.websocket('/upload/{file_id}')
async def websocket_endpoint(
        websocket: WebSocket,
        file_id: str,
):
    print('file_id', file_id)
    data = await websocket.receive_json(mode='binary')
    print('data:', data)

uvicorn.run(app)