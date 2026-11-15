Thực hành vòng lặp lồng nhau trong Python

Kỹ thuật lập trình \| Phiếu thực hành dành cho người mới học

Với mỗi bài, hãy dự đoán kết quả, chạy mã gợi ý, sửa theo yêu cầu rồi
chạy lại. Ghi đầu vào, kết quả thực tế và lý do thay đổi theo mẫu ở cuối
tài liệu. Các giá trị nhập cách nhau bằng dấu cách trên một dòng; giả sử
nhập đúng kiểu số nguyên.

# Bài 01 In hình chữ nhật dấu sao

In hình chữ nhật có 3 hàng, mỗi hàng 5 dấu sao.

## Cách làm

Vòng ngoài chọn hàng. Vòng trong in từng dấu sao trên hàng đó. Đặt
print() xuống dòng sau vòng trong, nhưng vẫn ở trong vòng ngoài.

n, m = 3, 5 for i in range(n): for j in range(m): print('\*', end=' ')
print()

## Cải tiến bắt buộc

Thay kích thước cố định bằng n và m nhập từ bàn phím. Nếu một kích thước
không dương, chỉ in "Khong hop le". Nếu hợp lệ, in hình và thêm một dòng
ghi tổng số dấu sao.

## Dữ liệu chạy thử sau cải tiến

| Đầu vào \| Kết quả mong đợi \|

| --- \| --- \|

| 2 3 \| 2 hàng, mỗi hàng 3 dấu sao; dòng cuối: 6. \|

| 1 1 \| Một hàng có 1 dấu sao; dòng cuối: 1. \|

| 0 4 \| Khong hop le \|

## Câu hỏi rút ra kết luận

Vì sao khối in dấu sao chạy n × m lần? Khi chuyển print() vào trong vòng
trong, hình thay đổi thế nào?

# Bài 02 In tam giác dấu sao

In tam giác cao 4 hàng: hàng i có i dấu sao.

## Cách làm

Cho i chạy từ 1 đến h. Vòng trong chạy i lượt, nên số lượt không còn
giống nhau ở mọi hàng.

h = 4 for i in range(1, h + 1): for j in range(i): print('\*', end=' ')
print()

## Cải tiến bắt buộc

Nhập chiều cao h. Nếu h không dương, chỉ in "Khong hop le". Nếu hợp lệ,
in tam giác ngược: hàng đầu có h dấu sao, mỗi hàng sau bớt một dấu sao.
Gợi ý: xét range có bước nhảy −1.

## Dữ liệu chạy thử sau cải tiến

| Đầu vào \| Kết quả mong đợi \|

| --- \| --- \|

| 4 \| Bốn hàng có lần lượt 4, 3, 2, 1 dấu sao. \|

| 1 \| Một hàng có đúng 1 dấu sao. \|

| -1 \| Khong hop le \|

## Câu hỏi rút ra kết luận

Với h = 4, tổng cộng in bao nhiêu dấu sao? Vì sao không dùng h × h?

## Truy vết mẫu trước khi sửa

| Hàng i \| Giá trị j \| Số dấu sao \|

| --- \| --- \| --- \|

| 1 \| 0 \| 1 \|

| 2 \| 0, 1 \| 2 \|

| 3 \| 0, 1, 2 \| 3 \|

Tự bổ sung hàng thứ 4, rồi lập bảng tương tự cho tam giác ngược.

# Bài 03 In bảng cửu chương

In hai bảng nhân 2 và 3, mỗi bảng có các phép nhân từ 1 đến 3. Đây là
phiên bản ngắn của bài in các bảng từ 2 đến 9 trong đề gốc.

## Cách làm

Vòng ngoài chọn bảng nhân i; vòng trong thay đổi thừa số j. In một phép
nhân trên mỗi dòng.

for i in range(2, 4): for j in range(1, 4): print(f"{i} x {j} = {i \*
j}")

## Cải tiến bắt buộc

Nhập a, b, k. Với 2 ≤ a ≤ b ≤ 9 và 1 ≤ k ≤ 10, in các bảng từ a đến b,
mỗi bảng nhân từ 1 đến k. Nếu dữ liệu ngoài miền trên, chỉ in "Khong hop
le".

## Dữ liệu chạy thử sau cải tiến

| Đầu vào \| Kết quả mong đợi \|

| --- \| --- \|

| 2 3 2 \| Bốn dòng: 2 x 1 = 2; 2 x 2 = 4; 3 x 1 = 3; 3 x 2 = 6. \|

| 9 9 1 \| Một dòng: 9 x 1 = 9. \|

| 3 2 5 \| Khong hop le \|

## Câu hỏi rút ra kết luận

Vì sao số bảng là b − a + 1? Nếu đổi thứ tự hai vòng lặp, các phép nhân
sẽ được nhóm theo biến nào?

# Bài 04 In bảng số theo hàng hoặc cột

In bảng 3 × 3. Trên mỗi hàng, các giá trị tăng từ 1 đến 3.

