# filename = "count.txt"
# with open(filename, "r") as file:
#     lines = file.readlines()
#     count = len(lines)
#     print("Số câu trong file là:", count)



# import cv2

# # Tải video từ đường dẫn
# video = cv2.VideoCapture("normal/VietNam/VI_art_0_50_01.mp4")

# # Lấy thông tin video
# total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# fps = int(video.get(cv2.CAP_PROP_FPS))

# # Tính thời gian tổng cộng của video (tính bằng giây)
# duration = total_frames / fps

# # In kết quả
# print("Độ dài của video: {:.2f} giây".format(duration))

# # Giải phóng tài nguyên
# video.release()



# update

import os
import cv2

# Đường dẫn đến thư mục chứa các video
directory = "Normal/VietNam"

# Lấy danh sách tất cả các tập tin trong thư mục
files = os.listdir(directory)

# Duyệt qua từng tập tin
for file in files:
    # Chỉ xử lý tập tin có đuôi .mp4
    if file.endswith(".mp4"):
        # Tải video từ đường dẫn
        video = cv2.VideoCapture(os.path.join(directory, file))

        # Lấy thông tin video
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(video.get(cv2.CAP_PROP_FPS))

        # Tính thời gian tổng cộng của video (tính bằng giây)
        duration = total_frames / fps

        # In kết quả
        print("Độ dài của video {}: {:.2f}s".format(file, duration))

        # Giải phóng tài nguyên
        video.release()