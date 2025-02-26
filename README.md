# DJI Thermal 画像変換ツール

このプロジェクトは、DJIのサーマルカメラで撮影した画像をTIFF形式に変換するPythonスクリプトです。  
**DJI Thermal SDK** を使用して、正確な温度データを取得・処理します。

## 🔧 必要な環境
- Python 3.x
- OpenCV
- NumPy
- **DJI Thermal SDK**

## 🛠 DJI Thermal SDK のインストール
1. DJIの公式サイトから **DJI Thermal SDK** をダウンロードします。
2.　SDK_DIRを設定 例：os.path.expanduser("~/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64")

## 🚀 変換スクリプトの実行

thermal_imagesにDJI画像を格納し、convert_dji_thermal.pyを実行する


❌ ERROR processing file: DJI_20250206153552_0001_T.JPG
   Error message: [Errno 13] Permission denied: '/home/kis/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64/dji_irp'

というエラー時は実行権限を付与

chmod +x ~/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64/dji_irp



error while loading shared libraries: libdirp.so: cannot open shared object file: No such file or directory

というエラー時はパスを追加

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64' >> ~/.bashrc
source ~/.bashrc

