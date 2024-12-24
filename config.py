from dotenv import load_dotenv
import os

# .envファイルを読み込み
load_dotenv()

# 環境変数を取得
IMAGE_PATH = os.getenv("IMAGE_PATH", "./images")  # デフォルト値
DEBUG_PATH = os.getenv("DEBUG_PATH", "./debug")  # デフォルト値
CLIPPED_IMAGES_PATH = os.path.join(IMAGE_PATH, "clipped_images")  # Add this line
INPUT_IMAGE_PATH = os.getenv("INPUT_IMAGE_PATH", "./images/input/test1.png")  # デフォルト値
LOG_PATH = os.getenv("LOG_PATH", "./logs")        # デフォルト値

# 新しい設定を追加
POKEMON_NAMES_DIR = os.getenv("POKEMON_NAMES_DIR", "./data/pokemon_names")
ALLY_PATH =  os.path.join(CLIPPED_IMAGES_PATH, "ally.png")  # Add this line 
ENEMY_PATH = os.path.join(CLIPPED_IMAGES_PATH, "enemy.png") 
CLIP_CONFIG_PATH = os.getenv("CLIP_CONFIG_PATH", "./config/clip_config.json")
GRID_IMAGE_PATH = os.path.join(DEBUG_PATH, "grid_with_labels.png") 


# 他の設定が必要な場合ここに追加