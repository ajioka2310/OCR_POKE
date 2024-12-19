import configparser
import os
from ocr_poke.ocr import ocr_from_image
from ocr_poke.data_loader import load_pokemon_names

if __name__ == "__main__":
    # Configファイルを読み込む
    config_path = os.path.join(os.path.dirname(__file__), "config.ini")
    config = configparser.ConfigParser()
    config.read(config_path)

    # サンプル画像のパスをConfigから取得
    sample_image_path = config.get("Settings", "image_path")
    # OCRの実行（デバッグモード有効）
    extracted_text = ocr_from_image(sample_image_path, debug=True)

    # 結果の出力
    print("抽出された文字列:")
    print(extracted_text.split())

    # ポケモン名データのロード
    pokemon_names_dir = config.get("Settings", "pokemon_names_dir")
    pokemon_names_df = load_pokemon_names(pokemon_names_dir)

    # デバッグ用にデータの確認
    print(pokemon_names_df.head())
