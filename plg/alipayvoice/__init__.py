import cn2an
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from ffmpy import FFmpeg
alipay_voice = on_command("/alipay", aliases={"/pay"})


@alipay_voice.handle()
async def alipay(matcher: Matcher, args: Message = CommandArg()):
    amount = args.extract_plain_text().replace("元", "")
    if not amount:
        return
    if not amount.isdigit():
        try:
            amount = cn2an.cn2an(amount, "smart")
        except Exception:
            await matcher.send("错误的，请输入正确的数字")
    if 0.01 <= float(amount) <= 999999999999.99:
        url = f"https://mm.cqu.cc/share/zhifubaodaozhang/mp3/{amount}.mp3"
        await matcher.send(MessageSegment.record(url))
    else:
        await matcher.send("数字大小超出限制，支持范围为0.01~999999999999.99")
