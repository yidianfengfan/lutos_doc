#python中函数的默认值只会被执行一次，(和静态变量一样，静态变量初始化也是被执行一次。）这就是她们的共同点。
def f(a, L=[]):
    L.append(a)
    return L
 
print f(1)
print f(2)
print f(3)
print f(4,['x'])
print f(5)
###
[1]
[1, 2]
[1, 2, 3]
['x', 4]
[1, 2, 3, 5]
###
