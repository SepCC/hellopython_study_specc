"""
字符串相关的工具模块
"""


def str_reverse(s):
    """
    功能是将字符串完成反转操作
    :param s: 将被反转的字符串
    :return:  完成反转的字符串
    """
    reversed_str = s[::-1]
    print(reversed_str)
    return reversed_str

# 测试
if __name__ == '__main__':
    str_reverse('hello')


def substr(s, x, y):
    """
    功能是按照给定的下标完成给定字符串的切片
    :param s:  需要进行切片的字符串
    :param x:  切片的开始下标
    :param y:  步长
    :return:  完成的字符串的切片
    """
    substr_s = s[x::y]  # 序列切片语法
    print(substr_s)
    return substr_s
# 测试
if __name__ == '__main__':
    substr('helloworld',1,2)









