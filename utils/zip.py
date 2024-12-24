import os
import zipfile

def zip_ocr_poke():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # utilsディレクトリのパス
    target_dir = os.path.join(base_dir, '..')  # OCR_POKE直下
    zip_path = os.path.join(target_dir, 'OCR_POKE.zip')  # 出力先ファイル
    
    # 除外対象のリスト
    exclude_paths = [
        zip_path,  # OCR_POKE.zip
        os.path.join(target_dir, '.mypy_cache'),  # .mypy_cache
        os.path.join(target_dir, '.git')  # .mypy_cache
        
    ]

    # OCR_POKE.zipが存在する場合は削除
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"既存のZIPファイルを削除しました: {zip_path}")
    
    # ZIPファイルを作成
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(target_dir):
            # 除外ディレクトリのフィルタリング
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_paths]
            for file in files:
                file_path = os.path.join(root, file)
                # 除外ファイルのスキップ
                if file_path in exclude_paths:
                    continue
                # ZIPファイル内のパスを計算（相対パス）
                arcname = os.path.relpath(file_path, target_dir)
                zipf.write(file_path, arcname)
                print(f"追加: {arcname}")
    
    print(f"OCR_POKEディレクトリをZIP化しました: {zip_path}")

if __name__ == "__main__":
    zip_ocr_poke()
