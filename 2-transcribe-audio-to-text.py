# # 오디오 텍스트 변환
import os
import whisper
import json
from config import  AUDIO_FILE,SUBTITLE_DIR, SUBTITLE_JSON_FILE, SUBTITLE_TEXT_FILE


# print("1. 모델 불러오기")
# # tiny, base, small, medium, large
model = whisper.load_model("small")

# # 오디오 파일 텍스트 변환

# print("2.1 오디오 > 텍스트 변환 전")

# audio_path = "./source/audio/test.wav"
result = model.transcribe(AUDIO_FILE)

print("2.1 오디오 > 텍스트 변환 후")


#변환된 텍스트 출력
print("3. 변환된 텍스트 출력")
print(result)

# 텍스트 파일 저장
# with 문 사용
# source/subtitle 폴더 내 test.txt 파일 생성
print("4.1 폴더 생성")

# output_dir = "./source/subtitle"
os.makedirs(SUBTITLE_DIR, exist_ok=True)

print("5.1 파일 경로 생성시작")
# output_path = os.path.join(output_dir, "test.txt")
# output_path_json = os.path.join(output_dir, "test.json")

print("6.1 텍스트 파일로 저장 시작")

with open(SUBTITLE_TEXT_FILE, "w", encoding="utf-8") as f:
    f.write(result["text"]) 
print("6.1 텍스트 파일로 저장 완료")

print("6.2 text랑 segments 각 파일로 저장 시작")

with open(SUBTITLE_JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(result["segments"], f, indent=2, ensure_ascii=False)