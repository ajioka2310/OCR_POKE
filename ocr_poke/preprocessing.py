"""
画像の前処理を行う
"""

import re
import cv2


def remove_noise_image(image_path):
    """
    ノイズ除去を行う
    Args:
        image_path (str): 画像ファイルのパス

    Returns:
        numpy.ndarray: ノイズ除去後の画像
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (5, 5), 0)  
    _, img = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    return img


def remove_noise_str(string):
    """
    ノイズ除去を行う
    Args:
        string (str): 対象文字列

    Returns:
        str: ノイズ除去後の文字列
    """
    return re.sub(r"[^一-龥ぁ-んァ-ンa-zA-Z0-9]", "", string)
