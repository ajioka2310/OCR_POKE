"""
文字列の類似度を計算するモジュール
"""

from fuzzywuzzy import fuzz  # type: ignore


def find_closest_pokemon(ocr_output, df):
    """
    ノイズ除去を行う
    Args:
        ocr_output (str): 検出された文字列
        df (pd.DataFrame): ポケモン名のデータフレーム

    Returns:
        closest_name (str): 一番近いポケモン名（日本語）
        highest_similarity (float): 類似度
    """
    closest_name = None
    closest_lang = None
    highest_similarity = 0
    closest_name_ja = None
    # 各行を処理
    for _, row in df.iterrows():
        for lang in [
            i for i in df.columns if i not in ("Number")
        ]:  # すべての言語をチェック
            similarity = fuzz.ratio(ocr_output, row[lang])  # 類似度を計算
            if similarity > highest_similarity:
                highest_similarity = similarity
                closest_lang = lang
                closest_name = row[lang]
                closest_name_ja = row["Japanese"]  # 日本語名を取得
                

    return closest_lang, closest_name, highest_similarity, closest_name_ja
