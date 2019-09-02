import qrcode
import zxing


# 生成二维码
# data = "{姓名：杨浩成}"
# dataEn = "https://www.baidu.com"
#
# img = qrcode.make(data=dataEn)
# img.show()



# 解析二维码

reader = zxing.BarCodeReader()

decode = reader.decode("testEn.jpg")

print(decode.parsed)