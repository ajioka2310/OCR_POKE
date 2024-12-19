import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display



# 任意のURLを指定
url = "https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7"

# ウェブページを取得
response = requests.get(url)
response.encoding = response.apparent_encoding  # 文字コードを自動判定
soup = BeautifulSoup(response.text, 'html.parser')

# すべてのテーブルを取得
tables = soup.find_all('table')

for gen,table in enumerate(tables):
    # テーブルを行ごとに解析
    rows = []
    for row in table.find_all('tr'):
        cells = row.find_all(['th', 'td'])  # <th>と<td>を取得
        rows.append([cell.get_text(strip=True) for cell in cells])  # テキストを抽出

    # DataFrameに変換
    df = pd.DataFrame(rows)
    # Display DataFrame
    display(df)
    # CSVファイルとして保存
    df.to_csv(f'./data/pokemon_names/pokemon_names_gen_{gen+1}.csv', index=False, header=False, encoding='utf-8-sig')