from moviepy.editor import VideoFileClip
from config import VIDEO_FILE, AUDIO_FILE

# input_video_path = "./source/video/test.mp4"
# output_video_path = "./source/audio/test.wav"


print("1. 영상에서 오디오 추출 시작")

# video = VideoFileClip(input_video_path)
video = VideoFileClip(VIDEO_FILE)

#video 에서 오디오 추출
video.audio.write_audiofile(AUDIO_FILE, fps=16000, nbytes=2, codec="pcm_s16le")

print("2. 오디오 추출 완료")



# config에서 1.1파일로 가져오기?
