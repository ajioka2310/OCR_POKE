import cv2

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
