"""
OCRのエンジン部分
"""

import logging
from PIL import Image
import pytesseract  # type: ignore
import numpy as np
from .preprocessing import remove_noise_image
from .debug_utils import save_debug_image
import cv2

# ロガーの設定
logger = logging.getLogger(__name__)

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
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if debug:
            save_debug_image(image,"preprocessed_image.png")
            logger.debug("Preprocessed image saved as preprocessed_image.png")
        # # ノイズ除去を実行
        # image = remove_noise_image(image)
        # OpenCVの画像をPILの画像に変換
        image = Image.fromarray(image)
        new_size = tuple(3 * x for x in image.size)  # 解像度を2倍にする
        logger.debug(f"resize_image size: {image.size} to {new_size}")
        image = image.resize(new_size, Image.Resampling.LANCZOS)

        if debug:
            # PIL画像をNumPy配列に戻して `processed_image` に再代入
            save_debug_image(
                np.array(image).astype(np.uint8),
                "processed_image.png",
            )
            logger.debug("Processed image saved as processed_image.png")

        # OCRを実行
        text = pytesseract.image_to_string(image, lang="jpn")
        logger.debug("OCR processing completed successfully")

        return text
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}")
        return ""
