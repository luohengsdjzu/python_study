# def auth(func, db_type):
#     def wrapper(*args, **kwargs):
#         if db_type == 'file':
#             user = input('your name:')
#             passwd = input('your password:')
#             if user == 'egon' and passwd == '123':
#                 print('登录成功')
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print('登录失败')
#         elif db_type == 'mysql':
#             print('mysql认证')
#             func(*args, **kwargs)
#         elif db_type == 'ldap':
#             print('ldap认证')
#             func(*args, **kwargs)
#         else:
#             print('无效认证')
#
#     return wrapper
#
#
# def index(x, y):
#     print('index->%s,%s' % (x, y))
#
#
# file=auth(index,'file')
# db = auth(index, 'mysql')
# ldap = auth(index, 'ldap')
#
# # file(5,6)
# # db(5,6)
# ldap(5, 6)



# 语法糖
def auth(db_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            if db_type == 'file':
                user = input('your name:')
                passwd = input('your password:')
                if user == 'egon' and passwd == '123':
                    print('登录成功')
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('登录失败')
            elif db_type == 'mysql':
                print('mysql认证')
                func(*args, **kwargs)
            elif db_type == 'ldap':
                print('ldap认证')
                func(*args, **kwargs)
            else:
                print('无效认证')

        return wrapper
    return deco


# deco = auth('file')
# @deco
# def index(x, y):
#     print('index->%s,%s' % (x, y))
# index(5,6)


# deco = auth('mysql')
# @deco
# def index(x, y):
#     print('index->%s,%s' % (x, y))
# index(5,6)

@auth('file')
def index(x, y):
    print('index->%s,%s' % (x, y))


index(5,6)


# 有参装饰器模板
def 有参装饰器(x,y,z):
    def outter(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return outter

@有参装饰器(x=1,y=2,z=3)
def 被装饰对象():
    pass

