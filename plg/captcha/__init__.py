import _thread
import json
import os
import random
import time
import _thread
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event


captcha = on_command("captcha", aliases={"验证码", "获取验证码"}, priority=5)
maxminute = 5


@captcha.handle()
async def handle_first_receive(bot: Bot, event: Event):

    await captcha.reject(create(event.get_user_id(), random.randint(1000, 9999)))


def create(uid: str, code):

    fname = "./data/captcha.json"
    f = open(fname, "r")  # 打开储存验证码的文件
    l_data = json.loads(f.read())  # 将文件内容解码为python list

    if uid in l_data:
        print(l_data[uid][1])
        print('t')
        if l_data[uid][1] > time.time():  # 验证码有效
            return '请等待之前创建的验证码失效后再重试'
        else:  # 验证码失效，清楚对应的字典元素
            del l_data[uid]

    if uid not in l_data:
        timeout = time.time() + maxminute * 60
        l_data[uid] = [code, timeout]
        f.close()
        f = open(fname, "w+")
        f.write(json.dumps(l_data, sort_keys=True,
                indent=4, separators=(',', ': ')))
        return f'您的验证码是 {code}，{maxminute}分钟内有效'

    f.close()


def thread():
    os.system('python plg/captcha/api.py')


_thread.start_new_thread(thread, ())