## Cách làm

i là số thứ tự hàng, j là số thứ tự cột. Thử dự đoán kết quả khi đổi
biến được in từ j sang i.

n = 3 for i in range(1, n + 1): for j in range(1, n + 1): print(j, end='
') print()

## Cải tiến bắt buộc

Nhập n và chế độ c. Với n dương, chế độ 1 in j ở từng ô; chế độ 2 in i ở
từng ô. Nếu n không dương hoặc c khác 1 và 2, chỉ in "Khong hop le". Giữ
nguyên hai vòng lặp; dùng if để chọn giá trị in.

## Dữ liệu chạy thử sau cải tiến

| Đầu vào \| Kết quả mong đợi \|

| --- \| --- \|

| 3 1 \| Ba hàng giống nhau: 1 2 3. \|

| 2 2 \| Hàng 1: 1 1. Hàng 2: 2 2. \|

| 2 3 \| Khong hop le \|

## Câu hỏi rút ra kết luận

Tại sao nên dùng n = 2 hoặc n = 3 để phân biệt hai chế độ? Hai chế độ có
thể trùng kết quả với n nào?

# Bài 05 Kết hợp while và for

Dùng while cho lượt ngoài, for cho lượt trong. Đếm số lần khối lệnh
trong cùng chạy.

## Cách làm

Tăng i đúng một lần sau mỗi vòng for. Đặt biến đếm trước cả hai vòng để
giữ tổng số lượt.

dem = 0 i = 1 while i \<= 2: for j in range(1, 4): print(i, j) dem += 1
i += 1 print(dem)

## Cải tiến bắt buộc

Nhập n, m là số lượt ngoài và số lượt trong, cho phép bằng 0. Với n, m
không âm, in các cặp (i, j) theo mẫu rồi in tổng. Nếu một giá trị âm,
chỉ in "Khong hop le".

## Dữ liệu chạy thử sau cải tiến

| Đầu vào \| Kết quả mong đợi \|

| --- \| --- \|

| 2 2 \| Bốn cặp theo thứ tự: (1,1), (1,2), (2,1), (2,2); dòng cuối: 4.
  \|

| 0 3 \| Không in cặp nào; chỉ in 0. \|

| 3 0 \| Không in cặp nào; chỉ in 0. \|

| -1 2 \| Khong hop le \|

## Câu hỏi rút ra kết luận

Khi n = 3, m = 0, vòng while chạy mấy lượt? Vì sao i += 1 phải ở ngoài
vòng for, kể cả khi for không chạy lượt nào?

# Phiếu ghi nhận và đánh giá

Sao chép hai bảng dưới đây cho mỗi bài. Chạy mã gốc và mã cải tiến bằng
dữ liệu phù hợp; ghi kết quả quan sát được. Với mã gốc có biến cố định,
ghi rõ giá trị được khai báo trong mã.

## Nhật ký thay đổi

| Mã hoặc hành vi trước khi sửa \| Thay đổi đã thực hiện \| Lý do và tác
  động \|

| --- \| --- \| --- \|

| Ví dụ bài 01: n, m được gán cố định. \| Đọc n, m từ bàn phím. \| Có
  thể kiểm thử nhiều kích thước mà không sửa lại mã. \|

|  \| \| \|

|  \| \| \|

## Bảng kiểm thử

| Loại ca \| Đầu vào \| Mong đợi \| Thực tế \| Đạt hay chưa \|

| --- \| --- \| --- \| --- \| --- \|

| Thông thường \| \| \| \| \|

| Biên \| \| \| \| \|

| Ngoài miền \| \| \| \| \|

| Tự thiết kế \| \| \| \| \|

Nếu kết quả khác mong đợi, ghi lỗi tìm được, cách sửa và kết quả sau khi
chạy lại. Với bài in hình, so sánh cả số hàng lẫn số phần tử trên từng
hàng.

## Kết luận của sinh viên

Viết 2--3 câu cho mỗi bài: vòng ngoài và vòng trong làm gì, em đã sửa
điểm nào và ca kiểm thử nào chứng minh thay đổi đó hoạt động. Trả lời
câu hỏi ở cuối mỗi bài bằng một ví dụ đã chạy.

## Sản phẩm nộp và thang điểm

Nộp 5 file Python đã cải tiến và một báo cáo Word gồm nhật ký, bảng kiểm
thử và kết luận của từng bài. Trong mỗi bài, chạy các ca đã cho và thêm
ít nhất một ca tự thiết kế.

| Tiêu chí \| Điểm \|

| --- \| --- \|

| Hai vòng lặp đúng yêu cầu và đúng thứ tự \| 3 \|

| Cải tiến đúng, xử lý đúng dữ liệu ngoài miền \| 3 \|

| Kiểm thử có kết quả thực tế và đối chiếu \| 2 \|

| Ghi nhận thay đổi và giải thích được kết quả \| 2 \|
