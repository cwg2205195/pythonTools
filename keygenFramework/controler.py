'''
负责数据传递，把界面数据传给 DataHandling 处理，
并把返回的结果传递给 界面 ，显示结果。
'''

from DataHandling import DataProcessor

#数据从GUI 传递到 模型层，然后从模型层返回给 GUI显示
class Dictator():
    def __init__(self,data):
        self.processData(data)

    #把前端数据传递给后端处理
    def processData(self,data):
        self.dataProcessor= DataProcessor(data)
        
    
    #从后端取数据回显
    def feedbackData(self):
        #转为字符串返回
        return self.dataProcessor.data