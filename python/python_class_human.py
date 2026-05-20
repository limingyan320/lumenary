from python_descriptor1 import MyProperty

class Human:
    def __init__(self,age):
        self.age = age

    @MyProperty
    def age(self):
        return self._age # 注意这里一定要用_age，否则会触发无限递归

    @age.setter
    def age(self,value):
        if not isinstance(value,int) or value < 0 or value > 150:
            raise ValueError(f"非法年龄:{value}")
        self._age = value

