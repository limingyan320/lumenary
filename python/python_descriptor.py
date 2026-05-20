# 本例可以直观说明简单decorator + 描述符descriptor
# 同时，也说明了@property的用法：存实例方法后，使用属性访问的方式直接调用方法
class MyProperty:
    def __init__(self,fget):
        print(f"__init__将函数{fget.__name__}存起来")
        self.fget = fget

    def __get__(self,instance,owner): # 三个签名是描述符的固定写法，只能这么写
        print(f"__get__有人访问我，对象名 instance = {instance}")
        if instance is None: # 类访问
            return self
        print(f"__get__调用存起来的函数，传instance 当作 self")
        return self.fget(instance)



class Foo:
    first = "Alice"
    last = "Wang"

    @MyProperty
    def full_name(self):
        print(f"full_name 函数正在执行,self = {self}")
        return self.first + self.last



# 这是真正的python property的定义，当然也不是完整的版本
class property:
  def __init__(self, fget=None, fset=None, fdel=None):  # 可以传 3 个函数
      self.fget = fget
      self.fset = fset
      self.fdel = fdel
  def __get__(self, instance, owner):  # 读：调 fget
      return self.fget(instance)
  def __set__(self, instance, value):  # 写：调 fset
      self.fset(instance, value)
  def __delete__(self, instance):       # 删：调 fdel
      self.fdel(instance)

  # ★ 关键 ★
  def setter(self, fset):
      # 返回一个新的 property，把 fget 保留，fset 换成新的
      return property(self.fget, fset, self.fdel)
  def getter(self, fget):
      return property(fget, self.fset, self.fdel)
  def deleter(self, fdel):
      return property(self.fget, self.fset, fdel)


if __name__ == "__main__":
    f = Foo()
    # print(f"验证:{type(f.full_name)}")
    result = f.full_name
    print(f"最终值: {result}")



