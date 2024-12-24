import os
from PIL import Image, ImageDraw, ImageFont
from config import DEBUG_PATH

def draw_grid_with_labels(image_path, grid_size=(5, 5)):
    """
    グリッドを描画し、各セルの4隅と右端、下端に座標ラベルを追加します。

    Args:
        image_path (str): 入力画像のパス
        grid_size (tuple): グリッドの分割数（列数, 行数）
        output_path (str): 出力画像のパス
    """
    # 画像を開く
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # 画像サイズを取得
    width, height = image.size
    cell_width = width // grid_size[0]
    cell_height = height // grid_size[1]

    # フォントの設定（フォントサイズを大きめに）
    try:
        font = ImageFont.truetype("arial.ttf", 20)  # Windows用フォント
    except:
        font = ImageFont.load_default()  # フォントが見つからない場合のデフォルト

    # グリッドを描画
    for x in range(0, width + 1, cell_width):
        draw.line([(x, 0), (x, height)], fill="red", width=2)
    for y in range(0, height + 1, cell_height):
        draw.line([(0, y), (width, y)], fill="red", width=2)

    # 座標ラベルを描画（4隅に配置）
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            # セルの左上座標
            top_left_x = col * cell_width
            top_left_y = row * cell_height

            # 各隅の座標ラベルテキスト
            corners = {
                "top_left": (top_left_x, top_left_y),
                "top_right": (top_left_x + cell_width, top_left_y),
                "bottom_left": (top_left_x, top_left_y + cell_height),
                "bottom_right": (top_left_x + cell_width, top_left_y + cell_height),
            }

            # 各隅にラベルを描画
            for corner, (label_x, label_y) in corners.items():
                label_text = f"({label_x}, {label_y})"
                bbox = font.getbbox(label_text)
                text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

                # テキストの描画位置（ラベルの背景ボックスを考慮）
                text_x = label_x
                text_y = label_y

                # 背景ボックスを描画（半透明の白）
                box_padding = 5
                box_coords = [
                    text_x - box_padding,
                    text_y - box_padding,
                    text_x + text_width + box_padding,
                    text_y + text_height + box_padding
                ]
                draw.rectangle(box_coords, fill=(255, 255, 255, 200))  # 半透明の白背景

                # ラベルの描画（黒い文字）
                draw.text((text_x, text_y), label_text, fill="black", font=font)

    # 右端のラベルを追加
    for y in range(0, height + 1, cell_height):
        label_x = width
        label_y = y
        label_text = f"({label_x}, {label_y})"
        bbox = font.getbbox(label_text)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        # 背景ボックス
        box_coords = [
            label_x - text_width - 10,
            label_y - 10,
            label_x + 10,
            label_y + text_height + 10,
        ]
        draw.rectangle(box_coords, fill=(255, 255, 255, 200))  # 半透明の白背景
        draw.text((label_x - text_width, label_y), label_text, fill="black", font=font)

    # 下端のラベルを追加
    for x in range(0, width + 1, cell_width):
        label_x = x
        label_y = height
        label_text = f"({label_x}, {label_y})"
        bbox = font.getbbox(label_text)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        # 背景ボックス
        box_coords = [
            label_x - 10,
            label_y - text_height - 10,
            label_x + text_width + 10,
            label_y + 10,
        ]
        draw.rectangle(box_coords, fill=(255, 255, 255, 200))  # 半透明の白背景
        draw.text((label_x, label_y - text_height), label_text, fill="black", font=font)

    # 画像を保存
    output_dir = os.path.dirname(DEBUG_PATH)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # 保存先ディレクトリがなければ作成する

    image.save(DEBUG_PATH)


if __name__ == "__main__":
  # 使用例
  draw_grid_with_labels("./images/tests/test1.png", grid_size=(20, 20))
