import os
import glob
import subprocess
import rasterio
import numpy as np
from tqdm import tqdm

# **DJI SDK のパスを設定**
SDK_DIR = os.path.expanduser("~/Downloads/dji_thermal_sdk_v1.7_20241205/utility/bin/linux/release_x64")
DJI_IRP = os.path.join(SDK_DIR, "dji_irp")

# **画像フォルダのパス**
IN_DIR = os.path.expanduser("~/DJI THERMAL/thermal_images")
OUT_DIR = os.path.join(IN_DIR, "ir_calib")
os.makedirs(OUT_DIR, exist_ok=True)

# **処理対象の画像を取得**
in_files = glob.glob(os.path.join(IN_DIR, "*_T.JPG"))

# **画像が見つからない場合**
if not in_files:
    print(f"❌ No images found in {IN_DIR}.")
    exit(1)

print(f"### Processing {len(in_files)} thermal images ###")

for i, in_path in enumerate(tqdm(in_files, desc="Processing images")):
    try:
        filename = os.path.basename(in_path)
        raw_path = os.path.join(OUT_DIR, os.path.splitext(filename)[0] + ".raw")
        tif_path = os.path.join(OUT_DIR, os.path.splitext(filename)[0] + ".tif")

        print(f"\n--- Processing file {i+1} of {len(in_files)}: {filename} ---")

        # **Step 1: DJI SDK で温度データを変換**
        print("Step 1: Converting to Celsius using DJI SDK...")
        cmd = [
            DJI_IRP, "-s", in_path, "-a", "measure", "-o", raw_path,
            "--measurefmt", "float32",
            "--emissivity", "1.0",
            "--humidity", "70",
            "--distance", "5"
        ]
        subprocess.run(cmd, check=True)

        # **Step 2: .raw ファイルを .tif に変換**
        print("Step 2: Converting .raw to .tif...")
        
        # **画像サイズを取得**
        with rasterio.open(in_path) as src:
            width, height = src.width, src.height

        # **raw ファイルを NumPy 配列に変換**
        raw_data = np.fromfile(raw_path, dtype=np.float32)
        image_matrix = raw_data.reshape((height, width))

        # **TIFF に保存**
        with rasterio.open(
            tif_path, "w",
            driver="GTiff",
            height=height,
            width=width,
            count=1,
            dtype=np.float32
        ) as dst:
            dst.write(image_matrix, 1)

        print(f"✔ Processing complete for: {filename}")

    except Exception as e:
        print(f"❌ ERROR processing file: {filename}")
        print(f"   Error message: {e}")

# **不要な .raw ファイルを削除**
print("\n### Cleaning up temporary files ###")
for file in os.listdir(OUT_DIR):
    if file.endswith(".raw"):
        os.remove(os.path.join(OUT_DIR, file))

print("\n✔ All processing completed!")
