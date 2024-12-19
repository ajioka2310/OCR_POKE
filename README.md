# OCR_POKE

日本語の画像からテキストを抽出するOCRツールです。

## セットアップ手順

### 1. リポジトリのクローン

```bash
git clone https://github.com/ajioka2310/OCR_POKE.git
cd OCR_POKE
```

### 2. 必要なソフトウェアのインストール

- [Docker](https://www.docker.com/get-started)
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
- VS Code 拡張機能:
  - [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### 3. 開発環境のセットアップ

1. VS Code でリポジトリを開きます。

2. 左下の「><」アイコン（Remote - Containers）をクリックし、「Reopen in Container」を選択します。

3. DevContainer の初回セットアップが開始されます。必要な Docker イメージのビルドや依存関係のインストールが自動的に行われます。

### 4. `config.ini` の設定

プロジェクトのルートディレクトリに `config.ini` ファイルを作成し、以下の内容を記述してください：

```ini
[Settings]
image_path = /workspaces/OCR_POKE/images/tests/test1.png
```

### 5. 画像ファイルの配置

OCR を実行したい画像ファイルを `images/tests/` ディレクトリに配置してください。

### 6. OCR の実行

VS Code のターミナルで以下のコマンドを実行してください：

```bash
python src/run_ocr.py
```

---

これらの手順に従ってセットアップと実行を行ってください。問題が発生した場合はお知らせください。

