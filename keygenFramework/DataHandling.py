'''
数据处理、模型定义
'''
import base64
import hashlib
import hmac

#数据数据类
class DataProcessor():
    def __init__(self,data):
        self.data = data        #注意，这里是原始数据，字符串类，使用需要自己转换
        self.workInterface()
    
    #base64 编码
    def encBase64(self,source):
        return base64.b64encode(source)
    
    #base64 解码
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

    #string to hex string ,decode every two charaters to one byte
    #字符串转 hex 流，每2位字符转 1 字节 ，ie : "12ab" -> "0x12,0xab", 返回的是列表
    def strToHexStream(self,source):
        #长度校验
        if len(source) %2 !=0 :
            return None 
        #数据类型校验，只能从 str 转为 bytes 或者 list？
        if type(source) != str:
            return None 
        l=len(source)
        i = 0
        ret = []
        while i < l :
            b = source[i:i+2]   #取出两个字符
            ret.append(int(bytes(b,encoding='utf-8',errors='ignore'),16))   #转为16进制数并加入到列表
            i+=2
        return ret
    
    #hex string decode to string,decode every two characters to one character
    #hex流转字符串，每两个hex字符转一个 字符， ie : "454647" -> "0,1,2",返回列表
    def hexstrToString(self,source):
        #长度校验
        if len(source) %2 !=0 :
            return None
        #数据类型校验 
        if type(source) != str:
            return None 
        l=len(source)
        i = 0
        ret = []
        while i < l :
            b = source[i:i+2]   #取出两个字符
            ret.append(chr(int(bytes(b,encoding='utf-8',errors='ignore'),16)))   #转为16进制数并加入到列表
            i+=2
        return ret

    #简化的python byte ，用 utf-8 编码的转换
    def getBytes(self,source):
        return bytes(source,encoding='utf-8',errors='ignore')

    #简化的python string， utf-8 编码
    def getString(self,source):
        if type(source) != str:
            return str(source,encoding='utf-8',errors='ignore')
        return source

    hashAlgs={0:'sha1',1:'sha224',2:'sha256',3:'sha384',4:'sha512',5:'blake2b',6:'md5',
    7:'sha3_384',8:'sha3_512',9:'shake_128',10:'shake_256',11:'sha3_224',12:'sha3_256',
    13:'sha3_384',14:'sha3_512',15:'shake_128',16:'blake2s'}

    #HMAC 计算函数
    def getHMAC(self,msg,key,alg):
        return hmac.new(self.getBytes(key),self.getBytes(msg),alg).hexdigest()
    
    #Hash 计算函数
    def getHash(self,msg,alg):
        pass 
    

    #implement your own keygen function
    #每个 Keygen 实现不同的处理函数，处理 data 即可 。
    def workInterface(self):
        #简单的计算 base64 
        #self.data=self.encBase64(bytes(self.data,encoding='utf-8',errors='ignore'))
        self.data= self.getString(self.getHMAC(self.data,'123456',self.hashAlgs[0]))
        '''dat=self.hexstrToString(self.data)
        print(dat)
        self.data="".join(dat)'''