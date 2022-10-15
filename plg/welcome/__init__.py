import io
import random
from time import sleep
from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, GroupIncreaseNoticeEvent, MessageSegment, Message
from PIL import Image
from plg.htmlrender.date_source import md_to_pic
from plg.imagerender import _md2pic



welcom = on_notice()


@welcom.handle()
async def mc_handle(bot: Bot, event: GroupIncreaseNoticeEvent):
    msg = get_text(event.get_user_id())
    await welcom.send(Message(msg))
    from pathlib import Path

    # 如果是直接获取消息内容 需要 unescape
    from nonebot.adapters.onebot.v11 import unescape
    fname = './doc/rule.md'
    f = open(fname, 'r', encoding='utf-8')
    doc = f.read()

    # css_path 可选
    # pic = await md_to_pic(
    #     md=msg, css_path=str(Path(__file__).parent / "templates" / "markdown.css")
    # )

    pic = await md_to_pic(md=doc)

    a = Image.open(io.BytesIO(pic))
    a.save("md2pic.png", format="PNG")
    sleep(10)
    await welcom.send(MessageSegment.image(pic))
    sleep(1)
    await welcom.finish(Message(f"[CQ:at,qq={event.get_user_id()}] 请遵守服务器规则，如果对上面这张自动生成的截图不满意可以访问官网获得更好的阅读体验：\nhttp://btl-craft.test.upcdn.net/help/rule"))
    
