import re

txt = '''
Phòng - Ban Khoa - Bộ môn Trung tâm Trường PTTH Tràng An Tổ chức đoàn thể Đào tạo Thống kê Thư viện Email Đề án tuyển sinh
 
Đại học Hoa Lư
TỔ CHỨC-HÀNH CHÍNH
TUYỂN SINH
ĐBCL-KĐCL
NCKH
CÔNG KHAI
HỢP TÁC QUỐC TẾ
LỊCH LÀM VIỆC
Thông tin tuyển sinh Trường Đại học Hoa Lư 2020
DANH SÁCH EMAIL
Tìm kiếm...
Tin tiêu điểm
Đề án tuyển sinh của Trường Đại học Hoa Lư năm 2020
Đề án tuyển sinh của Trường Đại học Hoa Lư năm 2020

Thứ Năm, 17:18 28/05/2020
Dự thảo đề án tuyển sinh năm 2020
Dự thảo đề án tuyển sinh năm 2020

Thứ Sáu, 15:04 20/03/2020
Lịch công tác tuần 10 năm 2020 (02/03/2020 - 08/03/2020)

Chủ Nhật, 12:13 01/03/2020
Lịch công tác tuần 9 năm 2020 (24/02/2020 - 01/03/2020)

Thứ Ba, 15:45 25/02/2020
HỘI NGHỊ QUÁN TRIỆT NỘI DUNG BÁO CÁO TỰ ĐÁNH GIÁ CHẤT LƯỢNG CƠ SỞ GIÁO DỤC
HỘI NGHỊ QUÁN TRIỆT NỘI DUNG BÁO CÁO TỰ ĐÁNH GIÁ CHẤT LƯỢNG CƠ SỞ GIÁO DỤC

Thứ Ba, 10:09 25/02/2020
ĐOÀN CHUYÊN GIA KHẢO SÁT SƠ BỘ PHỤC VỤ ĐÁNH GIÁ NGOÀI TRƯỜNG ĐẠI HỌC HOA LƯ
ĐOÀN CHUYÊN GIA KHẢO SÁT SƠ BỘ PHỤC VỤ ĐÁNH GIÁ NGOÀI TRƯỜNG ĐẠI HỌC HOA LƯ

Thứ Bảy, 21:51 15/02/2020
HỘI NGHỊ CÔNG TÁC TUYỂN SINH ĐẠI HỌC, CAO ĐẲNG NĂM 2019 VÀ THỰC TẬP NGHỀ NĂM HỌC 2018-2019, PHƯƠNG HƯỚNG, NHIỆM VỤ NĂM HỌC 2019-2020
HỘI NGHỊ CÔNG TÁC TUYỂN SINH ĐẠI HỌC, CAO ĐẲNG NĂM 2019 VÀ THỰC TẬP NGHỀ NĂM HỌC 2018-2019, PHƯƠNG HƯỚNG, NHIỆM VỤ NĂM HỌC 2019-2020

Thứ Tư, 14:31 08/01/2020
TẬP HUẤN NGHIỆP VỤ AN TOÀN PHÒNG CHÁY CHỮA CHÁY
TẬP HUẤN NGHIỆP VỤ AN TOÀN PHÒNG CHÁY CHỮA CHÁY

Chủ Nhật, 17:28 29/12/2019
Kỷ yếu hội thảo khoa học "Nâng cao hiệu quả đào tạo theo học chế tín chỉ ở Trường Đại học Hoa Lư"
Kỷ yếu hội thảo khoa học "Nâng cao hiệu quả đào tạo theo học chế tín chỉ ở Trường Đại học Hoa Lư"

Thứ Tư, 08:39 04/12/2019
HỘI THẢO “NÂNG CAO HIỆU QUẢ ĐÀO TẠO THEO HỌC CHẾ TÍN CHỈ Ở TRƯỜNG ĐẠI HỌC HOA LƯ”
HỘI THẢO “NÂNG CAO HIỆU QUẢ ĐÀO TẠO THEO HỌC CHẾ TÍN CHỈ Ở TRƯỜNG ĐẠI HỌC HOA LƯ”

Chủ Nhật, 13:49 01/12/2019
Danh sách email

Email chính thức trường: daihochoaluninhbinh@hluv.edu.vn

Stt

Họ và tên

Ngày sinh

Chức vụ

Địa chỉ mail

BAN GIÁM HIỆU

1

Vũ Văn Trường

01/01/1975

Hiệu trưởng

vvtruong@hluv.edu.vn

3

Nguyễn Mạnh Quỳnh

13/10/1970

P.Hiệu trưởng

nmquynh@hluv.edu.vn

3

Phạm Quang Huấn

15/03/1970

P.Hiệu trưởng

pqhuan@hluv.edu.vn

PHÒNG TỔ CHỨC - TỔNG HỢP

tochuc@hluv.edu.vn

1

Lương Duy Quyền

15/06/1981

Trưởng phòng

ldquyen@hluv.edu.vn

2

Hoàng Diệu Thúy

28/10/1976

P. Trưởng phòng

hdthuy@hluv.edu.vn

3

Bùi Duy Bình

25/08/1976

P. Trưởng phòng

bdbinh@hluv.edu.vn

4

Nguyễn Thanh Hòa

01/08/1983

Giảng viên

nthoa@hluv.edu.vn

5

Vũ Thị Loan

18/06/1990

Giảng viên

vtloan@hluv.edu.vn

6

Lã Thị Hương Giang

05/05/1978

Nhân viên

lthgiang@hluv.edu.vn

7

Nguyễn Thị Linh

05/07/1978

Nhân viên

ntlinh@hluv.edu.vn

PHÒNG TÀI VỤ

taivu@hluv.edu.vn

1

Bùi Thị Hải Yến

05/04/1969

Trưởng phòng

bthyen.tv@hluv.edu.vn

2

Trần Thị Tố Vân

03/06/1972

P.Trưởng phòng

tttvan@hluv.edu.vn

3

Phạm Văn Truyền

22/01/1970

P.Trưởng phòng

pvtruyen@hluv.edu.vn

4

Phạm Thị Oanh

02/04/1983

Giảng viên

ptoanh@hluv.edu.vn

5

Trần Thị Nam

22/10/1981

Kế toán viên TC

ttnam@hluv.edu.vn

6

Tống Thị Ngọc Lan

02/12/1981

Kế toán viên

ttnlan@hluv.edu.vn

7

Dương Thị Lan Hương

10/10/1983

Kế toán viên

dtlhuong@hluv.edu.vn

PHÒNG HÀNH CHÍNH - QUẢN TRỊ

hanhchinh@hluv.edu.vn

1

Trần Việt Hùng

22/02/1969

Trưởng phòng

tvhung@hluv.edu.vn

2

Đinh Thành Công

20/02/1985

P.Trưởng phòng

dtcong@hluv.edu.vn

3

Nguyễn Thị Thu Hoài

15/07/1977

P.Trưởng phòng

ntthoai@hluv.edu.vn

4

Hoàng Quốc Hùng

08/03/1983

Chuyên viên

hqhung@hluv.edu.vn

5

Nguyễn Thị Thùy Dung

02/04/1984

Nhân viên

nttdung@hluv.edu.vn

6

Nguyễn Văn Lĩnh

15/03/1980

Giáo viên THCS

nvlinh@hluv.edu.vn

7

Trần Thị Phương Thảo

30/01/1988

Nhân viên

ttpthao@hluv.edu.vn

8

Nguyễn Xuân Thuấn

22/10/1983

Nhân viên

nxthuan@hluv.edu.vn

9

Đặng Hữu Việt

11/06/1978

Nhân viên

dhviet@hluv.edu.vn

10

Vũ Thị Kiều Anh

20/12/1989

Nhân viên

vtkanh@hluv.edu.vn

11

Nguyễn Thị Vẻ

19/08/1983

Nhân viên

ntve@hluv.edu.vn

12

Phạm Xuân Giới

15/06/1959

Cán sự

pxgioi@hluv.edu.vn

13

Trần Gia Long

01/02/1981

Nhân viên

tglong@hluv.edu.vn

14

An Quang Hiển

03/02/1976

Nhân viên

aqhien@hluv.edu.vn

15

Lê Văn Hệ

26/01/1970

Nhân viên

lvhe@hluv.edu.vn

16

Nguyễn Văn Anh

22/02/1962

Nhân viên

nvanh@hluv.edu.vn

17

Hoàng Quý Thu

11/01/1969

Nhân viên

hqthu@hluv.edu.vn

18

Phạm Minh Tứ

03/01/1971

Nhân viên

pmtu@hluv.edu.vn

19

Nguyễn Quang Chiến

23/12/1967

Nhân viên

nqchien@hluv.edu.vn

20

Nguyễn Thị Chinh

15/10/1980

Nhân viên

ntchinh@hluv.edu.vn

21

Nguyễn Thị Tuyết

02/09/1982

Nhân viên

nttuyet@hluv.edu.vn

22

Đinh Thị Quyên

10/11/1996

Nhân viên

dtquyen@hluv.edu.vn

PHÒNG ĐÀO TẠO - QUẢN LÝ KHOA HỌC

daotao@hluv.edu.vn

1

Dương Trọng Luyện

18/02/1984

P.Trưởng phòng PT

dtluyen@hluv.edu.vn

2

Phan Thị Hồng Duyên

26/10/1970

P.Trưởng phòng

pthduyen@hluv.edu.vn

3

Hoàng Đức Hoan

15/07/1977

P.Trưởng phòng

hdhoan@hluv.edu.vn

4

Nguyễn Thị Minh Ngọc

29/01/1977

Giảng viên

ntmngoc@hluv.edu.vn

5

Nguyễn Thị Thảo

16/02/1984

Giảng viên

ntthao@hluv.edu.vn

6

Phùng Thị Thao

27/09/1986

Giảng viên

ptthao@hluv.edu.vn

7

Trương Ngọc Dương

22/04/1985

Giảng viên

tnduong@hluv.edu.vn

8

Phạm Văn Cường

28/01/1983

Giảng viên

pvcuong.pdt@hluv.edu.vn

9

Phạm Xuân Nguyện

22/03/1983

Giảng viên

pxnguyen@hluv.edu.vn

10

Vũ Thị Quyên

08/03/1986

Chuyên viên

vtquyen@hluv.edu.vn

PHÒNG KHẢO THÍ VÀ KIỂM ĐỊNH CHẤT LƯỢNG

khaothi@hluv.edu.vn

1

Nguyễn Hữu Tiến

30/07/1962

Trưởng phòng

nhtien@hluv.edu.vn

2

Lương Thị Hà

06/05/1975

P.Trưởng phòng

ltha@hluv.edu.vn

3

Nguyễn Anh Tuấn

10/05/1978

P.Trưởng phòng

natuan@hluv.edu.vn

4

Trương Tiến Phụng

22/12/1983

Giảng viên

ttphung@hluv.edu.vn

5

Lã Đăng Hiệp

08/04/1985

Giảng viên

ldhiep@hluv.edu.vn

6

Hoàng Thị Kim Thao

09/11/1987

Chuyên viên

htkthao@hluv.edu.vn

7

Đinh Thị Dương Quỳnh

02/02/1985

Chuyên viên

dtdquynh@hluv.edu.vn

9

Phạm Duy Hưng

08/01/1990

Chuyên viên

pdhung@hluv.edu.vn

8

Trần Thị Hà Tâm

10/12/1984

Chuyên viên

tthtam@hluv.edu.vn

PHÒNG CÔNG TÁC SINH VIÊN

congtacsinhvien@hluv.edu.vn

1

Phạm Xuân Lê Đồng

11/02/1976

Trưởng phòng

pxldong@hluv.edu.vn

2

Lê Hồng Phượng

26/10/1978

P.Trưởng phòng

lhphuong@hluv.edu.vn

3

Đinh Thị Liên

05/05/1987

P.Trưởng phòng

dtlien@hluv.edu.vn

4

Lâm Ngọc Cương

24/01/1991

Chuyên viên

lncuong@hluv.edu.vn

5

Trịnh Xuân Quỳnh

21/10/1986

Chuyên viên

txquynh@hluv.edu.vn

6

Ninh Tiến Nam

14/11/1987

Chuyên viên

ntnam@hluv.edu.vn

7

Phạm Thu Thủy

28/10/1985

Chuyên viên

ptthuy.ctsv@hluv.edu.vn

8

Vũ Thị Hà

27/08/1987

Chuyên viên

vtha@hluv.edu.vn

9

Trịnh Thị Hoài Thanh

17/12/1988

Chuyên viên

tththanh@hluv.edu.vn

KHOA XÃ HỘI - DU LỊCH

xahoidulich@hluv.edu.vn

1

Nguyễn Thị Phương

03/07/1973

P.Trưởng khoa PT

ntphuong@hluv.edu.vn

2

Nguyễn Thị Thu Giang

19/02/1977

P. Trưởng khoa

nttgiang@hluv.edu.vn

3

Trần Thị Huyền Phương

28/12/1975

Trưởng môn văn

tthphuong@hluv.edu.vn

4

Vũ Phương Thảo

25/08/1984

Giảng viên

vpthao@hluv.edu.vn

5

An Thị Ngọc Lý

13/05/1987

Giảng viên

atnly@hluv.edu.vn

6

Nguyễn Thị Thu

05/11/1982

Giảng viên

ntthu@hluv.edu.vn

7

Đỗ Thị Bích Thủy

27/07/1989

Giảng viên

dtbthuy@hluv.edu.vn

8

Lê Thị Huệ

25/09/1977

Trưởng môn Lịch sử

lthue@hluv.edu.vn

9

Phạm Thị Loan

28/03/1977

Giảng viên

ptloan@hluv.edu.vn

10

Lương Thị Tú

07/05/1986

Giảng viên

lttu@hluv.edu.vn

11

Đỗ Thị Hồng Thu

09/03/1984

Trưởng môn VNH

dththu@hluv.edu.vn

12

Nguyễn Hồng Thủy

14/09/1991

Giảng viên

nhthuy@hluv.edu.vn

13

Nguyễn Thị Hằng

12/12/1985

Giảng viên

nthang.kxh@hluv.edu.vn

14

Lê Thị Thu Hoài

06/06/1980

Giảng viên

ltthoai@hluv.edu.vn

15

Phạm Thị Hồng Tâm

24/06/1985

Giảng viên

pthtam@hluv.edu.vn

16

Đàm Thu Vân

10/02/1983

Giảng viên

dtvan@hluv.edu.vn

17

Bùi Thị Hồng Giang

16/11/1983

Giảng viên

bthgiang@hluv.edu.vn

18

Nguyễn Thị Hồng Nhung

08/07/1985

Giảng viên

nthnhung@hluv.edu.vn

19

Vũ Thị Tuyết Mai

27/03/1986

Giảng viên

vttmai@hluv.edu.vn

20

Phạm Thị Thu Thủy

16/04/1988

Giảng viên

pttthuy@hluv.edu.vn

21

Dương Thị Dung

29/09/1987

Giảng viên

dtdung@hluv.edu.vn

22

Trần Thị Thu

23/11/1984

Giảng viên

ttthu@hluv.edu.vn

23

Ngô Thị Huệ

20/10/1985

Giảng viên

nthue@hluv.edu.vn

24

Trần Thị Hiên

10/08/1988

Giảng viên

tthien@hluv.edu.vn

25

Lê Thị Hiệu

06/11/1988

Giảng viên

lthieu@hluv.edu.vn

26

Vũ Thị Hường

06/12/1985

Giảng viên

vthuong@hluv.edu.vn

27

Bùi Lê Nhật

15/02/1986

Giảng viên

blnhat@hluv.edu.vn

KHOA TỰ NHIÊN

tunhien@hluv.edu.vn

1

Lê Chí Nguyện

22/12/1964

P.Trưởng khoa PT

lcnguyen@hluv.edu.vn

2

Phùng Thị Thanh Hương

17/02/1976

P. Trưởng khoa

ptthuong@hluv.edu.vn

3

Lâm Văn Năng

08/11/1978

P. Trưởng khoa

lvnang@hluv.edu.vn

5

Phạm Văn Cường

26/12/1969

Giảng viên

pvcuong.ktn@hluv.edu.vn

6

Lê Thị Hồng Hạnh

22/12/1982

Giảng viên

lthhanh@hluv.edu.vn

7

Vũ Thị Ngọc Ánh

15/08/1986

Giảng viên

vtnanh@hluv.edu.vn

8

Đinh Bích Hảo

10/08/1987

Giảng viên

dbhao@hluv.edu.vn

9

Đặng Thị Thu Hiền

25/03/1985

Giảng viên

dtthien@hluv.edu.vn

10

Bùi Thị Hải Yến

03/03/1989

Giảng viên

bthyen.ktn@hluv.edu.vn

11

Nguyễn Thị Nhàn

23/07/1987

Giảng viên

ntnhan@hluv.edu.vn

12

Phạm Thị Minh Thu

03/10/1992

Giảng viên

ptmthu.ktn@hluv.edu.vn

13

Võ Thị Lan Phương

11/02/1984

Giảng viên

vtlphuong@hluv.edu.vn

14

Nguyễn Thị Lan Phương

12/01/1987

Giảng viên

ntlphuong@hluv.edu.vn

15

Hà Thị Hương

04/10/1976

Trưởng môn hóa

hthuong@hluv.edu.vn

16

Đinh Thị Kim Dung

21/11/1979

Giảng viên

dtkdung@hluv.edu.vn

17

Hoàng Thị Ngọc Hà

13/09/1980

Giảng viên

htnha@hluv.edu.vn

18

Bùi Thị Kim Cúc

28/10/1977

Giảng viên

btkcuc@hluv.edu.vn

19

Nguyễn Thiết Kế

22/03/1981

Giảng viên

ntke@hluv.edu.vn

KHOA NGOẠI NGỮ - TIN HỌC

ngoaingu-tinhoc@hluv.edu.vn

1

Nguyễn Thị Hồng Tuyên

09/11/1978

P.Trưởng khoa PT

nthtuyen@hluv.edu.vn

2

Đào Sỹ Nhiên

09/08/1979

P. Trưởng khoa

dsnhien@hluv.edu.vn

3

Phạm Thị Thanh

14/10/1981

Trưởng môn Tin học

ptthanh@hluv.edu.vn

4

Đặng Thị Thu Hà

03/09/1979

Giảng viên

dttha.nnth@hluv.edu.vn

5

Nguyễn Tất Thắng

20/12/1979

Giảng viên

ntthang.nnth@hluv.edu.vn

6

Mai Thị Thu Hân

22/02/1981

Trưởng môn Tiếng Anh

mtthan@hluv.edu.vn

7

Dương Thị Ngọc Anh

18/06/1977

Giảng viên

dtnanh@hluv.edu.vn

8

Nguyễn Thị Mỹ Hạnh

06/10/1984

Giảng viên

ntmhanh@hluv.edu.vn

9

Hoàng Thị Tuyết

09/03/1978

Giảng viên

httuyet@hluv.edu.vn

10

Nguyễn Thị Thúy Huyền

08/02/1986

Giảng viên

ntthuyen@hluv.edu.vn

11

Nguyễn Thị Hoàng Huế

27/09/1982

Giảng viên

nthhue@hluv.edu.vn

12

Đinh Thị Thùy Linh

18/02/1987

Giảng viên

dttlinh@hluv.edu.vn

13

Nguyễn Thị Huệ

19/01/1989

Giảng viên

nthue.nn@hluv.edu.vn

14

Phạm Đức Thuận

17/08/1980

Giảng viên

pdthuan@hluv.edu.vn

15

Nguyễn Thị Miền

20/03/1986

Giảng viên

ntmien@hluv.edu.vn

16

Phạm Thanh Tâm

15/12/1984

Giảng viên

pttam@hluv.edu.vn

17

Nguyễn Thị Lệ Thu

15/04/1988

Giảng viên

ntlthu@hluv.edu.vn

18

Đinh Thị Thu Huyền

20/11/1983

Giảng viên

dtthuyen.knn@hluv.edu.vn

19

Đặng Thanh Điềm

23/10/1989

Giảng viên

dtdiem@hluv.edu.vn

20

Bùi Thị Nguyên

08/03/1983

Giảng viên

btnguyen@hluv.edu.vn

KHOA KINH TẾ - KỸ THUẬT

kinhte@hluv.edu.vn

1

Đinh Thị Kim Khánh

09/12/1982

P.Trưởng khoa PT

dtkkhanh@hluv.edu.vn

2

Đỗ Thị Thủy

14/06/1977

P. Trưởng khoa

dothithuy@hluv.edu.vn

3

Nguyễn Thị Ánh Dương

06/04/1987

Giảng viên

ntaduong@hluv.edu.vn

4

Nguyễn Thị Bích Ngọc

28/08/1978

Trưởng môn Kinh tế

ntbngoc@hluv.edu.vn

5

Phạm Thị Khánh Quỳnh

02/09/1988

Giảng viên

ptkquynh@hluv.edu.vn

6

Nguyễn Thị Hồng Lý

12/08/1987

Giảng viên

nthly@hluv.edu.vn

7

Đặng Thị Thu Hà

10/10/1982

Trưởng môn Kế toán

dttha.kt@hluv.edu.vn

8

Đinh Thị Thanh Huyền

15/02/1989

Giảng viên

dtthuyen@hluv.edu.vn

9

Vũ Thị Phượng

11/12/1988

Giảng viên

vtphuong.kt@hluv.edu.vn

10

Lê Thị Uyên

24/03/1980

Giảng viên

ltuyen@hluv.edu.vn

11

Đặng Hà Quyên

21/01/1985

Giảng viên

dhquyen@hluv.edu.vn

12

Hà Thị Minh Nga

27/06/1985

Giảng viên

htmnga@hluv.edu.vn

13

Nguyễn Thị Bích Dung

07/02/1990

Giảng viên

ntbdung@hluv.edu.vn

14

Vũ Thị Vân Huyền

17/07/1982

Trưởng môn QTKD

vtvhuyen@hluv.edu.vn

15

Lê Thị Liễu

05/11/1982

Giảng viên

ltlieu@hluv.edu.vn

16

Phan Thị Hằng Nga

05/10/1983

Giảng viên

pthnga@hluv.edu.vn

17

Đinh Thị Thúy

27/09/1985

Giảng viên

dinhthithuy@hluv.edu.vn

18

Nguyễn Hải Biên

12/12/1985

Giảng viên

nhbien@hluv.edu.vn

19

Nguyễn Thùy Dương

18/10/1984

Giảng viên

ntduong@hluv.edu.vn

20

Vũ Thị Minh Huyền

22/03/1990

Giảng viên

vtmhuyen@hluv.edu.vn

21

Đinh Thị Thủy

15/09/1984

Giảng viên

dtthuy.ktcn@hluv.edu.vn

22

Hoàng Việt Hưng

14/02/1984

Giảng viên

hvhung@hluv.edu.vn

23

Lương Thu Giang

04/11/1984

Giảng viên

ltgiang@hluv.edu.vn

24

Ngô Thị Hằng

15/04/1986

Giảng viên

nthang@hluv.edu.vn

25

Phạm Thị Hương

09/11/1984

Giảng viên

pthuong@hluv.edu.vn

26

Bùi Thị Nhung

05/08/1987

Giảng viên

btnhung@hluv.edu.vn

27	Vũ Đức Hạnh		Giảng viên	vdhanh@hluv.edu.vn
KHOA TIỂU HỌC - MẦM NON

tieuhoc-mamnon@hluv.edu.vn

1

Tạ Hoàng Minh

02/07/1979

Trưởng khoa

thminh@hluv.edu.vn

2

Lưu Thị Chung

12/01/1974

P. Trưởng khoa

ltchung@hluv.edu.vn

3

Phạm Thị Thanh Vân

09/11/1972

P. Trưởng khoa

pttvan@hluv.edu.vn

4

Vũ Thị Diệu Thúy

18/05/1977

Trưởng môn MN

vtdthuy@hluv.edu.vn

5

Đinh Thị Hồng Loan

26/10/1984

Giảng viên

dthloan@hluv.edu.vn

6

Trương Hải Yến

06/05/1992

Giảng viên

thyen@hluv.edu.vn

7

Nguyễn Thị Hương Lan

01/04/1988

Giảng viên

nthlan@hluv.edu.vn

8

Phạm Thị Thu Hiền

01/06/1982

Trưởng môn âm nhạc

ptthien@hluv.edu.vn

9

Mai Thị Ánh Hồng

02/10/1980

Giảng viên

mtahong@hluv.edu.vn

10

Phạm Thị Thanh Mai

06/03/1989

Giảng viên

pttmai@hluv.edu.vn

11

Vũ Thị Thúy Ngà

11/06/1974

Giảng viên

vttnga@hluv.edu.vn

12

Phạm Thị Tuyết

06/08/1964

Giảng viên

pttuyet@hluv.edu.vn

13

Nguyễn Thị Hiền

07/09/1987

Giảng viên

nthien@hluv.edu.vn

14

Bùi Thị Kim Phụng

06/11/1982

Giảngviên

btkphung@hluv.edu.vn

15

Bùi Hương Giang

17/04/1987

Giảng viên

bhgiang@hluv.edu.vn

16

Hoàng Thị Hường

27/01/1984

Giảng viên

hthuong.mn@hluv.edu.vn

17

Lê Thị Thu Hương

30/11/1983

Trưởng môn GDTH

ltthuong@hluv.edu.vn

18

Phạm Văn Thiên

26/12/1976

Giảng viên

pvthien@hluv.edu.vn

19

Tống Thị Kim Anh

20/02/1987

Trưởng môn mỹ thuật

ttkanh@hluv.edu.vn

20

Dương Thu Hương

08/03/1994

Giảng viên

dthuong@hluv.edu.vn

21

Bùi Thị Hồng

28/09/1980

Giảng viên

bthong@hluv.edu.vn

22

Đỗ Hồng Lĩnh

10/11/1992

Giảng viên

dhlinh@hluv.edu.vn

23

Đinh Tiến Thành

01/09/1987

Chuyên viên

dtthanh@hluv.edu.vn

KHOA NÔNG LÂM

nonglam@hluv.edu.vn

1

Lê Thị Tâm

25/12/1980

Trưởng khoa

lttam@hluv.edu.vn

2

Lê Nguyệt Hải Ninh

16/06/1983

P.Trưởng khoa

lnhninh@hluv.edu.vn

3

Nguyễn Thi Loan

06/02/1979

Giảng viên

ntloan@hluv.edu.vn

4

Lưu Thanh Ngọc

27/07/1980

Giảng viên

ltngoc@hluv.edu.vn

5

Hoàng Thị Bằng

20/10/1974

Giảng viên

htbang@hluv.edu.vn

6

Bùi Thùy Liên

02/02/1985

Giảng viên

btlien@hluv.edu.vn

7

Nguyễn Thị Tố Uyên

20/08/1978

Giảng viên

nttuyen@hluv.edu.vn

8

Bùi Thị Phương

05/11/1983

Giảng viên

btphuong@hluv.edu.vn

9

Nguyễn Thị Mỳ

05/10/1983

Giảng viên

ntmy@hluv.edu.vn

10

Trần Thị Thanh Phương

08/09/1981

Giảng viên

tttphuong@hluv.edu.vn

11

Lê Thị Thu Thủy

21/05/1983

Giảng viên

lttthuy@hluv.edu.vn

12

Đinh Bá Hòe

01/01/1981

Giảng viên

dbhoe@hluv.edu.vn

13

Hoàng Phúc Ngân

14/05/1991

Giảng viên

hpngan@hluv.edu.vn

KHOA GIÁO DỤC THƯỜNG XUYÊN

gdthuongxuyen@hluv.edu.vn

1

Trần Ngọc Tú

23/10/1978

Trưởng khoa

tntu@hluv.edu.vn

2

Phạm Thị Hương Thảo

03/04/1981

P.Trưởng khoa

pththao@hluv.edu.vn

5

Nguyễn Thị Thanh Nhàn

07/12/1988

Chuyên viên

nttnhan@hluv.edu.vn

6

Phạm Thị Thùy Dung

14/12/1990

Chuyên viên

pttdung@hluv.edu.vn

3

Bùi Thị Tươi

24/01/1993

Chuyên viên

bttuoi@hluv.edu.vn

4

Lương Thị Hoàng Ngân

17/01/1980

Chuyên viên

lthngan@hluv.edu.vn

7

Trần Thị Phường

05/02/1988

Chuyên viên

ttphuong@hluv.edu.vn

8

Đinh Hoài Thu

01/12/1989

Nhân viên

dhthu@hluv.edu.vn

9

Nguyễn Trọng Tâm

20/08/1989

Nhân viên

nttam@hluv.edu.vn

BỘ MÔN GIÁO DỤC THỂ CHẤT - TÂM LÝ

tamly@hluv.edu.vn

1

Vũ Thị Phượng

24/01/1965

Trưởng bộ môn

vtphuong.tl@hluv.edu.vn

2

Nguyễn Thị Nguyệt

19/12/1976

P. Trưởng bộ môn

ntnguyet@hluv.edu.vn

3

Vũ Thị Hồng

02/08/1978

Trưởng môn Tâm lý

vthong@hluv.edu.vn

4

Nguyễn Thị Thịnh

16/09/1981

Giảng viên

ntthinh@hluv.edu.vn

5

Phạm Thị Trúc

20/08/1980

Giảng viên

pttruc@hluv.edu.vn

6

Đoàn Thị Hoa

21/01/1992

Giảng viên

doanthihoa@hluv.edu.vn

7

Bùi thị Kim Phương

01/07/1966

Giảng viên

btkphuong@hluv.edu.vn

8

Đoàn Thị Thơm

07/08/1984

Giảng viên

dtthom@hluv.edu.vn

9

Đinh Thị Hoa

04/10/1982

Giảng viên

dinhthihoa@hluv.edu.vn

10

Nguyễn Văn Hiếu

28/02/1983

Giảng viên

nvhieu@hluv.edu.vn

11

Phạm Thu Quỳnh

27/09/1988

Giảng viên

ptquynh@hluv.edu.vn

12

Trần Thị Tân

15/07/1990

Giảng viên

tttan@hluv.edu.vn

BỘ MÔN LÝ LUẬN CHÍNH TRỊ

llchinhtri@hluv.edu.vn

1

Đoàn Sỹ Tuấn

20/10/1978

P.Trưởng môn PT

dstuan@hluv.edu.vn

2

Lê Thị Ngọc Thùy

23/03/1983

P.Trưởng môn

ltnthuy@hluv.edu.vn

3

Phạm Thanh Xuân

24/01/1982

Giảng viên

ptxuan@hluv.edu.vn

4

Vũ Thị Hương Giang

21/04/1984

Giảng viên

vthgiang@hluv.edu.vn

5

Vũ Tuệ Minh

24/11/1984

Giảng viên

vtminh@hluv.edu.vn

6

Nguyễn Thị Hào

05/11/1985

Giảng viên

nthao@hluv.edu.vn

7

Bùi Thị Thu Hiền

01/06/1987

Giảng viên

btthien@hluv.edu.vn

8

Lê Thị Lan Anh

08/08/1985

Giảng viên

ltlanh@hluv.edu.vn

9

Phan Thị Thu Nhài

20/10/1985

Giảng viên

pttnhai@hluv.edu.vn

10

Phạm Thành Trung

06/04/1981

Trưởng môn ĐLCM của ĐCSVN

pttrung@hluv.edu.vn

11

Đỗ Thị Yên

25/02/1985

Giảng viên

dtyen@hluv.edu.vn

12

Nguyễn Thúy Mai

01/02/1989

Giảng viên

ntmai@hluv.edu.vn

13

Nguyễn Thị Thu Dung

22/08/1988

Giảng viên

nttdung.llct@hluv.edu.vn

14

Đào Thị Thu Phương

01/12/1985

Giảng viên

dttphuong@hluv.edu.vn

15

Nguyễn Thị Thu Thủy

01/08/1991

Giảng viên

nttthuy@hluv.edu.vn

TRUNG TÂM NGOẠI NGỮ - TIN HỌC

ttngoaingu-tinhoc@hluv.edu.vn

1

Nguyễn Thị Liên

13/08/1983

Giám đốc

ntlien@hluv.edu.vn

2

Đồng Thị Thu

22/04/1979

P. Giám đốc

dtthu@hluv.edu.vn

3

Bùi Thị Tuyết

27/07/1985

Giảng viên

bttuyet@hluv.edu.vn

4

Nguyễn Thị Thu Hà

14/05/1985

Giảng viên

nttha@hluv.edu.vn

5

Bùi Thị Thu Hoài

23/11/1984

Chuyên viên

btthoai@hluv.edu.vn

6

Đỗ Thị Thùy Linh

22/11/1992

Chuyên viên

dttlinh.ttnnth@hluv.edu.vn
TRUNG TÂM THƯ VIỆN - THIẾT BỊ

thuvien-thietbi@hluv.edu.vn

1

Dương Trọng Hạnh

26/03/1969

Giám đốc

dthanh@hluv.edu.vn

2

Bùi Bình An

04/11/1965

P.Giám đốc

buibinhan@hluv.edu.vn

3

Lê Thị Tuyết Nhung

14/03/1978

P.Giám đốc

lttnhung@hluv.edu.vn

4

Phạm Thị Ngà

12/08/1985

Giảng viên

ptnga@hluv.edu.vn

5

Hoàng Cao Minh

01/01/1986

Giảng viên

hcminh@hluv.edu.vn

6

Trần Thu Thủy

10/08/1984

Thư viện viên

ttthuy@hluv.edu.vn

7

Phạm Thị Yến

02/03/1986

Chuyên viên

ptyen@hluv.edu.vn

8

Đỗ Quang Đạt

28/07/1984

Tổ trưởng tổ TB

dqdat@hluv.edu.vn

9

Phạm Thị Thanh Hà

09/02/1985

Nhân viên

pttha@hluv.edu.vn

10

Đinh Công Quyền

20/06/1981

Nhân viên

dcquyen@hluv.edu.vn

11

Đỗ Thị Tươi

20/10/1981

Chuyên viên

dttuoi@hluv.edu.vn

12

Trịnh Thị Ngân Phương

19/09/1983

Nhân viên

ttnphuong@hluv.edu.vn

13

Nguyễn Thị Trang Nhung

12/08/1994

Nhân viên

nttnhung@hluv.edu.vn

14

Đinh Thị Hà

25/05/1990

Nhân viên

dtha@hluv.edu.vn

15

Trần Thanh Tâm

15/11/1986

Nhân viên

tttam@hluv.edu.vn

16

Dương Thị Thúy Hằng

09/01/1983

Nhân viên

dtthang@hluv.edu.vn

TRUNG TÂM Y TẾ - MÔI TRƯỜNG

ytemoitruong@hluv.edu.vn

1

Đinh Văn Viễn

24/02/1979

P.Giám đốc

dvvien@hluv.edu.vn

2

Đỗ Thị Giang

25/11/1969

Y sĩ (hạng IV)

dtgiang@hluv.edu.vn

3

Phạm Thị Minh Thu

03/07/1977

Dược (hạng IV)

ptmthu.yt@hluv.edu.vn

4

Nguyễn Thị Thu Hà

05/08/1975

Nhân viên

nttha.yt@hluv.edu.vn

5

Đặng Thị Hằng

02/07/1971

Hộ sinh (hạng IV)

dthang@hluv.edu.vn

6

Hoàng Ngọc Mai

30/06/1987

Nhân viên

hnmai@hluv.edu.vn

7

Phạm Thị Bích Phương

13/06/1989

Nhân viên

ptbphuong@hluv.edu.vn

BAN QUẢN LÝ KÝ TÚC XÁ

kytucxa@hluv.edu.vn

1

Đinh Ngọc Lưu

16/04/1960

Trưởng ban

dnluu@hluv.edu.vn

2

Lê Thị Hằng

31/10/1980

P.Trưởng ban

lthang@hluv.edu.vn

3

Nguyễn Thị Thanh Nga

20/05/1984

Chuyên viên

nttnga@hluv.edu.vn

4

Đào Thị Ánh Tuyết

19/02/1983

Giáo viên THCS

dtatuyet@hluv.edu.vn

5

Lê Thị Thu Hiền

15/05/1989

Thư viện viên (hạng IV)

ltthien@hluv.edu.vn

6

Vũ Thị Thu Hằng

16/02/1991

Chuyên viên

vtthang@hluv.edu.vn

7

Nguyễn Thị Thanh Nga

10/02/1988

Chuyên viên

nttnga.ktx@hluv.edu.vn

8

Đỗ Thị Hạnh

17/12/1987

Nhân viên

dthanh.ktx@hluv.edu.vn

9

Lê Thị Kim Dung

07/04/1983

Nhân viên

ltkdung@hluv.edu.vn

G
TS chính quy: 0938432640

G
TS VLVH 0936331567


Bản đồ chỉ dẫn
Trường Đại học Hoa Lư


Trụ sở chính
Đường Xuân Thành, thành phố Ninh Bình, tỉnh Ninh Bình.

Điện thoại: 02293 892 240

Fax: 02293 892 241

Hỗ trợ Tuyển sinh: 02293 892 701

Chịu trách nhiệm nội dung:
Phó Hiệu trưởng TS. Nguyễn Mạnh Quỳnh
Tel: 02293.892.895
Email: nmquynh@hluv.edu.vn

-->
Copyright © 2019 HoaLu University.
'''

Birthdays = re.findall("[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}", txt)

emails = re.findall("[a-z]+@[a-z]+.[a-z]+.[a-z]", txt)
#print(Birthdays)
print(emails)