<h6 align="right">Author: <a href="https://github.com/toandokhanh">Do Khanh Toan<a/> </h6>

#### Install all module install 

    conda install Pyaudio

    pip3 install -r requirements.txt

#### Chạy tạo phụ đề riêng

    python3 phude.py

#### Chạy web (Flask) + tự động chạy file

    python3 video.py
#### Cơ sở dữ liệu

- Trong file database cùng tên (dùng Xampp Mysql) (nếu đổi tên csdl thì vào file video.py)

#### Thay lại tên csdl:

- app.config['MYSQL_DATABASE_DB']= 'ten csdl mới'

- Database: phude.sql


#### Url: đường đẫn file (.mp4) 

    -s: ngôn ngữ nguồn.

    -d: ngôn ngữ đích (mặc định là vi)

    -n: tên mới

    -noise: thuật toán giảm nhiễu (2 giải thuật ở bên dưới)

=> deep: Dùng giải thuật DeepFilter

=> noise: Dùng giải thuật Noisereduce

    python3 phude.py 'url' -s ngonnguvao -d ngonngudich -n tenmoi -noise chongiaithuat

#### Example 1 (vi -> en) use: deepfilternet

    path = 't/video.mp4'
    language_source = 'vi'
    language_dest = 'en'
    newname = 'video2022'
    choose_noise = 'DeepFilterNet'

<!-- End  -->

    python3 phude.py t/video.mp4 -s vi -d en -n video2022 -noise deep

#### Example 2 (source vi) use noisereduce

    path = 'phude/cuoi.mp4'
    language_source = 'vi'
    language_dest = 'vi'
    newname = 'videokaka'
    choose_noise = 'Noisereduce'

<!-- End  -->
    python3 phude.py t/video.mp4 -s vi -n video2022 -noise noise

=> Because language dest is 'vi' should not parameter

<!-- End  -->

#### Example 3 (source en -> vi) no reduce

    path = 'phude/tron.mp4'
    language_source = 'vi'
    language_dest = 'en'
    newname = 'tron_new'
    choose_noise = 'No'
<!-- End  -->
    python3 phude.py t/video.mp4 -s vi -d en -n video2022

=>Not parameter -noise because choose_noise is 'no'

#### Tính phần trăm cosine

    python3 comparison_log -train train -compare template_log

- train: tham số tryền vào là thư mục cần so sánh với file gốc (trong đó train: là thư mục sau khi tạo phụ đề cần so sánh với nội dung gốc)

- compare: tham số truyền vào là thư mục file gốc (fileSoSanh: là thư mục có nội dung gốc)




#### Cấu trúc thư mục  

    └───Normal (ouput của phụ đề video không có tiếng ồn)
        ├───video.mp4
        ├───video.srt
        ├───video.txt
        ├───video.wav
    └───Noisy (thư mục chứa video có tiếng ồn)
        ├───deep (ouput của phụ đề chạy giải thuật deep)
        ├───noise (ouput của phụ đề chạy giải thuật noise)
        ├───not (ouput của phụ đề không có giải thuật)
            ├───video.mp4 (Video gốc có tiếng ồn)
    └───template_log (thư mục chứa video và file txt gốc không có tiếng ồn)


#### Cách đặt tên file video
    <NgonNgu>_<TacNhan>_<GioiTinh>_<SochuTrongVideo>_<STT>.mp4

    vd: EN_gg_1_50_01.mp4
- Ngôn ngữ
    + EN: ngôn ngữ English  
    + VI: ngôn ngữ Việt Nam
- Công cụ
    + gg: google translate đọc
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
    + 01
    + 02
    + 03
             
#### Cách đặt tên file video có tiếng ồn
    <NgonNgu>_<CongCu>_<GioiTinh>_<SochuTrongVideo>_<GiaiThuatChongTiengOn>_<LoaiTiengOn>_<STT>.mp4
    
- VietNam 50

        VI_gg_0_50_01
        VI_gg_1_50_01
        VI_gg_0_50_02
        VI_gg_1_50_02
        VI_art_0_50_01
        VI_art_1_50_01
        VI_art_0_50_02
        VI_art_1_50_02

- VietNam 100

        VI_gg_0_100_01  
        VI_gg_1_100_01
        VI_gg_0_100_02
        VI_gg_1_100_02
        VI_art_0_100_01
        VI_art_1_100_01
        VI_art_0_100_02
        VI_art_1_100_02

- VietNam 300

        VI_gg_0_300_01
        VI_gg_1_300_01
        VI_gg_0_300_02
        VI_gg_1_300_02
        VI_art_0_300_01
        VI_art_1_300_01
        VI_art_0_300_02
        VI_art_1_300_02

- VietNam 500

        VI_gg_0_500_01
        VI_gg_1_500_01
        VI_gg_0_500_02
        VI_gg_1_500_02
        VI_art_0_500_01
        VI_art_1_500_01
        VI_art_0_500_02
        VI_art_1_500_02

- VietNam 1000

        VI_gg_0_1000_01
        VI_gg_1_1000_01
        VI_gg_0_1000_02
        VI_gg_1_1000_02
        VI_art_0_1000_01
        VI_art_1_1000_01
        VI_art_0_1000_02
        VI_art_1_1000_02

- English 50

        EN_gg_0_50_01
        EN_gg_1_50_01
        EN_gg_0_50_02
        EN_gg_1_50_02
        EN_art_0_50_01
        EN_art_1_50_01
        EN_art_0_50_02
        EN_art_1_50_02

- English 100

        EN_gg_0_100_01
        EN_gg_1_100_01
        EN_gg_0_100_02
        EN_gg_1_100_02
        EN_art_0_100_01
        EN_art_1_100_01
        EN_art_0_100_02
        EN_art_1_100_02

- English 300

        EN_gg_0_300_01
        EN_gg_1_300_01
        EN_gg_0_300_02
        EN_gg_1_300_02
        EN_art_0_300_01
        EN_art_1_300_01
        EN_art_0_300_02
        EN_art_1_300_02

- English 500

        EN_gg_0_500_01
        EN_gg_1_500_01
        EN_art_0_500_01
        EN_art_1_500_01

- English 1000

        EN_gg_0_1000_01
        EN_gg_1_1000_01
        EN_art_0_1000_01
<!-- End  -->
