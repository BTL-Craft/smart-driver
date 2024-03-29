from mcstatus.server import JavaServer
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot.plugin import on_command

mc = on_command("/mc", priority=5)
host = "mc.btlcraft.top"

@mc.handle()
async def mc_handle(bot: Bot, event: Event):
    try:
        server = JavaServer.lookup(host)
        status = server.status()
        msg = f"[CQ:at,qq={event.get_user_id()}]\n" + f"在线：{status.players.online}人\n延迟：{round(status.latency, 2)}ms\n估计实际延迟：{round(status.latency, 2) * 2}ms\n状态：活着\nMOTD：\n{status.description}"
    except:
        msg = "查询失败，看看服务器是不是死了"
    await mc.finish(Message(msg))
    
motd = on_command("/mc motd", priority=5)

@motd.handle()
async def motd_handle(bot: Bot, event: Event):
    try:
        server = JavaServer.lookup(host)
        status = server.status()
        msg = f"[CQ:at,qq={event.get_user_id()}]\n" + f"{status.description}"
    except:
        msg = "查询失败，看看服务器是不是死了"
    await mc.finish(Message(msg))


ping = on_command("/mc ping", priority=5)

@ping.handle()
async def ping_handle(bot: Bot, event: Event):
    try:
        server = JavaServer.lookup(host)
        status = server.status()
        msg = f"[CQ:at,qq={event.get_user_id()}]\n" + f"延迟：{round(status.latency, 2)}ms"
    except:
        msg = "查询失败，看看服务器是不是死了"
    await mc.finish(Message(msg))

players = on_command("/mc player", priority=5)

@players.handle()
async def players_handle(bot: Bot, event: Event):
    try:
        server = JavaServer.lookup(host)
        status = server.status()
        msg = f"[CQ:at,qq={event.get_user_id()}]\n" + f"在线：{status.players.online}人"
    except:
        msg = "查询失败，看看服务器是不是死了"
    await mc.finish(Message(msg))


status = on_command("/mc status", priority=5)

@status.handle()
async def player_handle(bot: Bot, event: Event):
    try:
        server = JavaServer.lookup(host)
        status = server.status()
        msg = f"[CQ:at,qq={event.get_user_id()}]\n" + f"状态：活着"
    except:
        msg = "查询失败，看看服务器是不是死了"
    await mc.finish(Message(msg))
