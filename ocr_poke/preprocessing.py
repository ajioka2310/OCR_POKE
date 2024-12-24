"""
画像・文字列の前処理を行う
"""

import os
import re
import time
from PIL import Image
import cv2
from config import INPUT_IMAGE_PATH, INPUT_LOCK_PATH, CLIPPED_IMAGES_PATH  # Update this import
import logging

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def wait_for_file(file_path, lock_path, timeout=10):
    start_time = time.time()
    while os.path.exists(lock_path):
        if time.time() - start_time > timeout:
            raise TimeoutError(f"ロック解除を待つ間にタイムアウトしました: {lock_path}")
        logger.debug("ファイルがロックされています。解除を待っています...")
        time.sleep(0.05)


def clip_image(clip_config,debug=False):
    """
    画像をクリップする
    Args:
        coordinates (list): クリップする領域の座標リスト
        image_name (str): 画像の名前
        debug (bool): デバッグモードかどうか

    Returns:
        None
    """
    wait_for_file(INPUT_IMAGE_PATH, INPUT_LOCK_PATH)
    image = Image.open(INPUT_IMAGE_PATH)
    
    for image_name, coord in clip_config.items():
        logger.debug(f"clip_image started with image_name: {image_name}")
        # 指定された座標で画像をクロップする
        cropped_image = image.crop((
            coord[0]["x1"],
            coord[0]["y1"],
            coord[0]["x2"],
            coord[0]["y2"]
        ))
        if debug:
            output_path = CLIPPED_IMAGES_PATH
        else:
            output_path = CLIPPED_IMAGES_PATH  # Use CLIPPED_IMAGES_PATH from config
        filename = f"{image_name}.png"
        # 画像を保存
        if not os.path.exists(output_path):
            os.makedirs(output_path)  # 保存先ディレクトリがなければ作成する
        full_path = os.path.join(output_path, filename)
        cropped_image.save(full_path)
    logger.debug(f"clip_image completed for image_name: {image_name}")
        

def resize_image(image_path, output_path, size):
    """
    画像をリサイズする
    Args:
        image_path (str): 入力画像のパス
        output_path (str): 出力画像のパス
        size (tuple): リサイズ後のサイズ (width, height)

    Returns:
        None
    """
    logger.debug(f"resize_image started with image_path: {image_path}, output_path: {output_path}, size: {image.size} to {size}")
    image = Image.open(image_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)
    logger.debug(f"resize_image completed for image_path: {image_path}")


def remove_noise_image(img):
    """
    ノイズ除去を行う
    Args:
        img(numpy.ndarray): ノイズ除去前の画像

    Returns:
        numpy.ndarray: ノイズ除去後の画像
    """
    logger.debug("remove_noise_image started")
    img = cv2.GaussianBlur(img, (5, 5), 0)  
    _, img = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    logger.debug("remove_noise_image completed")
    return img


def remove_noise_str(string):
    """
    ノイズ除去を行う
    Args:
        string (str): 対象文字列

    Returns:
        str: ノイズ除去後の文字列
    """
    logger.debug("remove_noise_str started")
    result = re.sub(r"[^一-龥ぁ-んァ-ンa-zA-Z0-9]", "", string)
    logger.debug("remove_noise_str completed")
    return result
