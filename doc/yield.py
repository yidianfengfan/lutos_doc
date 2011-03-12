"""
常看到别人使用或讨论yield语法,能搜到的中文解释却不多,今天决心搞定yield,把暂时的理解贴到这里.
 
预备概念: 叠代器(iterator)
使用场合: 生成器(constructor)
yield用法: 递归调用
 
1. iterator
叠代器最简单例子应该是数组下标了，且看下面的c++代码：
int array[10];
for ( int i = 0; i < 10; i++ )
    printf("%d ", array[i]);
叠代器工作在一个容器里(array[10])，它按一定顺序(i++)从容器里取出值(array[i])并进行操作(printf("%d ", array[i])。
 
上面的代码翻译成python：
array = [i for i in range(10)]
for i in array:
    print i,

首先，array作为一个list是个容器，其次list这个内建类型有默认的next行为，python发现这些之后采取的秘密的没被各位看到的动作是：拿出array这丫容器的叠代器，从里面next一下把值给i供for循环主体处置，for把这个值print了。
 
现在的问题是数据可以做容器叠代，代码可以吗？
 
2. constructor
怎么把函数变成constructor？  在函数体里有yield就行了！
def gen():
    print 'enter'
    yield 1
    print 'next'
    yield 2
    print 'next again'

for i in gen():
    print i
各位！python看到gen函数里出现yield，知道可以用next了，问题是怎么对代码这个容器玩next？
从容器里拿到iterator的时候它还什么也不是，处在容器入口处，对于数组来说就是下标为-1的地方，对于函数来说就是函数入口嘛事没干，但是万事俱备就欠next。
开始for i in g，next让itreator爬行到yield语句存在的地方并返回值,
再次next就再爬到下一个yield语句存在的地方并返回值,依次这样直到函数返回(容器尽头)。
您一定看出来上面代码的输出是：
enter
1
next
2
next again
 
3. 使用yield
yield的代码叠代能力不但能打断函数执行还能记下断点处的数据，下次next书接上回，
这正是递归函数需要的。
例如中序遍历二叉树：
(应该是David Mertz写的)
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x
        yield t.label
        for x in inorder(t.right):
            yield x
for n in inorder(tree)
    print n

"""



#生成全排列
def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i+1:]
            for p in perm(rest, n-1):
                yield v + p
 
#生成组合
def comb(items, n=None):
    if n is None:
        n = len(items)    
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[i+1:]
            for c in comb(rest, n-1):
                yield v + c
 
a = perm('abc')
for b in a:
    print b
    break
print '-'*20
for b in a:
    print b 