import hypercorn.asyncio
from quart import Quart, request, jsonify, Response
from telethon import TelegramClient
import json
import asyncio


api_id = id
api_hash = 'hash'
client = TelegramClient('anon', api_id, api_hash)

app = Quart(__name__)

loop = client.loop
asyncio.set_event_loop(loop)


async def request_kronotex_bot(article):
    async with client.conversation('kronotex_bot') as conv:
        await conv.send_message(article)
        response = await conv.get_response()
        remains = response.text
        dict_krono = {'bot': 'Kronotex', 'answer': remains}
        return dict_krono


async def request_alixgroup_bot(article):
    #await client.connect()
    async with client.conversation('AlixGroupbot') as conv:
        await conv.send_message('Остатки')
        await conv.get_response()
        await conv.send_message(article)
        response = await conv.get_response()
        remains = response.text
        dict_alix = {'bot': 'Alixgroup', 'answer': remains}
        #await client.disconnect()
        return dict_alix


async def request_skalla_bot(article):
    async with client.conversation('skallabot') as conv:
        await conv.send_message(article)
        response = await conv.get_response()
        remains = response.text
        dist_skalla = {'bot': 'Skalla', 'answer': remains}
        return dist_skalla


async def request_wicanders_bot(article):
    async with client.conversation('wicanders_bot') as conv:
        await conv.send_message(article)
        response = await conv.get_response()
        remains = response.text
        dist_wicanders = {'bot': 'Wicanders', 'answer': remains}
        return dist_wicanders


async def request_nasp(article, bot):
    if bot == "AlixGroupbot":
        dict_nasp = await request_alixgroup_bot(article)
        return dict_nasp
    if bot == "Skallabot":
        dict_nasp = await request_skalla_bot(article)
        return dict_nasp
    if bot == "Wicandersbot":
        dict_nasp = await request_wicanders_bot(article)
        return dict_nasp
    if bot == "Kronotexbot":
        dict_nasp = await request_kronotex_bot(article)
        return dict_nasp
    #raise ValueError('Undefined unit: {}'.format(bot))
    else:
        dict_nasp = {'bot': 'error'}
        return dict_nasp


@app.before_serving
async def startup():
    await client.connect()


@app.after_serving
async def cleanup():
    await client.disconnect()


@app.route('/try/krono', methods=['GET'])
async def krono_req():
    json_krono = await request_kronotex_bot('3678')
    return json_krono


@app.route('/try/alix', methods=['GET'])
async def alix_req():
    json_alix = await request_alixgroup_bot('533123')
    return json_alix


@app.route('/', methods=['POST'])
async def echo() -> Response:
    data = await request.get_json()
    strdata = json.dumps(data)
    jsondata = json.loads(strdata)
    both_dict = []
    for bot_num in jsondata[0]['bots']:
        nasp_dict = await request_nasp(jsondata[0]['query'], bot_num)
        print(nasp_dict)
        both_dict.append(nasp_dict)
        print(bot_num)
    print(both_dict)
    #json_nasp = json.dumps(both_dict, indent=4)
    return jsonify(both_dict)


# async def main():
#     await hypercorn.asyncio.serve(app, hypercorn.Config())
#     loop.run_until_complete(hypercorn.asyncio.serve(app, hypercorn.Config()))

if __name__ == '__main__':
    loop.run_until_complete(hypercorn.asyncio.serve(app, hypercorn.Config()))
