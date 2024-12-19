import cv2
import os
from matplotlib import pyplot as plt

def show_image(image, title="Image"):
    """
    デバッグ用に画像を表示する。
    Args:
        image (numpy.ndarray): 表示する画像
        title (str): 表示するウィンドウのタイトル
    """
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.axis("off")
    plt.show()

def save_debug_image(image, output_path, filename="debug_image.png"):
    """
    デバッグ用に画像を保存する。
    Args:
        image (numpy.ndarray): 保存する画像
        output_path (str): 保存先ディレクトリのパス
        filename (str): 保存するファイル名
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)  # 保存先ディレクトリがなければ作成する
    full_path = os.path.join(output_path, filename)
    cv2.imwrite(full_path, image)
    print(f"デバッグ画像を保存しました: {full_path}")
