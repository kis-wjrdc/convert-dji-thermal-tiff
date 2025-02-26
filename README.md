# DJI Thermal 画像変換ツール

このプロジェクトは、DJIのサーマルカメラで撮影した画像をTIFF形式に変換するPythonスクリプトです。  
**DJI Thermal SDK** を使用して、正確な温度データを取得・処理します。

---

## 🔧 必要な環境
- Python 3.x
- OpenCV
- NumPy
- **DJI Thermal SDK**

---

## 🛠 DJI Thermal SDK のインストール
1. DJIの公式サイトから **DJI Thermal SDK** をダウンロードします。
2. `SDK_DIR` を設定します。  
   例：
   ```python
   os.path.expanduser("~/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64")

🚀 変換スクリプトの実行

    thermal_images フォルダに DJI 画像を格納します。
    以下のコマンドを実行して、TIFF 変換を行います。

    python convert_dji_thermal.py

❌ よくあるエラーと対処方法

1️⃣ Permission denied エラー

エラー例：

ERROR processing file: DJI_20250206153552_0001_T.JPG
Error message: [Errno 13] Permission denied: '/home/kis/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64/dji_irp'

✅ 対処方法：実行権限を付与

chmod +x ~/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64/dji_irp

2️⃣ libdirp.so の読み込みエラー

エラー例：

error while loading shared libraries: libdirp.so: cannot open shared object file: No such file or directory

✅ 対処方法：ライブラリのパスを追加

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64' >> ~/.bashrc
source ~/.bashrc

📝 ライセンス

MIT License
