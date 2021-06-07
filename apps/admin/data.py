
from random import randint


class Data:
    def __init__(self, title=None, values=None, xAxis=None, legend=None, unit=None, special=None):
        self.title = title  # 标题
        self.values = values  # 图表数据
        self.xAxis = xAxis  # 图例名称【一般折线，柱形图需要】
        self.legend = legend  # 横坐标数据【一般折线，柱形图需要】
        self.unit = unit  # 单位【可选】
        self.special = special  # 特殊图标保留参数


class SourceDataDemo:

    @property
    def pie_doughnut(self):
        data = Data()
        data.title = '项目申报数据'
        data.values = [
            {'name': '申请中', 'value': 335},
            {'name': '审核中', 'value': 310},
            {'name': '开展中', 'value': 234},

        ]
        data.legend = [key['name'] for key in data.values]
        data.unit = '项目数'
        return data



class SourceData(SourceDataDemo):
    ...
