"""
デバック用関数
"""
import logging
import os
import cv2
from matplotlib import pyplot as plt
from config import DEBUG_PATH

# ロガーの設定
logger = logging.getLogger(__name__)

def save_debug_image(image, filename="debug_image.png"):
    """
    デバッグ用に画像を保存する。
    Args:
        image (numpy.ndarray): 保存する画像
        output_path (str): 保存先ディレクトリのパス
        filename (str): 保存するファイル名
    """
    if not os.path.exists(DEBUG_PATH):
        os.makedirs(DEBUG_PATH)  # 保存先ディレクトリがなければ作成する
    full_path = os.path.join(DEBUG_PATH, filename)
    cv2.imwrite(full_path, image)
    logger.debug(f"デバッグ画像を保存しました: {full_path}")
