<h6 align="left">Author: <a href="https://github.com/toandokhanh">Do Khanh Toan<a/> </h6>

# VidSubWizard
VidSubWizard is a powerful application designed to simplify the process of creating subtitles for videos. With its user-friendly interface and advanced algorithms, VidSubWizard ensures precise and accurate subtitle generation, making your video content accessible to a wider audience. Combined with <a href="https://github.com/toandokhanh/Gender-classification"> Gender-classification <a/> we create a Voice-based Gender Classification System which is an area of research important for many applications in different fields. It is commonly used in speech recognition, forensic science, and social science. In the film industry, the use of both male and female voices in dub films can provide a more authentic and diverse experience for audiences. Along with noise removal methods with Noise-reduce and DeepFilterNet. Tests show that DeepFilterNet is the most effective noise removal technique, with a similarity score of 0.8442, followed by Noisereduce with 0.7339. In addition, the Support Vector Machine (SVM) and K-Nearest Neighbor (KNN) are more efficient in gender classification using speech-based signals with an average accuracy of 0, respectively. 8715 and 0.7773 versus Logistic Regression and Random Forest. The work is expected to produce a voiceover video using male and female voices.   
# How well does it work?
![image](https://github.com/toandokhanh/VidSubWizard/assets/98395447/6547ff7f-2f59-4439-928a-2d003c25066e)

The general procedure to reduce noise and create subtitles for videos, as shown in the image above, includes the following steps. First, we collect videos for testing. Then we use the FFmpeg Library to extract the audio from the video files. Next, to enhance the subtitle generator, we choose DeepFilterNet (Schroter2022) or Noisereduce (Sainburg2020) to remove the noise in the audio files. We then convert the audio file format from WAV to FLAC to comply with the Speech-to-Text API requirements. Finally, we evaluate the similarity between the generated subtitles and the original text. In addition, we perform voice-based gender classification to support voiced videos for further processing.
# How accurate is it?
##### Results Comparison of Noise Removal Algorithms

| Algorithms     | Length of Original Script | Detected Length | Similarity Score |
| -------------- | ------------------------ | --------------- | ---------------- |
| Do not use     | 283                      | 142             | 0.7266           |
| Noisereduce    | 283                      | 171             | 0.7339           |
| Deepfilternet  | 283                      | 184             | 0.8442           |
##### Results of Various Voice Types

|                     | Length of Original Script | Detected Length | Similarity Score |
| ------------------- | ------------------------ | --------------- | ---------------- |
| Natural voice       | 23949                    | 13767           | 0.7066           |
| Machine-based voice | 27900                    | 16598           | 0.8173           |

# How it's used?
##### Install all module install 
    conda install Pyaudio

    pip3 install -r requirements.txt
##### Run the web application (Flask) and automatically generate subtitles:
    python3 video.py
##### Database setup:
- Import the database file with the same name using Xampp Mysql.
- If you change the database name, update it in video.py file as well.
##### Update the database name:
- In video.py, modify the line app.config['MYSQL_DATABASE_DB'] = 'new_database_name'.
- Database: subtitle.sql
##### Use the following command-line arguments:
    -s: source language (default is vi)
    -d: destination language (default is vi)
    -n: destination language (default is vi)
    -noise: noise reduction algorithm (choose from two algorithms below)
=> deep: Use the DeepFilter algorithm.
=> noise: Use the Noisereduce algorithm.
##### Example command to generate subtitles from Vietnamese (vi) to English (en) using the DeepFilterNet algorithm:
    python3 phude.py 'url' -s vi -d en -n video2022 -noise deep
##### Example command to generate subtitles from Vietnamese (vi) to Vietnamese (vi) using the Noisereduce algorithm:
    python3 phude.py t2/video.mp4 -s vi -n video2022 -noise noise
##### Example command to generate subtitles from English (en) to Vietnamese (vi) without noise reduction:
    python3 phude.py t2/video.mp4 -s vi -d en -n video2022
##### Calculate cosine similarity percentage:
    python3 comparison_log -train train -compare template_log
- train: The directory containing generated subtitle files to compare with the original content.
- compare: The directory containing the original content files for comparison.

##### Folder structure:

    └───database
        ├───query.sql
        ├───subtitle.sql (main)
    └───static (web)
    └───sub 
    └───templates (web)
    └───comparison_log.py (cosine)
    └───phude.py (subtile code)
    └───video.py (run web)
    └───venv
    └───t2 (Where to save videos when uploading videos from the web)
    └───data
        └───Normal (the output of video subtitles has no noise)
            ├───video.mp4
            ├───video.srt
            ├───video.txt
            ├───video.wav
        └───Noisy (folder containing videos with noise)
            ├───deep (subtitle output runs deep algorithm)
            ├───noise (subtitle output runs noise algorithm)
            ├───not (subtitle output runs without algorithm)
                ├───video.mp4 (Original video with noise)
##### User Interface Design:
![image](https://github.com/toandokhanh/VidSubWizard/assets/98395447/b0df8aa0-36c2-434d-8d05-052854b605f1)
![image](https://github.com/toandokhanh/VidSubWizard/assets/98395447/393fc50f-ecdd-4d9e-8065-0c6fa24d29aa)
![image](https://github.com/toandokhanh/VidSubWizard/assets/98395447/2ac27d37-193c-484b-aa81-7ffbe0122442)
![image](https://github.com/toandokhanh/VidSubWizard/assets/98395447/21dcbeb9-26ea-486f-a148-a31dc15e45ca)
![image](https://github.com/toandokhanh/VidSubWizard/assets/98395447/797a02dc-e256-4a60-9332-9bdea77dea28)
![image](https://github.com/toandokhanh/VidSubWizard/assets/98395447/98e4d1db-456b-4b44-8b85-69c9be112886)
# Citation
        @inproceedings{nguyen2023removal,
          title={Removal of Various Noise Types and Voice-Based Gender Classification for Dubbed Videos},
          author={Nguyen, Hai Thanh and Do, Toan Khanh and Le, Khoa Viet and Nguyen, Tong Thanh and Luong, Huong Hoang},
          booktitle={International Conference on Future Data and Security Engineering},
          pages={92--103},
          year={2023},
          organization={Springer}
        }

        DOI: https://doi.org/10.1007/978-981-99-8296-7_7
