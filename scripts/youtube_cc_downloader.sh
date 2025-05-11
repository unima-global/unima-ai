# youtube_cc_downloader.sh – Tải video có giấy phép CC từ YouTube

# Cài đặt công cụ cần thiết (chạy 1 lần)
# pip install yt-dlp

mkdir -p datasets/youtube_cc
cd datasets/youtube_cc

# Thay link bên dưới bằng video có giấy phép CC
URL="https://www.youtube.com/watch?v=VIDEO_ID"

# Tải video và audio
yt-dlp -f bestaudio --write-auto-sub --extract-audio --audio-format mp3 "$URL"

# Tệp tải về sẽ gồm:
# - file .mp3 (audio)
# - file .vtt (phụ đề auto)

# Có thể dùng whisper hoặc bất kỳ công cụ nào để tạo transcript
# Ví dụ:
# whisper downloaded_audio.mp3 --language vi --model base --output_format txt
