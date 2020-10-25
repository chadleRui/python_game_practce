
'''
•	定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
1.	see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”
2.	fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
•	定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
•	加入模块化改造
'''

#定义一个天山童姥类
class TongLao:
    #构造方法初始化童姥的血量和武力值，通过传参赋值
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power
    #定义一个童姥的口号，见到不同的人输出不同的口号
    def see_people(self,name):
        if name == "无崖子":
            print("师弟~~~~！")
        if name == "李秋水":
            print("师弟是俺的！")
        if name == "丁春秋":
            print("叛徒！我杀了你")
    #定义一个童姥的绝招，使用时力量提高10倍，血量减半
    def fight_zms(self,enemy_hp,enemy_power):
        self.hp=self.hp/2
        self.power=self.power*10
        enemy_hp=enemy_hp-self.power
        self.hp=self.hp-enemy_power
        #只做一轮比试，如果敌人血量低则输出下面信息
        if enemy_hp< self.hp:
            print(f"童姥还有{self.hp}血")
            print(f"敌人还有{enemy_hp}血")
            print("哈哈哈，受死吧，再见！")
        #如果童姥血量低，则输出下面信息
        elif enemy_hp> self.hp:
            print(f"童姥还有{self.hp}血")
            print(f"敌人还有{enemy_hp}血")
            print("可恶，今日不和你纠缠，告辞！")
        #平局则输出下面信息
        else:
            print("你小子可以啊，我敬你一回，不送！")

# tongl=TongLao(2000,100)
# tongl.see_people("无崖子")
# tongl.see_people("李秋水")
# tongl.see_people("丁春秋")
# tongl.fight_zms(1000,300)