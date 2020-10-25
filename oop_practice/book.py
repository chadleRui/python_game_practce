#定义书父类
class Book:
    #定义书常有的商品
    def __init__(self):
        self.bookname="《c++从入门到放弃》"
        self.pages="1000"

    #定义书的打人方法
    def hit(self,bookname):
        print(f"将{bookname}举在手中并扔了出去")

#定义玄幻书子类
class XuanhuanBook(Book):
    #玄幻书也有跟父类一样的属性
    def __init__(self):
        super().__init__()
    #玄幻书特有的修仙方法
    def xiuxian(self,bookname):
        print(f"感谢{bookname}给我修仙的方法")
    #重写父类打人的方法
    def hit(self,bookname):
        print(f"将{bookname}玄幻的砸向人，厉害哦")



#实例化玄幻类，调用修仙方法和打人方法
xh=XuanhuanBook()
xh.hit("《遮天》")
xh.xiuxian("《遮天》")