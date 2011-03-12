#replceAll
newstring = 'ee'
subject = 'abbbbadddd'
reobj = re.compile('a')
result,number = reobj.subn(newstring, subject)

regex = "a"
reobj = re.compile(regex)
result = reobj.split(subject)


#re.search(regex, subject): match: have start, end, group
#re.match(regex, subject)
#re.finall(regex, subject) finditer(regex, subject)
#also can use reobj.search(subject) replace to use re.search(regex, subject)

#使用替换函数，能够实现对匹配的不同内容实现不同的替换方式 
def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'
 
 
re.sub('-{1,2}', dashrepl, 'pro----gram-files')
#结果为 'pro--gram files'