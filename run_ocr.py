"""
実行用.py
"""

import configparser
import os
import json
from ocr_poke.ocr import ocr_from_image
from ocr_poke.data_loader import load_pokemon_names
from ocr_poke.preprocessing import remove_noise_str, clip_image
from ocr_poke.similarity import find_closest_pokemon
import config  # config.pyをインポート

def extract_pokemon_names(image_path, pokemon_names_df):
    """
    画像からポケモン名を抽出する関数

    Args:
        image_path (str): 画像のパス
        pokemon_names_df (DataFrame): ポケモン名のデータフレーム

    Returns:
        tuple: 最も類似度の高いポケモン名とその類似度
    """
    extracted_text = ocr_from_image(image_path, debug=True)
    ls_extracted_text = extracted_text.split()
    ls_extracted_text = [remove_noise_str(i) for i in ls_extracted_text]
    ls_extracted_text = [i for i in ls_extracted_text if len(i) >= 2]
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
    return final_name, max_similarity

if __name__ == "__main__":
    # Configファイルを読み込む
    # config.pyから設定を取得
    pokemon_names_dir = config.POKEMON_NAMES_DIR
    pokemon_names_df = load_pokemon_names(pokemon_names_dir)
    print("各文字列に一番近いポケモンを見つける:")
    print("**********************************************")
        
    # 元画像をクリップ
    clip_config_path = config.CLIP_CONFIG_PATH
    with open(clip_config_path, "r") as f:
        clip_config = json.load(f)
    print(clip_config)
    for image_name, coordinates in clip_config.items():
        clip_image(coordinates, image_name)
        print("clip_image")
    # 味方のポケモン名を抽出
    ally_path = config.ALLY_PATH
    # print("aaaa")
    print(ally_path)
    final_name, max_similarity = extract_pokemon_names(ally_path, pokemon_names_df)
    print("**********************************************")
    print("最終的な判断")
    print(final_name, max_similarity)
    
    # 敵のポケモン名を抽出
    enemy_path = config.ENEMY_PATH
    final_name, max_similarity = extract_pokemon_names(enemy_path, pokemon_names_df)
    print("**********************************************")
    print("最終的な判断")
    print(final_name, max_similarity)
