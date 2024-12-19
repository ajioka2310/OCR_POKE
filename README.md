# Python Docker OCR プロジェクト

このプロジェクトは、Dockerを利用してOCR機能を開発するPythonアプリケーションです。開発環境はVSCodeのRemote - Containers拡張機能を利用してコンテナ内でセットアップされます。

---

## 必要なツール

- **Docker Desktop**: [公式サイト](https://www.docker.com/products/docker-desktop)からインストールしてください。
- **Visual Studio Code (VSCode)**: [公式サイト](https://code.visualstudio.com/)からインストールしてください。
- **Remote - Containers 拡張機能**: VSCode内で拡張機能をインストールします。

---

## 環境セットアップと実行手順

1. **リポジトリをクローン**
   プロジェクトをローカル環境にクローンします：
   ```bash
   git clone https://github.com/USERNAME/python-docker-ocr.git
   cd python-docker-ocr
   ```

2. **VSCodeでプロジェクトを開く**
   プロジェクトディレクトリ内で以下を実行し、VSCodeを起動します：
   ```bash
   code .
   ```

3. **コンテナ内で開発環境をセットアップ**
   - 左下の緑色のアイコンをクリックし、「Reopen in Container」を選択します。
   - 初回はコンテナがビルドされ、必要な依存関係がインストールされます（`requirements.txt` に基づきインストールされます）。

4. **スクリプトの実行**
   - ターミナルを開き、コンテナ内で以下のコマンドを実行します：
     ```bash
     python main.py
     ```

---

## 開発環境の特徴

- **Dockerを利用**:
  開発環境がコンテナ内で統一されており、ホスト環境に依存しません。

- **VSCode連携**:
  Remote - Containers拡張機能により、コンテナ内のコード編集やデバッグが簡単に行えます。

- **Git統合**:
  コンテナ内でGitを利用できます。VSCodeのGit GUIもサポートされています。

---

## 注意事項

- **コンテナがビルドされない場合**:
  Docker Desktopが正常に動作していることを確認してください。

- **日本語OCRの認識**:
  Tesseractの日本語データ（`jpn.traineddata`）は、Dockerfileでインストールされています。

---

これでプロジェクトの開発環境がセットアップされ、すぐに開発を開始できます！

