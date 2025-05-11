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

if (!fs.existsSync('uploads')) {
  fs.mkdirSync('uploads');
}

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

app.post('/upload', upload.single('audio'), (req, res) => {
  if (!req.file) {
    console.log('❌ Không nhận được file!');
    return res.status(400).json({ error: 'No file uploaded' });
  }

  const filePath = req.file.path;
  console.log('📥 File nhận được:', filePath);

  const whisperCmd = `python ../voice-server/whisper.py "${filePath}"`;

  exec(whisperCmd, (error, stdout, stderr) => {
    if (error) {
      console.error('❌ Whisper lỗi:', stderr);
      return res.status(500).json({ error: 'Whisper failed' });
    }

    console.log('🧠 Whisper kết quả:', stdout.trim());

    // Trả về dữ liệu JSON đúng định dạng
    res.setHeader('Content-Type', 'application/json');
    res.status(200).json({ transcript: stdout.trim() });
  });
});

app.listen(PORT, () => {
  console.log(`✅ UNIMA API server is running at http://localhost:${PORT}`);
});
