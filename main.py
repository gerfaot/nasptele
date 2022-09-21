from telethon import TelegramClient


api_id = id
api_hash = 'hash'
client = TelegramClient('anon', api_id, api_hash)


async def request_alixgroup_bot(article):
    async with client.conversation('AlixGroupbot') as conv:
        await conv.send_message('Остатки')
        await conv.get_response()
        await conv.send_message(article)
        response = await conv.get_response()
        remains = response.text
        list_alix = {'bot': 'Alixgroup', 'answer': remains}
        return list_alix


async def request_skalla_bot(article):
    async with client.conversation('skallabot') as conv:
        await conv.send_message(article)
        response = await conv.get_response()
        remains = response.text
        list_skalla = {'bot': 'Skalla', 'answer': remains}
        return list_skalla


async def request_wicanders_bot(article):
    async with client.conversation('wicanders_bot') as conv:
        await conv.send_message(article)
        response = await conv.get_response()
        remains = response.text
        list_wicanders = {'bot': 'Wicanders', 'answer': remains}
        return list_wicanders


async def request_brateclis_bot(article):
    async with client.conversation('sdvor_911_bot') as conv:
        await conv.send_message(article)
        await conv.get_response()
        await conv.get_response()
        response = await conv.get_response()
        remains = response.text
        list_skalla = {'bot': 'Brateclis', 'answer': remains}
        return list_skalla


async def request_kronotex_bot(article):
    async with client.conversation('kronotex_bot') as conv:
        await conv.send_message(article)
        response = await conv.get_response()
        remains = response.text
        list_krono = {'bot': 'Kronotex', 'answer': remains}
        #json_krono = json.dumps(list_krono, indent=4)
        return list_krono


async def request_nasp(article, bot):
    if bot == "AlixGroupbot":
        json_nasp = await request_alixgroup_bot(article)
        return json_nasp
    else:
        json_nasp = await request_kronotex_bot(article)
        return json_nasp


async def main():

    os = await request_brateclis_bot('CA158')
    print(os)


with client:
    client.loop.run_until_complete(main())

