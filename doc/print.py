strHello = "the length of (%s) is %d" %('Hello World',len('Hello World'))
print strHello
#输出果：the length of (Hello World) is 11

nHex = 0x20
#%x --- hex 十六进制
#%d --- dec 十进制
#%d --- oct 八进制
print "nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex)

#浮点数的格式化，精度、度和
#width = 10,precise = 3,align = left
print "PI = %10.3f" % math.pi
#width = 10,precise = 3,align = rigth
print "PI = %-10.3f" % math.pi
#前面填充字符
print "PI = %06d" % int(math.pi)

#print 会自动在行末加上回车,如果不需回车，只需在print语句的结尾添加一个逗号”,“，就可以改变它的行为。
print "sssgsg",
sys.stdout.write("输出的字串")