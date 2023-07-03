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
# Reference source

1. Lei, J., Yu, L., Berg, T.L., Bansal, M. (2020). [TVR: A large-scale dataset for video-subtitle moment retrieval](https://doi.org/10.1007/978-3-030-58589-1_27). In: Computer Vision – ECCV 2020, Springer International Publishing.

2. Elshahaby, H., Rashwan, M. (2021). [An end to end system for subtitle text extraction from movie videos](https://doi.org/10.1007/s12652-021-02951-1). Journal of Ambient Intelligence and Humanized Computing, 13(4), 1853–1865.

3. Tassano, M., Delon, J., Veit, T. (2019). [DVDNET: A fast network for deep video denoising](https://doi.org/10.1109/icip.2019.8803136). In: 2019 IEEE International Conference on Image Processing (ICIP), IEEE.

4. Nguyen, H.T., Thanh, T.N.L., Ngoc, T.L., Le, A.D., Tran, D.T. (2022). [Evaluation on noise reduction in subtitle generator for videos](https://doi.org/10.1007/978-3-031-08819-3_14). In: Innovative Mobile and Internet Services in Ubiquitous Computing, Springer International Publishing.

5. Alnuaim, A.A., Zakariah, M., Shashidhar, C., Hatamleh, W.A., Tarazi, H., Shukla, P.K., Ratna, R. (2022). [Speaker gender recognition based on deep neural networks and ResNet50](https://doi.org/10.1155/2022/4444388). Wireless Communications and Mobile Computing, 2022, 1–13.

6. Ertam, F. (2019). [An effective gender recognition approach using voice data via deeper LSTM networks](https://doi.org/10.1016/j.apacoust.2019.07.033). Applied Acoustics, 156, 351–358.

7. Kabil, S.H., Muckenhirn, H., Magimai-Doss, M. (2018). On learning to identify genders from raw speech signal using CNNs. In: Interspeech, 287-291.

8. Shrawankar, U., Thakare, V. (2010). [Noise estimation and noise removal techniques for speech recognition in adverse environment](https://doi.org/10.1145/3479162.3479172). In: Intelligent Information Processing V: 6th IFIP TC 12 International Conference, IIP 2010, Springer.

9. Perez-Martin, J., Bustos, B., Guimarães, S.J.F., Sipiran, I., Pérez, J., Said, G.C. (2022). [A comprehensive review of the video-to-text problem](https://doi.org/10.1007/s10462-021-10104-1). Artificial Intelligence Review, 55(5), 4165–4239.

10. Domingo, I.V.R., Mamanta, M.N.G., Regpala, J.T.S. (2021). [FILENG: An automatic English subtitle generator from Filipino video clips using hidden Markov model](https://doi.org/10.1145/3479162.3479172). In: The 2021 9th International Conference on Computer and Communications Management, ACM.

11. Yim, J. (2015). [Design of a subtitle generator](https://doi.org/10.14257/astl.2015.117.17). In: Advanced Science and Technology Letters, Science & Engineering Research Support Society.

12. Halpern, Y., Hall, K., Schogol, V., Riley, M., Roark, B., Skobeltsyn, G., Bäuml, M. (2016). [Contextual Prediction Models for Speech Recognition](https://doi.org/10.1109/icassp.2016.7472483). Proc. Interspeech 2016, 2338–2342.

13. Lagos, D. (2019). [Hearing gender: Voice-based gender classification processes and transgender health inequality](https://doi.org/10.1177/0003122419872504). American Sociological Review, 84(5), 801–827.

14. Harb, H., Chen, L. (2003). [Gender identification using a general audio classifier](https://doi.org/10.1109/icme.2003.1221721). In: 2003 International Conference on Multimedia and Expo, IEEE.

15. Mamyrbayev, O., Toleu, A., Tolegen, G., Mekebayev, N. (2020). [Neural architectures for gender detection and speaker identification](https://doi.org/10.1080/23311916.2020.1727168). Cogent Engineering, 7(1), 1727168.

16. Priya, E., S, J.P., Reshma, P.S., S, S. (2022). [Temporal and spectral features based gender recognition from audio signals](https://doi.org/10.1109/ic3iot53935.2022.9767929). In: 2022 International Conference on Communication, Computing and Internet of Things (IC3IoT), IEEE.

17. Schroter, H., Escalante-B, A.N., Rosenkranz, T., Maier, A. (2022). [Deepfilternet: A low complexity speech enhancement framework for full-band audio based on deep filtering](https://doi.org/10.1109/icassp43922.2022.9747055). In: ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), IEEE.

18. Sainburg, T., Thielk, M., Gentner, T.Q. (2020). [Finding, visualizing, and quantifying latent structure across diverse animal vocal repertoires](https://doi.org/10.1371/journal.pcbi.1008228). PLOS Computational Biology, 16(10), e1008228.

19. Ardila, R., Branson, M., Davis, K., Henretty, M., Kohler, M., Meyer, J., Morais, R., Saunders, L., Tyers, F.M., Weber, G. (2019). [Common voice: A massively-multilingual speech corpus](https://arxiv.org/abs/1912.06670).

20. Wikipedia: [Nhận dạng tiếng nói](https://vi.wikipedia.org/wiki/Nh%E1%BA%ADn_d%E1%BA%A1ng_ti%E1%BA%BFng_n%C3%B3i) (2020).
