#定义杯子父类
class Cups:
    #定义杯子常有的属性
    def __init__(self):
        self.xingzhuang="圆形"
        self.meizhuang="方形"
    #定义加入装水方法
    def zhuangshui(self,water):
        print(f"装了{water}毫升水")


#定义保温杯继承杯子父类
class BaowenCups(Cups):
    #保温杯也有跟父类一样的属性
    def __init__(self):
        super().__init__()
    #保温杯特有的保温方法
    def baowen(self,water):
        print(f"装入{water}毫升水，并保温")
    #重写父类装水的方法
    def zhuangshui(self,water):
        print(f"将{water}毫升水加入保温杯")

#实例化保温杯类，调用装水和保温方法
baowen=BaowenCups()
baowen.zhuangshui("200")
baowen.baowen("200")