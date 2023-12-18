import datetime

class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.balance = 0
        self.branches = [] # 存所有分校对象 
        # self.stu_number = stu_number 
        print(f'我们创建了学校总部 {self.name}')
    def count_stu_number(self):
        pass
    def pay_salary(self):
        pass
    def stuff_enrollment(self):
        pass
    def count_total_revenue(self):
        print("-------校区总收入")
        total = 0
        print(f'总校总收入为{self.name}, {self.balance}')
        for b in self. branches: 
            print(b.name, b.balance)
            total += b.balance 
        print(f'各个分校总共收入为{total}') 
    def __repr__(self): #打印name而不是内存地址 
        return self.name 
    
class Branch(School):
    def __init__(self, name, address,headquarter_obj) -> None:
        super().__init__(name, address)
        self.headquarter = headquarter_obj # 将分校和总部链接 （我叫它headquarter——obj就是提醒自己 这个是要把school实例化headquarter拿过来用）
        self.headquarter.branches.append(self) # 把自己加入总校的校区列表， 建立 总部->分校的反向关联 （说了headquarter是school实例来的 所以school类的东西拿过来直接用 比如branches）


class Class: 
    def __init__(self,semaster,school,course_obj) -> None:
       # self.class_obj = class_obj
        self.semaster =semaster
        self.school = school  # 这里school直接就是class school实例带进来，所以下面可以直接.name?? 
        self.course_obj = course_obj
        self.stu_list =[]
    def Stu_transfer(self, class_obj, school):
        pass
    def __str__(self) -> str: # 打印not IP地址 rather属性信息, 属性是来自School类
        return (f'{self.school.address},{self.school.name}“课程为” {self.course_obj.name}{self.semaster}')
    

class Course:
    def __init__(self, name, outline, price):
        self.name = name 
        self.outline = outline
        self.price = price
        print(f'学校总部创建了{self.name}课程，学费是{self.price}')
        
            
class Student: 
    def __init__(self, name, class_obj, balance: int):
        self.balance = balance
        self.name = name
        self. class_obj = class_obj
        # 加入班级
        class_obj.stu_list.append(self) #student类和class类互相关联
        # 交学费
        class_obj.school.balance += class_obj.course_obj.price #这里.school; .course_obj都是从school和course实例化初始化拿过来用的
        self.balance -= class_obj.course_obj.price
        print(f'class {self.class_obj} has new student {self.name} who paid tuition of {class_obj.course_obj.price}')
     
    def punch_card(self):
         pass
    def pay_tuition(self, balance, class_obj):
        print(f'student{self.name} paid tuition to class {self.class_obj}, remaining balance of {self.balance} on {datetime.datetime.now()}')
    
    
'''class Course:
    def __init__(self, name, outline, price):
        self.name = name 
        self.outline = outline
        self.price = price
        print(f'创建了{self.name} 学费是{self.price}')'''
        

class Staff:
    def __init__(self,name, balance, position, school_obj,salary) -> None:
        self.name = name
        self.balance = balance
        self. position = position
        self.salary = salary
        self. school_obj = school_obj
    def punch_card(self, name, school_obj):
        pass
    
        
class Teacher(Staff):
    def __init__(self, name, balance, position, school_obj, salary, course) -> None:
        super().__init__(name, balance, position, school_obj, salary)
        self.course = course
    
    def teach_class(self,class_obj, day): 
        print(f'{self.name} Teacher is at {class_obj} teaching for days')


# 实例化开始
# 创建校区
headquarter = School('老男孩IT教育集团', "北京昌平")
luffy = Branch('虹桥校区', "上海虹桥", headquarter)
school1 = Branch('张江校区', "上海张江",headquarter)
school2 = Branch('虹桥校区', "上海虹桥",headquarter)
# 创建课程
py_course = Course('Python',None, 300)
linux_course = Course('Linux',None, 1980)
test_course = Course('Test',None, 1980)
# 创建班级
py_24 = Class(24,headquarter,py_course)
py_12 = Class(12,school1,py_course)
linux_class = Class(24,school2,linux_course)
linux_class = Class(24,headquarter,linux_course)
# 创建 学员 老师 员工
s1 = Staff('Alex',0,"cook",luffy, 4000)
s1 = Staff('Todd',0,"CEO",headquarter, 60000)

t1 = Teacher('日天', 0, "讲师",headquarter, 4000, py_course)
t1 = Teacher('Egon', 0, "讲师",school2, 4000, linux_course)
t1 = Teacher('Piggy', 0, "学科负责人",school1, 6000, test_course)

stu1 = Student('1',py_12,1000)
stu2 = Student('2',py_24,3000)
stu3 = Student('3',linux_class,5000)


# 调用：
print(headquarter.balance)
stu2.pay_tuition(3000, py_24)
stu3.pay_tuition(5000,linux_class)

print(headquarter.branches)
headquarter.count_total_revenue()