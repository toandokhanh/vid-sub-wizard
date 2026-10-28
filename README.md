# VidSubWizard

A 2023 research prototype studying noise reduction for automatic video subtitles and voice-label classification for dubbing. The project compares Noisereduce and DeepFilterNet and includes a Flask demonstration interface.

## Historical findings

The original experiments reported cosine-similarity scores of 0.7266 without noise reduction, 0.7339 with Noisereduce and 0.8442 with DeepFilterNet. These measure text similarity in the recorded experiment; they are not word-error rate, human subtitle-quality ratings or a universal speech-recognition benchmark. Results were not recomputed during maintenance.

The related voice-classification experiments reported mean accuracy of 0.8715 for SVM and 0.7773 for KNN. Dataset provenance and split design must accompany any reuse of these numbers. See [Gender-classification](https://github.com/toandokhanh/Gender-classification).

## CLI experiments

`phude.py` generates subtitles, `comparison_log.py` compares transcripts, and `sub/` contains the legacy recognition/translation implementation.

```sh
python3 phude.py data/input.mp4 -s vi -d en -n demo-output -noise deep
```

The CLI needs FFmpeg, the original Python/audio dependencies and a configured `GOOGLE_SPEECH_API_KEY` for the legacy recognizer. A modern provider integration may require additional changes.

## Local web demo

Copy `.env.example` to `.env`; set a new random `SECRET_KEY` of at least 32 characters and your local database credentials. Import `database/subtitle.sql` into a disposable local database. User rows and processing history have been removed from the dump. The password column accommodates modern password hashes.

```sh
python3 video.py
```

The server binds to `127.0.0.1:5003`. Create a new local demo account; legacy MD5/plaintext accounts must be reset and are no longer accepted. Forms use CSRF protection. Uploads use generated filenames, have a 256 MiB limit and check ownership before media edits, downloads and deletion.

Dependency installation, MySQL migration and media processing were not performed during the 2026 cleanup. Preserve your own dataset separately; use synthetic demo accounts and media for public demonstrations.

## Research citation

@inproceedings{nguyen2023removal,
          title={Removal of Various Noise Types and Voice-Based Gender Classification for Dubbed Videos},
          author={Nguyen, Hai Thanh and Do, Toan Khanh and Le, Khoa Viet and Nguyen, Tong Thanh and Luong, Huong Hoang},
          booktitle={International Conference on Future Data and Security Engineering},
          pages={92--103},
          year={2023},
          organization={Springer}
        }

        DOI: https://doi.org/10.1007/978-981-99-8296-7_7

See [third-party notices](THIRD_PARTY_NOTICES.md). Selected original UI screenshots can be found in the repository history; links and external demos have not been revalidated.
