import logging
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


# ロガーの設定
LOG_FILE = os.path.join(LOG_PATH, "app.log")
os.makedirs(LOG_PATH, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,  # ログレベルをDEBUGに設定　INFO
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# 特定のライブラリのログレベルを設定
logging.getLogger('matplotlib').setLevel(logging.WARNING)
logging.getLogger('PIL').setLevel(logging.WARNING)
logging.getLogger('pytesseract').setLevel(logging.WARNING)
