#定义帮派父类
class Gang:
    #定义帮派常有的属性
    def __init__(self):
        self.man="张三"
        self.gun="手枪"
    #定义打架方法
    def fight(self,man,gun):
        print(f"{man}用{gun}开枪了")


#定义梁山帮派继承帮派父类
class LiangshanGang(Gang):
    #梁山也有跟父类一样的属性
    def __init__(self):
        super().__init__()
    #梁山帮派特有的走私方法
    def zousi(self,man):
        print(f"梁山的{man}从事军火外销")
    #重写打架方法
    def fight(self,man,gun):
        print(f"梁山的{man}拿着{gun}去打架了")

#实例化梁山帮派类，调用走私和打架方法
ls=LiangshanGang()
ls.man="李逵"
ls.fight(ls.man,"M4A1")
ls.zousi("宋江")