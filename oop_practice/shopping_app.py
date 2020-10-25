#定义购物APP父类
class ShoppingAPP:
    #定义购物软件常有的商品
    def __init__(self):
        self.shuma="手机"
        self.meizhuang="粉底"
        self.xiezi="运动鞋"
        self.yifu="上衣"
    #定义加入购物车方法
    def gouwuche(self,things):
        print(f"将{things}加入购物车")
    #定义付款方法
    def fukuan(self,things):
        print(f"为{things}付款")

#定义淘宝继承购物APP父类
class Taobao(ShoppingAPP):
    #淘宝也有跟父类一样的商品
    def __init__(self):
        super().__init__()
    #淘宝特有的天猫超市方法
    def tmMarcket(self,things):
        print(f"在天猫超市买{things}")
    #购物车和付款重写父类的方法
    def gouwuche(self,things):
        print(f"将{things}加入淘宝购物车")
    def fukuan(self,things):
        print(f"在淘宝上为{things}付款")

#定义京东继承购物APP父类
class Jingdong(ShoppingAPP):
    # 京东也有跟父类一样的商品
    def __init__(self):
        super().__init__()
    #特有的京东超市方法
    def jdMarcket(self,things):
        print(f"在京东超市买{things}")
    #复写父类的购物车和付款方法
    def gouwuche(self,things):
        print(f"将{things}加入京东购物车")
    def fukuan(self,things):
        print(f"在京东上为{things}付款")

#实例化京东类，调用京东超市方法和付款方法
jd=Jingdong()
jd.jdMarcket("牙膏")
jd.fukuan("袜子")