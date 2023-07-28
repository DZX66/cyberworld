# =-= coding:utf-8 =-=
import function

def write_script():
    talker = ["玛莉特"]
    script = ""
    while True:
        sender = function.select(["结束", "自定义", "旁白"] + talker)
        if sender == 0:
            break
        elif sender == 1:
            custom_sender = input("请输入自定义发出者名称：")
            talker.append(custom_sender)
        content = input("请输入内容：")
        if sender == 1:
            script += f'function.talk("【{custom_sender}】 {content}")\n'
        elif sender == 2:
            script += f'function.talk("{content}")\n'
        else:
            script += f'function.talk("【{talker[sender-3]}】 {content}")\n'

    return script


script = write_script()
print(script)
