import os
from datetime import datetime, timedelta

import whisper

from config import AUDIO_FILE, SUBTITLE_DIR, VIDEO_FILE


def format_time(seconds):

    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    seconds = int(td.total_seconds() % 60)
    milliseconds = int((td.total_seconds() % 1) * 1000)


    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'


def generate_srt_from_movie(input_video_path, subtitle_dir):

    # 오디오 > segments
    print("\n\n1. 영상 -> whisper로 텍스트 변환")

    # 모델 생성
    model = whisper.load_model("small")

    #텍스트 변환
    result = model.transcribe(input_video_path)

    # segments만 저장 
    segments = result["segments"]

    # segments -> srt 저장
    print("\n\n 2. segments -> srt 저장")

    ### 고유한 파일명 생성
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    subtitle_srt_path = os.path.join(subtitle_dir, f"subtitle_{timestamp}.srt")

    with open(SUBTITLE_DIR, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg["start"])
            end = format_time(seg["end"])
            text = seg["text"].strip()

            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")

        print(f"3. [srt 생성 완료] -> {SUBTITLE_DIR}")
    return subtitle_srt_path
 
# 함수 호출
if __name__ == "__main__":
    print("AUdioFIle:", AUDIO_FILE)           
    print("VideoFIle:", VIDEO_FILE)
    print("SUBTITLE_DIR:", SUBTITLE_DIR)
    generate_srt_from_movie(VIDEO_FILE,SUBTITLE_DIR)