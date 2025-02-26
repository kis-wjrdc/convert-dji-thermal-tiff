import rasterio
import numpy as np
import matplotlib.pyplot as plt

# 変換後の TIFF ファイルのパス
tif_file = "model1.tif"

# TIFF 画像を開く
with rasterio.open(tif_file) as src:
    thermal_image = src.read(1)  # 1番目のバンドを取得（温度データ）
    transform = src.transform    # 座標変換情報
    width, height = src.width, src.height

# 画像を表示
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(thermal_image, cmap="inferno")

# 等高線を描画
contour = ax.contour(thermal_image, levels=10, colors='white', linewidths=0.8)
ax.clabel(contour, inline=True, fontsize=8, fmt="%.1f")  # ラベルを追加

ax.set_title("Thermal Image with Contours - Click to get temperature")

# カラーバーを追加
cbar = fig.colorbar(im, ax=ax)
cbar.set_label("Temperature (°C)")

# クリックイベントの処理
def onclick(event):
    if event.xdata is None or event.ydata is None:
        return
    
    # 画像内の座標に変換
    col, row = int(event.xdata), int(event.ydata)
    
    # 温度データを取得
    if 0 <= row < height and 0 <= col < width:
        temperature = thermal_image[row, col]
        print(f"Cursor Position: ({col}, {row}) | Temperature: {temperature:.2f}°C")
    else:
        print("Clicked outside of the image")

# クリックイベントを登録
fig.canvas.mpl_connect("button_press_event", onclick)

plt.show()
