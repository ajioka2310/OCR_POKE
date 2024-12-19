import pytesseract
from PIL import Image
import configparser
import os
import cv2
import numpy as np

def remove_noise(image_path):
    """
    ノイズ除去を行う
    Args:
        image_path (str): 画像ファイルのパス

    Returns:
        numpy.ndarray: ノイズ除去後の画像
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return img

def ocr_from_image(image_path):
    """
    画像から文字列を抽出する
    Args:
        image_path (str): 画像ファイルのパス

    Returns:
        str: 抽出された文字列
    """
    try:
        # ノイズ除去を実行
        processed_image = remove_noise(image_path)

        # OpenCVの画像をPILの画像に変換
        
        image = Image.fromarray(processed_image)
        new_size = tuple(2 * x for x in image.size)  # 解像度を2倍にする
        image = image.resize(new_size, Image.Resampling.LANCZOS)
        image = image.point(lambda x: 0 if x < 128 else 255, '1')  # 二値化

        # OCRを実行
        text = pytesseract.image_to_string(image, lang="jpn")

        return text
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return ""

if __name__ == "__main__":
    # Configファイルを読み込む
    config_path = os.path.join(os.path.dirname(__file__), "config.ini")
    print(f"config_path: {config_path}")
    config = configparser.ConfigParser()
    config.read(config_path)

    # サンプル画像のパスをConfigから取得
    
    sample_image_path = config.get("Settings", "image_path")
    print(f"sample_image_path: {sample_image_path}")
    # OCRの実行
    extracted_text = ocr_from_image(sample_image_path)

    # 結果の出力
    print("抽出された文字列:")
    print(extracted_text)