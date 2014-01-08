# coding:utf-8

# 继承.


# 父类 学校成员类.
class SchoolMember:
    '''学校成员类.'''
    # 构造函数.
    def __init__(self, name, age):
        # 初始化成员姓名.
        self.name = name;
        # 初始化成员年龄.
        self.age = age;
        # 调试输出.
        print ('(初始化 学校成员类: %s)' % self.name);
    # 类里面定义的方法.
    def tell(self):
        '''Tell my details.'''
        print ('姓名:"%s" 年龄:"%s"' % (self.name, self.age));

        
# 教师类 继承 学校成员类 
class Teacher(SchoolMember):
    '''教师类.'''
    # 构造函数.
    def __init__(self, name, age, salary):
        # 调用 父类的构造函数进行初始化.
        SchoolMember.__init__(self, name, age);
        # 初始化 薪资.
        self.salary = salary;
        # 调试输出.
        print ('(初始化 教师类: %s)' % self.name);

    def tell(self):
        # 调用 父类的 tell 方法.
        SchoolMember.tell(self);
        # 输出自己的特有的信息.
        print ('薪水: "%d"' % self.salary);
    
    # 对对象使用print语句或是使用str()的时候调用。
    def __str__(self):
        return "教师：" + self.name + " 年龄：" + str(self.age) + " 薪水：" + str(self.salary);
        
# 学生类 继承 学校成员类
class Student(SchoolMember):
    '''学生类.'''
    # 构造函数.
    def __init__(self, name, age, marks):
        # 调用 父类的构造函数进行初始化.
        SchoolMember.__init__(self, name, age);
        # 初始化 marks.
        self.marks = marks;
        # 调试输出.
        print ('(Initialized Student: %s)' % self.name);

    def tell(self):
        # 调用 父类的 tell 方法.
        SchoolMember.tell(self);
        # 输出自己的特有的信息.
        print ('Marks: "%d"' % self.marks);

    # 对对象使用print语句或是使用str()的时候调用。
    def __str__(self):
        return "学生：" + self.name + " 年龄：" + str(self.age) + " Marks：" + str(self.marks);


# 主程序执行开始.
t = Teacher('张三', 40, 30000);
s = Student('李四', 22, 75);

# 打印一空行.
print ();


members = [t, s];
for member in members:
    # works for both Teachers and Students
    member.tell();
    print("对象信息：", member);


