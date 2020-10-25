#定义手机父类
class Phone:
    #定义手机常有的属性
    def __init__(self):
        self.brand="手机"
        self.size="6.5寸"
        self.name="安卓手机"
    #定义打电话方法
    def call(self,number):
        print(f"拨打{number}")
    #定义上网方法
    def surfTheNet(self,page):
        print(f"去{page}浏览网页")

#定义华为继承手机父类
class Huawei(Phone):
    #华为也有跟父类一样的属性
    def __init__(self):
        self.brand="华为"
        self.size="6.5寸"
        self.name="P40"
        self.chip="麒麟"
    #华为特有的华为支付方法
    def huaweiPay(self,money):
        print(f"在华为支付花了{money}块钱")

    #重写父类的打电话和上网方法
    def call(self, number):
        print(f"用华为手机拨打{number}")
    def surfTheNet(self, page):
        print(f"在华为手机上去{page}浏览网页")



#实例化华为类，调用付款方法和打电话方法
hw=Huawei()
hw.call("110")
hw.surfTheNet("华为商城")