"""
面向对象，数据分析案例， 主业务逻辑代码

实现步骤：
1. 设计一个类，可以完成数据的封装
2. 设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3. 读取文件，生产数据对象
4. 进行数据需求的逻辑计算（计算每一天的销售额）
5. 通过PyEcharts进行图形绘制
"""

from data_define import Record
from file_define import TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import InitOpts, TitleOpts, LabelOpts
from pyecharts.globals import ThemeType


text_data = TextFileReader(r"D:\PythonProject\数据分析案例数据\2011年1月销售数据.txt")
jan_data: list[Record] = text_data.data_read()

json_data = JsonFileReader(r"D:\PythonProject\数据分析案例数据\2011年2月销售数据JSON.txt")
feb_data: list[Record] = json_data.data_read()

# 将两个月的销售数据进行合并
all_data: list[Record] = jan_data + feb_data

# 数据计算，转换为 dict 类型，日销售额求和
all_data_dict = {}
for record in all_data:
    if record.date in all_data_dict.keys():
        all_data_dict[record.date] += record.money
    else:
        all_data_dict[record.date] = record.money

# 可视化图表开发
daily_sales_bar = Bar(init_opts = InitOpts(theme = ThemeType.LIGHT))

daily_sales_bar.add_xaxis(list(all_data_dict.keys()))  # 添加 X 轴数据
daily_sales_bar.add_yaxis(
    "销售额",
    list(all_data_dict.values()),
    label_opts = LabelOpts(is_show = False)
)  # 添加 Y 轴数据

daily_sales_bar.set_global_opts(
    title_opts = TitleOpts(
        title = "每日销售额",
        pos_left = "center",
        pos_bottom = "1%")
    )

daily_sales_bar.render("每日销售额.html")
