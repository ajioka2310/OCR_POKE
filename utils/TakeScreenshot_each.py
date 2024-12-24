import time
from PIL import ImageGrab
from screeninfo import get_monitors
import os
import argparse

# 引数を解析
parser = argparse.ArgumentParser(description="スクリーンショットキャプチャツール")
parser.add_argument("--debug", action="store_true", help="デバッグモード（モニター情報を表示して終了）")
parser.add_argument("--single", action="store_true", help="領域選択用に一枚だけスクショをとる")
parser.add_argument("--monitor_num", type=int, default=0, help="使用するモニター番号（0から始まる）")

args = parser.parse_args()

# デバッグモードの場合
if args.debug:
    monitors = get_monitors()
    print("モニター情報:")
    for i, monitor in enumerate(monitors):
        print(f"モニター {i}: {monitor}")
    exit(0)

# 保存先ディレクトリ
save_dir = os.path.join(os.getcwd(), "../images/input")
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

print(f"スクリーンショットを {save_dir} に保存します。停止するにはCtrl+Cを押してください。")

# モニター選択
monitors = get_monitors()
if args.monitor_num < 0 or args.monitor_num >= len(monitors):
    print(f"無効なモニター番号が指定されました。利用可能な範囲は 0～{len(monitors) - 1} です。")
    exit(1)

monitor = monitors[args.monitor_num]
print(f"使用するモニター: {args.monitor_num} ({monitor})")

if args.single:
    # スクリーンショットをキャプチャ
    bbox = (monitor.x, monitor.y, monitor.x + monitor.width, monitor.y + monitor.height)
    screenshot = ImageGrab.grab(bbox=bbox)
    save_file_path = os.path.join(save_dir, "input.png")
    # 保存
    screenshot.save(save_file_path, "PNG")
    print(f"Saved: {save_file_path}")
    exit(0)

# キャプチャループ
try:
    while True:
        # ロックファイルを作成
        lock_file_path = os.path.join(save_dir, "input.lock")
        if os.path.exists(lock_file_path):
            with open(lock_file_path, "r") as lock_file:
                lock_info = lock_file.read()
            print(f"ロックが存在します: {lock_info}")
            time.sleep(0.1)
            continue

        # ロックを設定
        with open(lock_file_path, "w") as lock_file:
            lock_file.write(f"LOCKED by {os.getpid()} at {time.time()}")

        try:
            # 選択されたモニターの位置とサイズ
            bbox = (monitor.x, monitor.y, monitor.x + monitor.width, monitor.y + monitor.height)

            # スクリーンショットをキャプチャ
            screenshot = ImageGrab.grab(bbox=bbox)
            save_file_path = os.path.join(save_dir, "input.png")

            # 保存
            screenshot.save(save_file_path, "PNG")
            print(f"Saved: {save_file_path}")

        finally:
            # ロックファイルを削除
            try:
                if os.path.exists(lock_file_path):
                    os.remove(lock_file_path)
            except Exception as e:
                print(f"ロックファイル削除中にエラーが発生: {e}")

        # 0.5秒待機
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nスクリーンショットを終了します。")
