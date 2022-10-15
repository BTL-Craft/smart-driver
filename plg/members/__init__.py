import json
import os
from nonebot.plugin import on_notice, on_command
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    GroupIncreaseNoticeEvent,
    GroupDecreaseNoticeEvent,
    MessageSegment
)
from ..htmlrender import md_to_pic

import io
from PIL import Image
from datetime import datetime


def save(data, gid):
    fname = "./data/member/"+str(gid)+".json"
    f = open(fname, "w+")
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    f.close()


join = on_notice(priority=5000)


@join.handle()
async def join_handle(bot: Bot, event: GroupIncreaseNoticeEvent):
    gid = event.group_id
    data = await bot.get_group_member_list(group_id=gid)
    await bot.call_api("get_group_member_list", group_id=gid)
    save(data, gid)
    await join.finish()

leave = on_notice(priority=5000)


@leave.handle()
async def leave_handle(bot: Bot, event: GroupDecreaseNoticeEvent):
    gid = event.group_id
    data = await bot.get_group_member_list(group_id=gid)
    await bot.call_api("get_group_member_list", group_id=gid)
    save(data, gid)
    await leave.finish()

list = on_command('/member', priority=5000)


@list.handle()
async def list_handle(bot: Bot, event: GroupMessageEvent):
    gid = event.group_id
    if event.get_plaintext() == '/member update':
        data = await bot.get_group_member_list(group_id=gid)
        await bot.call_api("get_group_member_list", group_id=gid)
        save(data, gid)
        await list.finish('已手动更新群成员列表')
    else:
        if event.get_plaintext() == '/member show':
            data = await bot.get_group_member_list(group_id=gid)
            await bot.call_api("get_group_member_list", group_id=gid)
            save(data, gid)
            fname = "./data/member/" + str(gid) + ".json"
            f = open(fname, "r")
            data = json.loads(f.read())
            fname = "./data/member/temporary.md"
            md = open(fname, "a", encoding="utf8")
            # user_id nickname card role level join_time last_sent_time
            md.write("| QQ号 | 昵称 | 群名片 | 权限 | 等级 | 加入时间 | 最后一次发言时间 |\n")
            md.write(
                "| :----: | :----: | :----: | :----: | :----: | :----: | :----: |\n")
            for i in range(len(data)):
                md.write("| "+str(data[i]["user_id"])+" | "+data[i]["nickname"]+" | "+data[i]["card"]+" | "+data[i]["role"]+" | "+str(
                    data[i]["level"])+" | "+str(datetime.fromtimestamp(data[i]["join_time"]))+" | "+str(datetime.fromtimestamp(data[i]["last_sent_time"]))+" |\n")

            f.close()
            md.close()
            # 解析并输出markdown
            fname = './data/member/temporary.md'
            f = open(fname, 'r', encoding='utf-8')
            doc = f.read()

            pic = await md_to_pic(md=doc, width=1000)

            a = Image.open(io.BytesIO(pic))
            a.save("md2pic.png", format="PNG")
            f.close()
            os.remove(fname)
            await list.finish(MessageSegment.image(pic))

        else:
            await list.finish('用法：\n/member：显示这条信息\n/member update：手动更新群成员列表\n/member show：显示成员列表')
