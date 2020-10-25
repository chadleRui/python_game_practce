'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
'''
#引入童姥父类
from oop_practice.wulin_tonglao import TongLao

#定义虚竹，继承童姥父类
class XuZhu(TongLao):
    #虚竹不打人，所以你只能看到他，和念经的方法
    def __init__(self):
        print("你看到了虚竹，想偷袭他")
    #虚竹启动念经模式
    def read(self):
        print("你的攻击miss了，并且虚竹说：")
        print("罪过罪过，施主不要被执念所固")
    #虚竹看到不同人的话术
    def say(self,name):
        print("只见虚竹说道：")
        if name == "梦姑":
            print("啊，梦姑，我中意你，但我说不出口。⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄")
        elif name == "乔峰":
            print("大哥好！")
        elif name == "段誉":
            print("二哥好！")
        else:
            print("阿弥陀佛~")
xz=XuZhu()
# xz.read()
xz.say("梦姑")
xz.say("乔峰")
xz.say("段誉")
xz.say("野比大雄")
