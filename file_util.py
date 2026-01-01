"""
文件处理相关的工具模块
"""

def print_file_info(file_name):
    """
    功能是将给定路径的文件内容进行读取
    :param file_name:  需要被读取的文件路径
    :return:  None
    """
    f = None  # 提前初始化变量
    try:
        f = open(file_name, 'r', encoding='utf-8')
        content = f.read()
        print("文件的内容如下：")
        print(content)

    except Exception as e:
        print(f"程序出现异常，报错信息是：{e}")
    finally:
        if f is not None:
            f.close()

# 测试
if __name__ == '__main__':
    print_file_info("C:/Users/15755/Desktop/b.txt")


def append_to_file(file_name, date):
    """
    功能是将指定的数据追加到指定的文件中
    :param file_name:  需要追加数据的文件路径
    :param date:  追加的数据
    :return:  None
    """
    f = open(file_name, 'a', encoding='utf-8')
    f.write(date)
    f.write("\n")
    f.close()
