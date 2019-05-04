#dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    #list >>>> []
    #tuple >>>> ()
    #dist >>>> {}
d['Bob']
d['Bob']=33     #赋值
d.pop('Bob')    #删除

#set
    #无序和无重复元素的集合
s = set([1, 1, 2, 2, 3, 3])
s.add(4)    #添加
s.remove(4) #删除
    #两个set的交，并操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2     #交
s1 | s2     #并（相加）

###都是不可变元素