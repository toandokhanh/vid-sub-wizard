<!-- install all module install -->

# conda install Pyaudio

# pip3 install -r requirements2.txt

<!-- Chạy tạo phụ đề riêng -->

# python3 phude.py

<!-- Chạy web (Flask) + tự động chạy file-->

# python3 video.py

<!-- Cơ dư dữ liệu -->

# Trong file database cùng tên (dùng Xampp Mysql) (nếu đổi tên csdl thì vào file video.py)

thay lại tên csdl:

# app.config['MYSQL_DATABASE_DB']='ten csdl mới'

- Database: phude.sql

url: đường đẫn file (.mp4)
-s: ngôn ngữ nguồn.
-d: ngôn ngữ đích (mặc định là vi)
-n: tên mới
-noise: thuật toán giảm nhiễu (2 giải thuật ở bên dưới)

=> deep: Dùng giải thuật DeepFilter
=> noise: Dùng giải thuật Noisereduce

# python3 phude.py 'url' -s ngonnguvao -d ngonngudich -n tenmoi -noise chongiaithuat

<!-- Example 1 (vi -> en) use: deepfilternet -->

path = 't/video.mp4'
language_source = 'vi'
language_dest = 'en'
newname = 'video2022'
choose_noise = 'DeepFilterNet'

<!-- End  -->

# python3 phude.py t/video.mp4 -s vi -d en -n video2022 -noise deep

<!-- Example 2 (source vi) use noisereduce -->

path = 'phude/cuoi.mp4'
language_source = 'vi'
language_dest = 'vi'
newname = 'videokaka'
choose_noise = 'Noisereduce'

# python3 phude.py t/video.mp4 -s vi -n video2022 -noise noise

-> Because language dest is 'vi' should not parameter

<!-- End  -->

<!-- Example 3 (source en -> vi) no reduce -->

path = 'phude/tron.mp4'
language_source = 'vi'
language_dest = 'en'
newname = 'tron_new'
choose_noise = 'No'

# python3 phude.py t/video.mp4 -s vi -d en -n video2022

->Not parameter -noise because choose_noise is 'no'

<!-- tính phần trăm cosine -->

# python3 sosanh_log -train train -compare fileSoSanh

- train: tham số tryền vào là thư mục cần so sánh với file gốc (trong đó train: là thư mục sau khi tạo phụ đề cần so sánh với nội dung gốc)
- compare: tham số truyền vào là thư mục file gốc (fileSoSanh: là thư mục có nội dung gốc)




<!-- Cấu trúc thư mục Normal và tên video (không có tiếng ồn) -->
.
└───Video
    ├───Normal
    │   ├───video.mp4
        ├
        ├
        ├───Output     (sau chạy xong video các file txt ... được lưu vào thư mục Output với tên đúng như video gốc)
# <NgonNgu>_<CongCu>_<GioiTinh>_<SochuTrongVideo>_<STT>.mp4
vd: EN_tran_1_50_01.mp4
- Ngôn ngữ
    + EN: ngôn ngữ English  
    + VI: ngôn ngữ Việt Nam
- Công cụ
    + tran: google translate đọc
    + art: artificial (giọng con người đọc)
- Giới tính
    + 1: nam
    + 0: nữ
- Số chữ trong video
    + 50: video chứa < 50 chữ
    + 100: video chứa từ 50 - 100 chữ
    + 300: video chứa từ 100 - 300 chữ
    + 500: video chứa từ 500 - 1000 chữ
    + 1000: video chứa từ > 1000 chữ
- Số thứ tự của video





<!-- Cấu trúc thư mục Noisy và tên video (có tiếng ồn)-->
.
└───Video
    ├───Noisy
    │   ├───video.mp4
        ├
        ├
        ├───Output     (sau chạy xong video các file txt ... được lưu vào thư mục Output với tên đúng như video gốc)

# <NgonNgu>_<CongCu>_<GioiTinh>_<SochuTrongVideo>_<GiaiThuatChongTiengOn>_<LoaiTiengOn>_<STT>.mp4
vd: EN_tran_1_50_1_01.mp4
- Ngôn ngữ
    + EN: ngôn ngữ English  
    + VI: ngôn ngữ Việt Nam
- Công cụ
    + tran: google translate đọc
    + art: artificial (giọng con người đọc)
- Giới tính
    + 1: nam
    + 0: nữ
- Số chữ trong video
    + 50: video chứa < 50 chữ
    + 100: video chứa từ 50 - 100 chữ
    + 300: video chứa từ 100 - 300 chữ
    + 500: video chứa từ 500 - 1000 chữ
    + 1000: video chứa từ > 1000 chữ
- Giải thuật
    + deep: DeepFilterNet
    + noise: Noisereduce 
- Loại tiếng ồn
    + 1 là loại tiếng ồn nơi công cộng (nơi đông người)
    + 2 là loại tiếng ồn quán cafe (phòng kính)
    + 3 là loại tiếng ồn do mưa
    + 4 là loại tiếng ồn của máy móc thiết bị
    + 5 là loại tiếng ồn máy lạnh
    + 6 là loại tiếng ồn quạt gió
    + 7 là loại tiếng ồn xe máy
    + 8 là loại tiếng ồn xe oto
    + 9 là loại tiếng ồn khác
- Số thứ tự của video


- vietnam 50 
    + VI_gg_0_50_01
    + VI_gg_1_50_01
    + VI_gg_0_50_02
    + VI_gg_1_50_02
    + VI_art_0_50_01
    + VI_art_1_50_01
    + VI_art_0_50_02
    + VI_art_1_50_02
- vietnam 100
    + VI_gg_0_100_01
    + VI_gg_1_100_01
    + VI_gg_0_100_02
    + VI_gg_1_100_02
    + VI_art_0_100_01
    + VI_art_1_100_01
    + VI_art_0_100_02
    + VI_art_1_100_02
- vietnam 300
    + VI_gg_0_300_01
    + VI_gg_1_300_01
    + VI_gg_0_300_02
    + VI_gg_1_300_02
    + VI_art_0_300_01
    + VI_art_1_300_01
    + VI_art_0_300_02
    + VI_art_1_300_02
- vietnam 500
    + VI_gg_0_500_01
    + VI_gg_1_500_01
    + VI_gg_0_500_02
    + VI_gg_1_500_02
    + VI_art_0_500_01
    + VI_art_1_500_01
    + VI_art_0_500_02
    + VI_art_1_500_02

<!-- End  -->
