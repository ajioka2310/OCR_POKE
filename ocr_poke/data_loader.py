"""
データの読み込み
"""

import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_pokemon_names(directory: str) -> pd.DataFrame:
    """
    指定されたディレクトリ内の全てのCSVファイルを読み込み、
    1つのDataFrameにまとめて返す関数。

    Parameters:
        directory (str): CSVファイルが格納されたディレクトリへのパス。

    Returns:
        pd.DataFrame: 結合されたデータフレーム。
    """
    all_dataframes = []

    # ディレクトリ内の全てのファイルを取得
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            file_path = os.path.join(directory, file)
            try:
                df = pd.read_csv(file_path)
                all_dataframes.append(df)
            except Exception as e:
                logger.error(f"Error reading {file}: {e}")

    # 全てのデータフレームを結合
    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        combined_df.columns = [
            "Number",
            "Japanese",
            "English",
            "German",
            "French",
            "Korean",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
        ]
        return combined_df
    else:
        logger.info("No valid CSV files found in the directory.")
        return pd.DataFrame()
