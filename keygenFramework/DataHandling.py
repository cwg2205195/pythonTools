'''
数据处理、模型定义
'''
import base64


#数据数据类
class DataProcessor():
    def __init__(self,data):
        self.data = data        #注意，这里是原始数据，字符串类，使用需要自己转换
        self.workInterface()
    
    def encBase64(self,source):
        return base64.b64encode(source)
    
    def decBase64(self,source):
        return base64.b64decode(source)
    
    #处理由winhex 直接粘贴过来的数据
    def handleWinHexData(self):
        if type(self.data)  != str:
            return 
        dat=self.data
        dat= dat[dat.find('{')+1:dat.rfind('}')]
        dat = dat.split(',')
        self.data=dat

    #implement your own keygen function
    #每个 Keygen 实现不同的处理函数，处理 data 即可 。
    def workInterface(self):
        #简单的计算 base64 
        #self.data=self.encBase64(bytes(self.data,encoding='utf-8',errors='ignore'))
        self.handleWinHexData()