# fetch_mozilla.py – Tải dữ liệu Mozilla Common Voice (tiếng Việt)

import os
import requests
import zipfile

def download_common_voice(lang="vi", version="11.0"):
    url = f"https://commonvoice.mozilla.org/vi/datasets"
    output_zip = f"common_voice_{lang}_v{version}.zip"
    if not os.path.exists(output_zip):
        print("🔽 Đang tải dữ liệu...")
        r = requests.get("https://voice-prod.brl.nyc3.cdn.digitaloceanspaces.com/cv-corpus-11.0-2022-09-21/vi.tar.gz", stream=True)
        with open(output_zip, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("✅ Tải xong!")
    else:
        print("✅ File đã tồn tại!")

    print("📦 Đang giải nén...")
    os.makedirs("datasets", exist_ok=True)
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall("datasets")
    print("✅ Giải nén hoàn tất!")

if __name__ == "__main__":
    download_common_voice()
