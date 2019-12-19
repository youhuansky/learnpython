#条件判断语句，if语句
#简化写法（一行）
if False :print("123456")

#代码块写法,":"后面不跟随代码，换行缩进后写先要执行的代码，只要有缩进，就是if控制的范围
#随进可以是tab也可以是4个空格
s = 100
if s < 100 :
    print("qwert")
    print("afds")
    print("asdfghj")
elif s > 100 :
    print("zxcvzxcvxzvz")
else :
    print("fg bureb")

while s < 105 :
    s +=1
    print("test")
else :
    print("test2")
