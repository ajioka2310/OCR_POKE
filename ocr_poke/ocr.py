from PIL import Image
import pytesseract
from .preprocessing import remove_noise
from .debug_utils import show_image, save_debug_image
import cv2
import numpy as np


def ocr_from_image(image_path, debug=False):
    """
    画像から文字列を抽出する
    Args:
        image_path (str): 画像ファイルのパス
        debug (bool): デバッグ情報を表示するかどうか

    Returns:
        str: 抽出された文字列
    """
    try:
        # ノイズ除去を実行
        processed_image = remove_noise(image_path)

        if debug:
            show_image(processed_image, title="Processed Image")
            save_debug_image(processed_image, "./debug", "processed_image.png")

        # OpenCVの画像をPILの画像に変換
        image = Image.fromarray(processed_image)
        new_size = tuple(2 * x for x in image.size)  # 解像度を2倍にする
        image = image.resize(new_size, Image.Resampling.LANCZOS)
        image = image.point(lambda x: 255 if x < 128 else 0, "1")  # 二値化

        if debug:
            save_debug_image(
                cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR),
                "./debug",
                "resized_image.png",
            )

        # OCRを実行
        text = pytesseract.image_to_string(image, lang="jpn")

        return text
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return ""
