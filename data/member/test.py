import json


fname = "E:/Desktop/bot/smart-driver/data/member/484408987.json"
f = open(fname, "r")
data = json.loads(f.read())
fname = "E:/Desktop/bot/smart-driver/data/member/md.md"
md = open(fname, "a", encoding="utf8")
md.write("| QQ号 | 昵称 | 群名片 | 等级 | 加入时间 | 最后一次发言时间 |\n") # user_id nickname card level role join_time last_sent_time  
md.write("| :----: | :----: | :----: | :----: | :----: | :----: |\n")
for i in range(len(data)):
    md.write("| "+str(data[i]["user_id"])+" | "+data[i]["nickname"]+" | "+data[i]["card"]+" | "+str(data[i]["level"])+" | "+str(data[i]["join_time"])+" | "+str(data[i]["last_sent_time"])+" |\n")

f.close()
md.close()