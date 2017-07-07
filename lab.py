# -*- coding: utf-8 -*-
from my_module import fun1, fun2
from datetime import datetime
from contextlib import contextmanager
import numbers
import ujson
from datetime import datetime, timedelta
import traceback
import sys
import codecs
import time
import string
import requests
import ujson
from my_module import*
import pprint
import uuid
from bson import ObjectId, errors

p = pprint.PrettyPrinter().pprint

class MyClass(object):
    @classmethod
    def _fun1(cls):
        print 'from cfun1'

    # just convention
    def _fun1(self):
        print 'from _fun1'

    # name mangle
    def __fun2(self):
        print 'from __fun2'

o = MyClass()
# p(dir(o))
o._fun1()
#  o.__fun2()
o._MyClass__fun2()


# f = MyClass._fun1
# f2 = o._fun1
# f(o)
# f2()
# MyClass._fun1()
print MyClass._fun1 is o._fun1

print MyClass._fun1
print o._fun1

# fc = MyClass._cfun1
# f = MyClass.__fun2





# a = {u'weight': u'1', u'sender_name': u'aqq', u'declared_value': u'1', u'product_url': u'', u'sender_phone_number': u'123456789', u'product_count': u'2', u'receiver_address': u'hl', u'receiver_country': u'Germany', u'sender_address': u'aqq', u'receiver_city': u'hl', u'sender_city': u'aqq', u'user_defined': u'', u'receiver_address_local': u'', u'receiver_province_local': u'', u'receiver_province': u'hl', u'receiver_city_local': u'', u'collection_option': u'1', u'receiver_country_local': u'', u'receiver_name_local': u'', u'registered': u'true', u'product_detailed_name': u'other', u'wish_transaction_value': u'', u'product_name_chinese': u'\u4e1c\u897f', u'product_country_of_origin': u'china', u'wish_transaction_id': u'592f762aa07ccd5542cae070', u'sender_address_book': u'0', u'has_battery': u'', u'package_type': u'1', u'receiver_zip_code': u'20044', u'sender_province': u'aqq', u'receiver_name': u'hlcao', u'receiver_phone_number': u'123455'}
# p = pprint.PrettyPrinter()
# p.pprint(a)
 
#     n = "n is a nubmer"
#     # raise "some errror"
#     print n
# except Exception as e:
#     print 'exp handling...'
#     raise 'New Error'
# finally:
#     print "finnally procesing.."


# print " s".strip().lower() == "S".lower()


# l = [1, 2, 3]
# l.append(6)
# print list.__class__


# merchant_url = "https://merchant.wish.com"
 
# url = merchant_url + \
#            '/api/v1/wishpost/get_orders_by_transaction_ids?key=JHBia2RmMiQxMDAkb0RRRzRIeVAwZnBmSzZXVWNvNFJvZyRhL0tERkxCbEtNaXZQdi55TDRoS2I0YWJjZVk='

# headers = {
#     'content-type': 'application/json',
# }
# transaction_ids = ['590ad53a676951413cb683ee']

# # payload = ','.join(transaction_ids)

# payload = '590ad53a676951413cb683ee'

# print payload
# resp = requests.post(
#     url=url,
#     headers=headers,
#     data=payload,
#     timeout=60
# )

 
# # 200
# print ujson.loads(resp._content)







# t_jsn = ujson.dumps(temp)
# print(t_jsn)
 

# === lambda
    # string = "ab cd ef"
    # lbd = lambda s: "--".join(s.split())
    # lbd(string)
# === end

# print(len(s.ljust(30))

#  === it is pretty coll
    # def pp_log(log_str, tag=""):
    #     @contextmanager
    #     def print_log(tag):
    #         hr = "-------" + tag + "----------"
    #         print(hr)
    #         yield
    #         print(hr)

    #     with print_log(tag):
    #         print(log_str)
#  === end

# ==== magic trick
    # @contextmanager
    # def funny_wrap():
    #     hr = "================"
    #     print(hr)
    #     yield
    #     print(hr)
# ==== end

# with funny_wrap():
#     print("notice!")

# d = datetime.strptime('2012-03-01T10:00:00.000Z','%Y-%m-%dT%H:%M:%S.%fZ')
# print(d)

# =====  basic function
# class Parent(object):
#     tag1 = "tag1"
#     tag2 = "tag2"


# class Son(Parent):
#     tag3 = "tag3"
#     def __init__(self, *args, **kwargs):
#         print(args)
#         print(kwargs)

#     # def play(self, str):
#     #     print(str)

#     #  no overloading, just overwrite
#     def play(self, str, str2):
#         print(str)
#         print(str2)
    


# Son(name='hlcao', age = 31)
# s = Son({'name':'hlcao', 'age': 31})
# # s.play(str="good dog")
# s.play(str="good dog", str2="good taste")
# print(isinstance([], list))

# ==== end

# === built in method
    # class MyClass:
    #     meta = {"name": "hlcao"}
    #     pass

    # print(MyClass.__dict__)
    # print(MyClass.__dict__["meta"])
    # print(dir(MyClass))
    # obj = MyClass()
    # print(obj.__class__)
# ===

#  add a comment
# test

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




# t_now = datetime(2017, 6, 1)
# print(t_now)
# t_o = datetime(1970, 1, 1)
# print( (t_now - t_o).total_seconds() )
# p = {"name": 'hlcao'}



# try:
#     raise Exception("something wrong")
# except Exception as e:
#     print(e.message)
#     print(traceback.format_exc())
    # exc_info = sys.exc_info()
    # job_error = exc_info[1]
    # trace_back = exc_info[2]
    # print(job_error)
    # print(traceback.format_exc())
    # print("----")
    # exc_type, exc_value, exc_traceback = sys.exc_info()
    # print "*** print_tb:"
    # traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    # print "*** print_exception:"
    # traceback.print_exception(exc_type, exc_value, exc_traceback,
    #                           limit=2, file=sys.stdout)
    # print "*** print_exc:"
    # traceback.print_exc()
    # print "--- end --- "
    # traceback.print_exc()
