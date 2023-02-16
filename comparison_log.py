from fileinput import filename
import os,re
import sys
import cv2
from datetime import datetime
import time
from regex import P
from convert import handleFile
import argparse
import contextlib
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

#  Tính độ dài video
# Đường dẫn đến thư mục chứa các video
directory = "template_log"



# Duyệt qua từng tập tin

 
def Tong(test_content):
    tong = len(re.findall(r'\w+', test_content))
    return tong

# Thời gian bắt đầu thực thi
start_time = datetime.now()


parser = argparse.ArgumentParser()
parser.add_argument('-train', '--train', help="---> file sau khi tạo phụ đề")
parser.add_argument('-compare', '--file_origin', help="---> File gốc cần lúc ban đầu ")

args = parser.parse_args()

path = ''
path2 = ''

try:
# File train

    path = args.train + '/'
    train_files =[doc for doc in os.listdir(path) if (doc.endswith('.txt') )]

    path2 = args.file_origin + '/'
    compare_files =[doc for doc in os.listdir(path2) if (doc.endswith('.txt') )]
    compare_videos =[doc for doc in os.listdir(path2) if (doc.endswith('.mp4') )]
    # Lấy danh sách tất cả các tập tin trong thư mục

except:
    print("")


# File so sanh
# path2 = "train/"


# for file in student_files:
#     print(file[:file.index('.')])
# 


def readfile(filename):
    file_input = open(filename, "r", encoding="utf-8")
    read_file = file_input.read()  # Đọc nội dung của File
    read_file = read_file.lower()
    return read_file

    



def check_similarity(file1,file2):
    vector1 = []

    read_file = readfile(file1)
    
    read_file2 = readfile(file2)

    vector1.append(read_file)
    vector1.append(read_file2)

    # Tính độ quan trọng và số lần xuất hiện
    vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
    # Tính Sine dựa vào tích vô hướng
    similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])
    vector = vectorize(vector1)
    result = similarity(vector[0],vector[1])[0][1]
    return round(result*100,5)




if __name__ == "__main__":
# print(check_similarity('train/tong.txt','fileSoSanh/tong_mau.txt'))
# tạo file luu ket qua trong thư mục fileKetQua
    today = datetime.today()

    time = today.strftime("%H") + "h" + today.strftime("%M")
    date = today.strftime("%Y-%m-%d") 

    dateVN = today.strftime("%d-%m-%Y")
    file_log =args.train + '_' + args.file_origin
    file_log = file_log.replace('/', '---')
    # print(file_log)
    f = open('result/'+str(file_log)+'.txt', 'w',encoding = 'utf-8')
    #f = open('result/result.txt', 'w',encoding = 'utf-8')
    
    f.write("Thực hiện: "+str(time) + " " + str(dateVN) +"\n")
    f.write("\n==== ==== ==== ==== ==== ====\n")
    f.write("Đầu ra, Số chữ đầu ra, Đầu vào, Số chữ đầu vào, Tác nhân, Số giây của video, Kết quả \n")
    result = []
    i=0
    arrayTimes = [];    


    # kiểm tra tham số video
    result_algorithm = '';
    if "Normal" in file_log:
        result_algorithm = ('Kết quả phụ đề video không có tiếng ồn')
    elif "noise" in file_log:
        result_algorithm = ('Kết quả phụ đề của video có tiếng ồn dùng giải thuật giảm tiếng ồn Noisereduce')
    elif "deep" in file_log:
        result_algorithm = ('Kết quả phụ đề của video có tiếng ồn dùng giải thuật giảm tiếng ồn DeepFilter')
    elif "not" in file_log:
        result_algorithm = ('Kết quả phụ đề video có tiếng ồn không dùng giải thuật giảm tiếng ồn')
    else:
        result_algorithm = ('Kết quả phụ đề không xác định')
    
    for compare_video in compare_videos:
        
        video = cv2.VideoCapture(os.path.join(path2, compare_video))
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(video.get(cv2.CAP_PROP_FPS))
        duration = total_frames / fps
        # Giải phóng tài nguyên
        nameVideo = format(compare_video)
        timeVideo = format(duration)    
        video.release()
        arrayTimes.append(timeVideo);
    for index,train in enumerate(train_files):
        file1 = path+train
        file2 = path2+train[:train.index('.')]+'_mau.txt'
        # dem so chu (8/2/2023)
        def count_words(filename):
            with open(filename, "r") as f:
                contents = f.read()
                words = contents.split()
                return len(words)
        file1_words = count_words(file1)
        file2_words = count_words(file2)
        # print(f"{file1}   : {file1_words}")
        # print(f"{file2}   : {file2_words}")

# kiem tra tac nhan
        if "art" in file2:
            tacnhan = "connguoi"
        elif "gg" in file2:
            tacnhan = "google"
        else :
            tacnhan = "Không xác định được"
        if(os.path.isfile(file2)==False):
            print('Đường dẫn thư mục {} không tồn tại'.format(file2))
            continue
        else:
            
            similarity = str(check_similarity(file1,file2)) 
        # print(file1,file2)
        # print(str(round(check_similarity(vec)*100,5))+" %")
        # Format biến arrayTimes[index]
            formatted_array_time = "{:.2f}".format(float(arrayTimes[index]))
            testt = 100
            kq = '{} , {}, {} , {}, {}, {}s, {}%'.format(train,file1_words,train[:train.index('.')]+'_mau.txt',file2_words,tacnhan,formatted_array_time,similarity)
            i+=1
            f.write(kq+"\n")
            
        result.append(kq)
    end_time = datetime.now()
    f.write(result_algorithm)
    print('Chạy thành công '+result_algorithm)
    f.write('\n=> Tổng số có {} file đã thực thi '.format(i))
    f.write('\n=> Thời gian thực thi: '+str(end_time - start_time))


# tachfile = s_vectors[-1][0].split(".")
# f = open( "fileKetQua/KetQuaCosine.txt" , 'w',encoding = 'utf-8')

# #Lưu kết quả vào file
# f.write("Thực hiện: "+str(time) + " " + str(dateVN) +"\n")
# # f.write("\nTập tin  CTUD_QLDatPhong.docx ("+ str(Tong(test_notes[0])) +"):")
# f.write("\n==== ==== ==== ==== ==== ====\n")
# for data in check_plagiarism():
#     f.write(str(data) + "\n") 
    
    
# end_time = datetime.now()
# f.write('\n=> Thời gian thực thi: '+str(end_time - start_time))



# Thời gian kết thúc thực thi
# Thời gian kết thúc thực thi
# file1 = file1.split("/")[-1]
# file2 = file2.split("/")[-1]

# print("file2",file2)
# lines = file1.readlines()
# count = len(lines)
# print("Số câu trong file1 là:", count)
# lines = file2.readlines()
# count = len(lines)
# print("Số câu trong file2 là:", count)
       

