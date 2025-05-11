const express = require('express');
const multer = require('multer');
const cors = require('cors');
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.static('uploads'));

// Đảm bảo thư mục uploads tồn tại
if (!fs.existsSync('uploads')) {
  fs.mkdirSync('uploads');
}

// Cấu hình lưu file
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    const uniqueName = 'voice_' + Date.now() + path.extname(file.originalname);
    cb(null, uniqueName);
  },
});
const upload = multer({ storage });

// Route nhận file từ client
app.post('/upload', upload.single('audio'), (req, res) => {
  if (!req.file) {
    console.log('❌ Không nhận được file!');
    return res.status(400).json({ error: 'No file uploaded' });
  }

  const filePath = req.file.path;
  console.log('📥 File nhận được:', filePath);

  // Gọi Whisper xử lý
  const whisperCmd = `python ../voice-server/whisper.py "${filePath}"`;

  exec(whisperCmd, (error, stdout, stderr) => {
    if (error) {
      console.error('❌ Whisper lỗi:', stderr);
      return res.status(500).json({ error: 'Whisper failed' });
    }

    console.log('🧠 Whisper kết quả:', stdout.trim());
    res.json({ transcript: stdout.trim() });
  });
});

app.listen(PORT, () => {
  console.log(`✅ UNIMA API server is running at http://localhost:${PORT}`);
});
