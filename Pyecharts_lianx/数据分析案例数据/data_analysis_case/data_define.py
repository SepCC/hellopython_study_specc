# 设计一个类，可以完成数据的封装

class Record:

    def __init__(self, date, order_id, money, province):
        self.date= date           # 定义日期数据
        self.order_id = order_id  # 定义订单数据
        self.money = money        # 定义金额数据
        self.province = province  # 定义省份数据

    # 调用字符串方法，输出字符串对象
    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"
