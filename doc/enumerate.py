#python enumerate
#参数为可遍历的变量，如 字符串，列表等；返回值为enumerate类：
#
#line 是个 string 包含 0 和 1，要把1都找出来：

#方法一
print "start..."
def read_line(line):
    sample = {}
    n = len(line)
    for i in range(n):
        if line[i]!='0':
            sample[i] = int(line[i])
    return sample
 
#方法二
def xread_line(line):
    return((idx,int(val)) for idx, val in enumerate(line) if val != '0')
 
print read_line('0001110101')
print list(xread_line('0001110101'))
print "finish..."