def get_text(uid):
    话术表 = [
        f'这个服又多了一个成员！怎么想都是 [CQ:at,qq={uid}] 的错',
        f'万众瞩目的 [CQ:at,qq={uid}] 终于来了，让我们用掌声和热情激烈的欢迎他！',
        f'[CQ:at,qq={uid}] 进入了群 过度的索取终究会带来灭亡...',
        f'[CQ:at,qq={uid}] 来了 快上车！没时间解释了！',
        f'新成员揭开了神秘的面具，原来他是 [CQ:at,qq={uid}] ',
        f'[CQ:at,qq={uid}] 快看看我！我是黄瓜瑞克！',
        f'欢迎 [CQ:at,qq={uid}] 进入群 但是我们已经没有多余的僵立停了...',
        f'有请新加入的 [CQ:at,qq={uid}] 给大家整活儿',
        f'[CQ:at,qq={uid}] 来支援我们了！他肯定不会让这条战线垮掉的！',
        f'[CQ:at,qq={uid}] 进入了群 嘿！有人想要出来和他一较高下吗？',
        f'[CQ:at,qq={uid}] 进入了群 请各位成员不要在甲板上空中劈叉',
        f'我不演了，我摊牌了， [CQ:at,qq={uid}] 就是我们新的一员',
        f'[CQ:at,qq={uid}] 手里提着两斤鳎目，腰里别着个喇叭进入了群',
        f'[CQ:at,qq={uid}] 发出了耀眼的光芒！他进化成了......什么也没有',
        f'你以为他在第一层，但其实 [CQ:at,qq={uid}] 在第五层',
        f'[CQ:at,qq={uid}] 进入了群！是新的朋友！是新的好兄弟！',
        f'是谁？有那广阔的胸怀？是谁？站在那高耸的山峰上？是 [CQ:at,qq={uid}]',
        f'我不演了，我摊牌了， [CQ:at,qq={uid}] 就是我们新的一员',
        f'我们刚刚见证了 [CQ:at,qq={uid}] 加入了我们光荣的战团！',
        f'欢迎你陌生的 [CQ:at,qq={uid}] 所有人都想在这个小镇用铅换黄金...',
        f'[CQ:at,qq={uid}] 就是你！为什么要杀害我的妻儿！来打把昆特牌吧~',
        f'[CQ:at,qq={uid}] 从天而降，原来就是你炸了系守镇！',
        f'三年二班 [CQ:at,qq={uid}] 同学！你妈妈拿了两罐BTL牛奶！要给你！',
        f'铁头娃成员 [CQ:at,qq={uid}] 带着他的小姨子来了！',
        f'只要像这样把生石灰慢慢的倒入水中...啊！[CQ:at,qq={uid}] 我们等...（boom）',
        f'我们被延迟劝退了...但是 [CQ:at,qq={uid}] 进来啦！',
        f'[CQ:at,qq={uid}] ，加入了队伍！',
        f'欢迎你！在那山的那边海的那边有一个 [CQ:at,qq={uid}]',
        f'[CQ:at,qq={uid}] 来了，简直就像...就像...我编不下去了',
        f'[CQ:at,qq={uid}] 从餐馆回到了群，他挺着肚子表示已经吃不下了',
        f'如果上帝为 [CQ:at,qq={uid}] 关上了一扇门，那么上帝就会让他进入群',
        f'时间？真的又到了那个时间了吗？ [CQ:at,qq={uid}] 先生？',
        f'斗宗强者 [CQ:at,qq={uid}] ，君临群！还不赶快出来求饶？',
        f'欢迎 [CQ:at,qq={uid}] 进入群 我将挥舞铁锤，行使正义！',
        f'[CQ:at,qq={uid}] 一位！这位爷，里边儿请！',
        f'你们见过 [CQ:at,qq={uid}] 了吗？以后他就是我们的人了',
        f'[CQ:at,qq={uid}]，你选择红色药丸还是蓝色药丸？',
        f'啊！[CQ:at,qq={uid}] 博士，我以为你和那些外星人一起留在黑山基地了...',
        f'手头活都放一放， [CQ:at,qq={uid}] 来了！',
        f'你们见过 [CQ:at,qq={uid}] 了吗？以后他就是我们的人了',
        f'天才玩家 [CQ:at,qq={uid}] 进入了群，这把我们有救辣！',
        f'[CQ:at,qq={uid}] 开着他的龙卷风破烂老爷车进入了群',
        f'[CQ:at,qq={uid}] 加入了我们！Level UP！',
        f'[CQ:at,qq={uid}] 进入了群，但事态远没有他想的那么简单 ',
        f'[CQ:at,qq={uid}]，黑暗给你打了电话',
        f'[CQ:at,qq={uid}] 刚从5000年的长眠中醒来，该让这些人知道谁才是他们皇帝了',
        f'欢迎你陌生的 [CQ:at,qq={uid}] 所有人都想在这个小镇用铅换黄金...',
        f'电闪雷鸣风雨交加， [CQ:at,qq={uid}] 降临了！',
        f'[CQ:at,qq={uid}] 曾经也是个勇者，直到他的膝盖中了一箭',
        f'热烈欢迎 [CQ:at,qq={uid}]！你是电~你是光~你是唯一的神话~',
        f'[CQ:at,qq={uid}] 进入了群 嘿！有人想要出来和他一较高下吗？',
        f'[CQ:at,qq={uid}] 已经无人能挡了！他已经超神了！',
        f'[CQ:at,qq={uid}] 从天而降，原来就是你炸了系守镇！',
        f'[CQ:at,qq={uid}]，对吾起，吾系差人',
        f'[CQ:at,qq={uid}] 来到了群，将其裹上蛋液面包糠，炸至金黄...',
        f'[CQ:at,qq={uid}] 进入了群！是新的朋友！是新的好兄弟！',
        f'是他！就是他！我们的朋友 [CQ:at,qq={uid}]',
        f'热烈欢迎 [CQ:at,qq={uid}]！你是电~你是光~你是唯一的神话~',
        f'我的名字叫 [CQ:at,qq={uid}]，是一个普通的上班族...',
        f'我轻轻的走了，正如 [CQ:at,qq={uid}] 轻轻的来',
        f'[CQ:at,qq={uid}] 吃掉了你的脑子！',
        f'[CQ:at,qq={uid}] 来支援我们了！他肯定不会让这条战线垮掉的！',
        f'[CQ:at,qq={uid}] 来了，他就是那个行天之道总司一切的人！',
        f'[CQ:at,qq={uid}] 是一个真正的大师，他永远怀着一颗学徒的心',
        f'[CQ:at,qq={uid}] 连宇宙的边缘都不知道在哪儿，怎么会晓得这个',
        f'[CQ:at,qq={uid}] 加入了我们！Level UP！',
        f'[CQ:at,qq={uid}] 从餐馆回到了群，他挺着肚子表示已经吃不下了',
        f'[CQ:at,qq={uid}] 宁愿上战场，也不愿意在沙滩上晒太阳',
        f'来了个新人，[CQ:at,qq={uid}]，大家快来欺负他！',
        f'[CQ:at,qq={uid}] f.h.y 戴着黄色眼镜进入了群，他看什么都是黄色的',
        f'铁头娃成员 [CQ:at,qq={uid}] 带着他的小姨子来了！',
        f'告诉你的父亲，亲爱的 [CQ:at,qq={uid}]，准备好迎接出乎意料的结果吧...',
        f'[CQ:at,qq={uid}]，你选择红色药丸还是蓝色药丸？',
        f'给老子爬起来！[CQ:at,qq={uid}]！让我们把这城市烧成灰！',
        f'我们的好兄弟，团队的核心 [CQ:at,qq={uid}] 进入了群',
        f'[CQ:at,qq={uid}] 在无聊的夜晚辗转反侧，最终进入了群找乐子',
        f'警告！警告！[CQ:at,qq={uid}] 灾害浓度五级警告！',
        f'[CQ:at,qq={uid}]！你在干什么啊！不要停下来啊！',
        f'欢迎 [CQ:at,qq={uid}] 有朋自远方来，不亦说乎！',
        f'吼！没有逃走反而是朝这里走过来了吗？[CQ:at,qq={uid}]！',
        f'嘿！ [CQ:at,qq={uid}]！有内鬼！终止交易！',
        f'我们的好兄弟，团队的核心 [CQ:at,qq={uid}] 进入了群',
        f'[CQ:at,qq={uid}] 倒在地上，双眼反射出诡异的光',
        f'狂风呼啸 *站在你面前的是 [CQ:at,qq={uid}]，一个真正的勇士',
        f'快看，这是一种叫做 [CQ:at,qq={uid}] 的地球生物',
        f'[CQ:at,qq={uid}]！你tnd意大利炮呢？给他来一炮！',
        f'此乃佛门净地，[CQ:at,qq={uid}] 也敢私闯？大威天龙！世尊地藏！般若诸佛！般若巴麻空！',
        f'电闪雷鸣风雨交加， [CQ:at,qq={uid}] 降临了！',
        f'[CQ:at,qq={uid}] 已经无人能挡了！他已经超神了！',
        f'啊嘞哇，打雷打？打雷打？打雷打？啊嘞哇， [CQ:at,qq={uid}]！',
        f'[CQ:at,qq={uid}]！你在干什么啊！不要停下来啊！',
        f'狂风呼啸 *站在你面前的是 [CQ:at,qq={uid}]？刹那！，一个真正的勇士',
    ] # 从开黑啦复制过来时，使用正则表达式@.*?\s来匹配大部分名称，没匹配到的要手动修改，用\[.*?\]来检查已修改的
    max = len(话术表) - 1
    id = random.randint(0,max)
    return 话术表[id]
