import pysrt

def srt_to_txt(file,out_file,name):
    subs = pysrt.open(file)

    with open(out_file+'/'+name+'.txt','w',encoding='utf-8') as f:
        for sub in subs:
            f.write(sub.text.lower()+' ')

