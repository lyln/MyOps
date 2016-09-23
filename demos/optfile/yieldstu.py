# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/7 16:00

# yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。

def createGenerator() :
        mylist = range(3)
        for i in mylist :
           yield i*i
mygenerator = createGenerator()
print mygenerator

for i in mygenerator:
    print i

# 这个函数会返回一大批你只需要读一次的值.
# 为了精通 yield ,你必须要理解：当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象，这有点蹊跷不是吗。
# 那么，函数内的代码什么时候执行呢？当你使用for进行迭代的时候.
# 现在到了关键点了！
# 第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值. 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。