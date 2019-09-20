# # 面向过程编程（从头到尾的执行过程）
# user1 = {'name':'tom','hp':100}
# user2 = {'name':'sherry', 'sherry':80}
#
# def print_role(rolename):
#     print('name is %s, hp is %s' %(rolename['name'],rolename['hp']))
#
# print_role(user1)

# 面向对象编程


# class Player():  # 定义一个类（相似的东西归类），以大写字母开头
#     def __init__(self, name, hp, occu): # 再增加一个属性
#         self.__name = name # 变量被称为属性，函数被称为方法
#         self.hp = hp
#         self.occu = occu
#
#     def print_role(self):  # 定义一个方法
#         print('%s:%s %s' % (self.__name, self.hp, self.occu))
#
#     def updateName(self, newname): # 再增加一个方法
#         self.name = newname

class Monster():
    '定义怪物类'
    # pass # 定义了新的类但暂时不想实现
    def __init__(self, hp=100): # 定义hp的默认值为100
        self.hp = hp
    def run(self):
        print('移动到某个位置')
    def whoami(self):
        print('我是怪物父类')

class Animals(Monster): # 表示属于Monster的子类
    '普通怪物'
    def __init__(self,hp= 10):
        super().__init__(hp)  # 表示在animals子类中不用进行初始化了，父类已经初始化了，节省资源

class Boss(Monster):
    'Boss类怪物'
    def whoami(self):
        print('我是怪物我怕谁')

a1 = Monster(200)
print(a1.hp)
print(a1.run())
a2 = Animals(1)
print(a2.hp)
print(a2.run())

a3 = Boss(800)
a3.whoami()

# user1 = Player('tom', 100, 'war')  # 类的实例化
# user2 = Player('sherry', 80, 'master')
# user1.print_role()
# user2.print_role()
#
# user1.updateName('willom')
# user1.print_role()
# user1.name = ('aaa')
# user1.print_role()