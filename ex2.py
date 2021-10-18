import re

txt = '''
TÊN KHOA FILE DS TÀI KHOẢN SV USER SỐ LỚP USER CÓ QUYỀN XEM VÀ SỬA SỐ ĐT THẦY CÔ GIÁO VỤ
Khoa Kinh Tế và Quản lý XD Link file 3246 119 thunm@nuce.edu.vn
yenlh@nuce.edu.vn 0912 052 626
0989 097 730
Khoa XD CT Biển Link file 236 17 duongntt@nuce.edu.vn
hauttc@nuce.edu.vn 0917 967 276
0386 293 499
Khoa XD Cầu Đường Link file 1605 76 hiendtt2@nuce.edu.vn
vanltt1@nuce.edu.vn 0382 728 986
0932 329 166
Khoa XD CTrình Thủy Link file 582 40 dunglm@nuce.edu.vn
vanltt2@nuce.edu.vn 0983 588 320
0988 425 812
Ban đào tạo KS Chất Lượnng Cao Link file 346 22 ngapth@nuce.edu.vn
tuanhv@nuce.edu.vn
vanttb@nuce.edu.vn 0912 463 277
0983 910 375
0982 419 265
Khoa KT Môi Trường Link file 1555 80 minhtn@nuce.edu.vn
yennth@nuce.edu.vn 0386 428 888
0976 832 354
Khoa Kiến Trúc và Quy hoạch Link file 2799 103 hoangnh@nuce.edu.vn
leht@nuce.edu.vn 0988 542 626
0982 484 579
Khoa Cơ khí XD Link file 652 30 hattt@nuce.edu.vn
huongntt3@nuce.edu.vn 0988 238 299
0976 316 696
Khoa CN Thông Tin Link file 1529 51 binhct2@nuce.edu.vn
hongvth@nuce.edu.vn 0983 239 189
0987 260 155
Khoa Vật Liệu XD Link file 417 21 anhntv@nuce.edu.vn
phuongdn@nuce.edu.vn 0979 892 805
0982 112 852
Khoa XD DD và CN Link file 4234 154 huongmtx@nuce.edu.vn
ngocntk@nuce.edu.vn
quyenma@nuce.edu.vn 0934 381 295
0986 558 193
0915 217 989
Khoa Đào tạo Quốc tế Link file 7 2 anhbtl@nuce.edu.vn
linhcn@nuce.edu.vn 0975 728 663
0975 737 464
'''
x = re.findall('[0-9]{4} +[0-9]{3} +[0-9]{3}', txt)
print(x)
y = re.findall('[0-9]{1,4} +[0-9]{1,3} +[0-9]{1,3}', txt)
print(y)
emails = re.findall('[a-z]+@[a-z]+.[a-z]', txt)
print(emails)