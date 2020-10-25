
'''
变量只能由字母（大小写敏感）、数字和下划线组成，且不能以数字开头
用等号赋值。赋值就是把值绑定或重新绑定到变量上
变量没有默认值，在使用前都必须赋值，否则会报错
'''

a = 2
b = a + 3
b = 2 * (3 + 5) - 9 / 4
c1 = 2 ** 5 + 9 // 4
_f2 = 16 % 5

print(a)
print(b)
print(c1)
print("sum =", a + b + c1)
print("-"*30)

# 注意类型的匹配
# x = "2020"
# print(x+1)

# int 与 float的区别
print("a =", a, ", type =", type(a))
print("b =", b, ", type =", type(b))
