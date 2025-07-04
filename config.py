import os

# 기본 디렉토리
# abspath->절대경로.  c드라이브부터 출력


# __00 < 내장변수
print(__file__)
# c:\Users\d\course_video\16_ai\ai-model-development\backend\config.py 

print(os.path.dirname(__file__))
# dirname - directory name


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# print("base_dir >>>", BASE_DIR)
# base_dir >>> c:\Users\d\course_video\16_ai\ai-model-development\backend


""" 폴더 경로 """
VIDEO_DIR = os.path.join(BASE_DIR, "source", "video")
# 경로 뒤에 source 폴더, 그 안에 있는 "video파일" 추가한다는 뜻
AUDIO_DIR = os.path.join(BASE_DIR, "source", "audio")
SUBTITLE_DIR = os.path.join(BASE_DIR, "source", "subtitle")

file_name = "test"
VIDEO_FILE = os.path.join(VIDEO_DIR, f"{file_name}.mp4")
AUDIO_FILE = os.path.join(AUDIO_DIR, f"{file_name}.wav")
SUBTITLE_TEXT_FILE = os.path.join(SUBTITLE_DIR, f"{file_name}.txt")
SUBTITLE_JSON_FILE = os.path.join(SUBTITLE_DIR, f"{file_name}.json")
SUBTITLE_SRT_FILE = os.path.join(SUBTITLE_DIR, f"{file_name}.srt")

print("VIDEO_FILE >>>>>>>", VIDEO_FILE)
print("AUDIO_FILE >>>>>>>", AUDIO_FILE)
print("SUBTITLE_TEXT_FILE >>>>>>>",SUBTITLE_TEXT_FILE)
print("SUBTITLE_JSON_FILE >>>>>>>",SUBTITLE_JSON_FILE)
