# 设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
# 读取文件，生产数据对象

from data_define import Record
import json

class FileReader:

    def data_read(self):
        pass

class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def data_read(self) -> list[Record]:


        file_data = open(self.path, "r", encoding = "UTF-8")

        record_list: list[Record] = []
        for line in file_data.readlines():
            line = line.strip()  # 清空"\n"
            if not line:
                continue  # 跳过空行
            data_list = line.split(",")
            if len(data_list) >= 4:  # 确保数据有4个字段
                record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
                record_list.append(record)
        file_data.close()
        return record_list

class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def data_read(self) -> list[Record]:
        file_data = open(self.path, "r", encoding = "UTF-8")

        record_list: list[Record] =[]
        for line in file_data.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
            record_list.append(record)
        file_data.close()
        return record_list



if __name__ == "__main__":
    text_data = TextFileReader(r"D:\PythonProject\数据分析案例数据\2011年1月销售数据.txt")
    list1= text_data.data_read()
    json_data = JsonFileReader(r"D:\PythonProject\数据分析案例数据\2011年2月销售数据JSON.txt")
    list2 = json_data.data_read()

    for l in list1:
        print(l)

    for l in list2:
        print(l)