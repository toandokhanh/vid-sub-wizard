from regex import F
from num2words import num2words
from srtToTxt import srt_to_txt



def readfile(filename):
    file_input = open(filename, "r", encoding="utf-8")
    read_file = file_input.read()  # Đọc nội dung của File
    return read_file

def write_file(filename,txt):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(txt)











def handleFile(path,lang='vi'):
    # Đọc file
    a = readfile(path)


    # Chuyển đổi số sang chữ
    tach_tu = a.split(' ')
    for word in tach_tu:
        if(word.isdigit()):
            num = num2words(int(word),lang=lang)
            a = a.replace(word,num)
    # Lưu file
    write_file(path,a)



