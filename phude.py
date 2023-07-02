import argparse
import os,sys
import createsub

from regex import F
from datetime import datetime
from srtToTxt import srt_to_txt

import noisereduce as nr
import soundfile as sf
import librosa
from noisereduce.generate_noise import band_limited_noise
import time



parser = argparse.ArgumentParser()
parser.add_argument('source_path', help="Path to the video or audio file to subtitle", nargs='?')
# parser.add_argument('-i', '--dir', help="---> đường dẫn file cần chạy")
# parser.add_argument('-o', '--dir_op', help='---> đường dẫn lưu trữ file')
parser.add_argument('-s', '--l_in', help='---> truyền ngôn ngữ file đầu vào')
parser.add_argument('-d', '--l_out', help='---> truyền ngôn ngữ file cần xuất',default="vi")
parser.add_argument('-txt', '--file_txt', help='---> chuyển về folder srt thành txt để so sánh độ chính xác')
parser.add_argument('-noise','--algorithm_noise',help="---> Chọn thuật toán giảm nhiễu",default="no")
parser.add_argument('-n','--new_name',help="---> Đặt lại với tên mới")
args = parser.parse_args()

# python3 phude.py 'url' -s ngonnguvao -d ngonngudich -n tenmoi -noise chongiaithuat



def mp4_to_wav(filename,output,name):
    # name = filename[filename.index('/'):filename.[]]
    os.system('ffmpeg -i {} -ar 44100 {}/{}.wav'.format(filename,output,name))

def noise_deepfilternet(file,file_out):
    os.system('deepFilter {} -o {}'.format(file,file_out))
    print("Đã giảm tiếng ồn DeepFilterNet")


def noise_reduce(file,file_out):
    y, sr = librosa.load(file)
    reduced_noise = nr.reduce_noise(y = y, sr=sr, thresh_n_mult_nonstationary=2,stationary=False)
    sf.write(file_out,reduced_noise, sr, subtype='PCM_24')
    print('Đã giảm tiếng ồn xong!')

def rename(filename,newname): 
    os.rename(filename, newname)

try: 
    newname = args.new_name

    noises = args.algorithm_noise

    directory = args.source_path
    # file_output = args.dir_op
    lang_in = args.l_in
    lang_out = args.l_out
    path_txt = args.file_txt
except:
    print('')

def wav_to_flac(filename,output):
    os.system('ffmpeg -y -f wav -i {} -write_xing 0 -f flac {}'.format(filename,output))


def videoOutput(file_in,file_srt,file_out):
        os.system('ffmpeg -y -i {} -filter_complex "subtitles={}" {}'.format(file_in,file_srt,file_out))


if __name__ == "__main__":
    
        # start_time = time.time()
        start_time = datetime.now()

        # Lấy ra đường dẫn chứa file
        path = os.path.dirname(directory) + '/' 
        # Lấy ra tên file nhập vào có cả duôi file
        file = os.path.basename(directory)

        # Lấy ra tên file
        name1 = os.path.splitext(file)
        name = name1[0]
        
        
        # if not (os.path.exists(path)):
        #     os.mkdir(path) 
        mp4_to_wav(path+file,path,name)
        if not newname:
            newname = name
        
        if noises:
            # Giảm nhiễu dùng thuật toán deepfilter
            if noises == 'deep':
                noise_deepfilternet(path+name+'.wav',path)
                deep = '_DeepFilterNet2.wav'
                rename(path+name+deep,path+newname+'.wav')
                # wav_to_flac(path+newname+'.wav',path+newname+'.flac')

                pass
            # Giải thuật giảm nhiễu Noisereduce (không cố định)
            elif noises == 'noise':
                noise_reduce(path+name+'.wav',path+newname+'.wav')
                # wav_to_flac(path+newname+'.wav',path+newname+'.flac')
            else:
            # Không chọn giải thuật
                rename(path+name+'.wav',path+newname+'.wav')
                pass
        source = path+newname+'.wav'
        

        # Tạo phụ đề
        createsub.main(source,lang_in,lang_out)
        # if os.path.exists(path+newname+'.wav'):
        #     os.remove(path+newname+'.wav')
        if path_txt:
            srt_to_txt(path+newname+'.srt',path_txt,newname)
        else:
            srt_to_txt(path+newname+'.srt',path,newname)
        # Gộp phụ đề với FFmpeg
        if lang_in == lang_out:
            if name != newname:
                videoOutput(path+file,path+newname+'.srt',path+newname+'.mp4')
            else:
                videoOutput(path+file,path+newname+'.srt',path+newname+'_output.mp4')
        else:
            if name != newname:
                videoOutput(path+file,path+newname+'_translated.srt',path+newname+'.mp4')
            else:
                videoOutput(path+file,path+newname+'_translated.srt',path+newname+'_output.mp4')


        
        # end_time = time.time()
        end_time = datetime.now()

        print(str(end_time-start_time))

        print("Tạo phụ đề thành công")
        







