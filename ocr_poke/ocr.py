"""
OCRのエンジン部分
"""

from PIL import Image
import pytesseract  # type: ignore
import numpy as np
from .preprocessing import remove_noise_image
from .debug_utils import save_debug_image


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
        processed_image = remove_noise_image(image_path)
        print("processed_image", processed_image.shape, processed_image.dtype)
        if debug:
            save_debug_image(processed_image, "./debug", "processed_image.png")

        # OpenCVの画像をPILの画像に変換
        image = Image.fromarray(processed_image)
        new_size = tuple(2 * x for x in image.size)  # 解像度を2倍にする
        image = image.resize(new_size, Image.Resampling.LANCZOS)

        if debug:
            # PIL画像をNumPy配列に戻して `processed_image` に再代入
            save_debug_image(
                np.array(image).astype(np.uint8),
                "./debug",
                "resized_image.png",
            )

        # OCRを実行
        text = pytesseract.image_to_string(image, lang="jpn")

        return text
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return ""
