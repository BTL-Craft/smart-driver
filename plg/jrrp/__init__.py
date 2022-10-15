import random
from datetime import date
from ssl import OP_NO_COMPRESSION
from nonebot.plugin import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

def luck_simple(num):
    if num < 18:
        return '大吉'
    elif num < 53:
        return '吉'
    elif num < 58:
        return '半吉'
    elif num < 62:
        return '小吉'
    elif num < 65:
        return '末小吉'
    elif num < 71:
        return '末吉'
    else:
        return '凶'


jrrp = on_command('/jrrp',priority=50)  # type: ignore
@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = rnd.randint(1,100)
    await jrrp.finish(Message(f'[CQ:at,qq={event.get_user_id()}]你今日的幸运指数是{lucknum}/100（越低越好），为"{luck_simple(lucknum)}"\n'))


""" tnnd = on_keyword(['tnnd'],priority=60)  # type: ignore
@tnnd.handle()
async def tnnd_handle(bot: Bot, event: Event):
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = rnd.randint(1,100)
    await jrrp.finish(Message(f'[CQ:at,qq={event.get_user_id()}]管好你逼嘴')) """

sleep = on_keyword(['碎觉了', '睡觉了', '睡了', '睡去', '觉去了'],priority=60)  # type: ignore
@sleep.handle()
async def sleep_handle(event: Event):

    await sleep.finish(Message(f'[CQ:at,qq={event.get_user_id()}]晚安(￣o￣) . z Z'))


