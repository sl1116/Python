#hàm findall của regex. syntax = re.findall()
#ex

import re

txt = '''
   abc seven deadly sins
'''
x = re.findall("[a-n]", txt)
print(x)
#Dòng code trên cho phép t tìm thấy cả các chữ in thường bắt đầu từ a và kết thúc là n có trong đoạn txt, sau đó in ra 1 list.
y = re.findall("[abc]", txt)
print(y)
#dòng code trên cho phép ta tìm tất cả các tổ hợp chữ có 1 trong 3 chữ abc, hoặc cả 3 chữ 

z = re.findall("[^a-n]", txt)
print(z)
#In ra màn hình tất cả các kí tự bắt đầu từ m đến hết bảng chữ cái có trong txt, in ra cả các dấu phẩY, trừ, cộng...