from my_module import fun1, fun2

# === more on yield
    # def funny_gen(count):
    #     for i in range(count):
    #         print("start to count.." + str(i))
    #         yield i
    #     yield "hey there, i'm also yield string"
    #     print("count done!")
    #     return 

    # for val in funny_gen(3):
    #     print(val)
# === end

#=== scope  ....
    # class FunClass:
    #     status = 5
    #     def play(self):
    #         # local variable
    #         status = 1


    # fun_obj = FunClass()
    # fun_obj.play()
    # print(FunClass.status)
    # print(fun_obj.status)
#=== end

# === dict comprehension syntax 
    # d = {key: value for (key, value) in iterable} 

    # def key_value_gen(k):
    #     yield chr(k+65)
    #     yield chr((k+13)%26+65)

    # for v in key_value_gen(2):
    #     print(v)

    # d = dict(map(key_value_gen, range(2)))
    # print(d)
# ===

# === getattr built-in
    # class FunClass(object):
    #     pass

    #     def __init__(self):
    #         self.category = 'toy'

    # fun_obj = FunClass()
    # fun_obj.tag = 'fun1'
    # print(getattr(fun_obj, 'tag'))
    # print(getattr(fun_obj, 'category'))
# === end

# === function play
    # def foo(key, *args, **kwargs):
    #     print(key)
    #     print(args)
    #     for v in args:
    #         print(v)
    #     print(kwargs)
    #     for key,value in kwargs.iteritems():
    #         print(key + " " + value) 

    # foo('hlcao', 'good', 'test', fav_color='red', fav_movie='bat man')
#  === end

# === with key word and "__enter__" and "__exit"
    # class MyClass(object):
    #     def __init__(self, msg):
    #         print("initing...")
    #         self.message = msg

    #     def __enter__(self):
    #         print("on enter..")
    #         #  must return an object as the ref of "as"
    #         return self

    #     def __exit__(self, type, value, trackback):
    #         print("on exit...")

    #     def tell(self):
    #         print("your message is:" + self.message)

    # with MyClass("my message") as my_obj:
    #     my_obj.tell()
#=== end

#===  super in multi-inheritence
    # class Parent(object):
    #     def __init__(self, name):
    #         super(Parent, self).__init__(name)
    #         print("... parent init called")
    #         self.name = name

    # class MixIn(object):
    #     def __init__(self, name):
    #         super(MixIn, self).__init__()
    #         print("... mixin int called")
    #         self.hidden_name = name

    # class Son(Parent, MixIn):
    #     def __init__(self, name):
    #         print("... son init called")
    #         super(Son, self).__init__(name)

    # son = Son("jack")
    # print(son.name)
#=== end

# === basic class definition
    # class MyClass(object):
    #     # class variable, shared by all
    #     cls_counter = 0
    #     def __init__(self, cnt = 1):
    #         # instance variable
    #         self.counter = cnt
    #         self._v = 1000

    #     def tell(self):
    #         print(self.counter)

    #     def verbos_tell(self):
    #         # must use self 
    #         # print("the counter is: " + tell())
    #         pass

    #     #  get only
    #     @property
    #     def v(self):
    #         return self._v

    #     @v.setter
    #     def v(self, new_val):
    #         print(".. in setter")
    #         self._v = new_val
            
    #     @v.deleter
    #     def v(self):
    #         print(".. in deleter")
    #         del self._v

    # my_obj = MyClass()

    # # setting object instace, only for this instance
    # my_obj.color = "red"
    # print(my_obj.color)

    # # see method type:
    # print(MyClass.tell)
    # print(my_obj.tell)
    # # use of bound method
    # trick_f = my_obj.tell
    # trick_f()
    # # use of unbuound method: pass the bound object!
    # MyClass.tell(my_obj)

    # # use of property
    # print(my_obj.v)
    # my_obj.v = 5600
    # print(my_obj.v)
    # print(my_obj._v)
    # del my_obj.v
    # # print(my_obj.v)
# === end

# === overwrite built-in function
    # def len(collection):
    #     print("my guess is 3")

    # col = [1, "string1"]
    # print(len(col))
# == end

# === call method with self or nor
    # def say_word(word):
    #     print("global word: " + word)

    # class MyClass:
    #     temp = 1
    #     def say_hello(self):
    #         say_word("hello")
    #         self.say_word("hello")

    #     def say_word(self, word):
    #         print(word)
# === end

# MyClass().say_hello()

# ==== for generator and yield
    # def createGenerator():
    #     mylist = range(3)
    #     for i in mylist:
    #         yield i*i

    # mygenerator = createGenerator() # create a generator
    # print(mygenerator) # mygenerator is an object!

    # for i in mygenerator:
    #     print(i)


    # print("try do it again..")
    # for i in mygenerator:
    #     print(i)
# === end

