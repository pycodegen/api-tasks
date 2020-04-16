import asyncio

import uvicorn
from flask import Flask
from server.SocketIOTaskRunner import SocketIOTaskRunner
from task_definitions.TaskDefinitions import task_definition

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketioTaskRunner = SocketIOTaskRunner(
    task_definitions=task_definition,
)


uvicorn.run(
    socketioTaskRunner.app,
    host='127.0.0.1',
    port=30001,
    log_level='info',
)

# socketioTaskRunner.on_taskrun()

# socketioTaskRunner.start()

# async def test_run():
#
#     await socketioTaskRunner.on_taskrun(10, 10)


#
# a = asyncio.wait([
#     socketioTaskRunner.on_taskrun(20, 20),
#     socketioTaskRunner.on_taskrun(10, 10),
#     socketioTaskRunner.on_taskrun(15, 15),
# ])
# loop = asyncio.get_event_loop()
# loop.run_until_complete(a)