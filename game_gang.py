"""
一个回合制游戏，角色都有hp 和power，hp代表血量，power代表攻击力，
my_hp的初始值为1000，power的初始值为150。
定义一个gang方法：
my_hp = my_hp - enemy_power
enemy_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""
import random

#定义打架方法，传入敌人血量和攻击力
def gang(enemy_hp,enemy_power):
    #定义自己的血量和攻击力
    my_hp=1000
    my_power=150
    print(f"你总共有{enemy_hp}血量，我要打你了！")
    #循环，控制双方不断攻击，知道满足条件结束
    while True:
        #开始攻击
        my_hp=my_hp - enemy_power
        enemy_hp= enemy_hp - my_power
        # print(f"被你打掉{enemy_power},我还有{my_hp}血。")
        # print(f"你被我打掉{my_power}血，还剩{enemy_hp}")
        #当自己血量低于等于0，结束输出“你赢了”，break结束while循环
        if my_hp<=0:
            print(f"我还有{my_hp}血")
            print(f"你还有{enemy_hp}血")
            print("你赢了")
            break
        #当敌人血量低于等于0，结束输出“我赢了”，break结束while循环
        elif enemy_hp<=0:
            print(f"我还有{my_hp}血")
            print(f"你还有{enemy_hp}血")
            print("我赢了")
            break
#定义main方法，调用gang()方法
if __name__ == '__main__':
    #定义血量，通过列表解析式生成一个区间列表
    hp=[ x for x in range(995,1010) ]
    #将生成的列表放入敌人血量中，并用choice随机读取一个值作为敌人血量
    enemy_hp=random.choice(hp)
    #用randint定义随机敌人的攻击力区间值
    enemy_power=random.randint(120,160)
    #调用gang()方法，敌我开始打架
    gang(enemy_hp,enemy_power)
