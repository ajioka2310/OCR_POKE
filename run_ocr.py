"""
実行用.py
"""

import configparser
import os
from ocr_poke.ocr import ocr_from_image
from ocr_poke.data_loader import load_pokemon_names
from ocr_poke.preprocessing import remove_noise_str
from ocr_poke.similarity import find_closest_pokemon


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
    print(extracted_text)
    print("\n")

    ls_extracted_text = extracted_text.split()
    print("文字列を分解:")
    print(ls_extracted_text)
    print("\n")

    # ノイズの除去
    ls_extracted_text = [remove_noise_str(i) for i in ls_extracted_text]
    ls_extracted_text = [i for i in ls_extracted_text if len(i) >= 2]
    print("ノイズ除去:")
    print(ls_extracted_text)
    print("\n")
    # ポケモン名データのロード
    pokemon_names_dir = config.get("Settings", "pokemon_names_dir")
    pokemon_names_df = load_pokemon_names(pokemon_names_dir)
    print("各文字列に一番近いポケモンを見つける:")
    print("**********************************************")

    max_similarity = 0
    final_name = None
    for i, (closest_lang, closest_name, similarity, name) in enumerate(
        [find_closest_pokemon(i, pokemon_names_df) for i in ls_extracted_text]
    ):
        if similarity > max_similarity:
            final_name = name
            max_similarity = similarity
        print("各文字列への候補と類似度")
        print(f"{ls_extracted_text[i]} -> {name}")
        print(f"諸元：{closest_name}({closest_lang}) 類似度：{similarity}")
        print("\n")
    print("**********************************************")
    print("最終的な判断")
    print(final_name, max_similarity)
