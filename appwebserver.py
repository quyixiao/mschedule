from aiohttp import web, log
import zerorpc

client = zerorpc.Client()
client.connect('tcp://127.0.0.1:9000')

async def targetshandler(request:web.Request):
    txt = client.get_agents()
    return web.json_response(txt)

async def addtaskhandler(request:web.Request):
    print('-----------')
    data = await request.json()
    return web.json_response(client.add_task(data), status=201)

app = web.Application()
app.router.add_get('/task/agents', targetshandler)
app.router.add_post('/task', addtaskhandler)

web.run_app(app, host='0.0.0.0', port=9900)



