import argparse
import os
import sys


# mainの関数
def main_func():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="テキストファイルを分割します。")
    parser.add_argument("input_file", help="分割するテキストファイルのパス。")

    # コマンドライン引数の取得
    args = parser.parse_args()
    input_file = args.input_file

# テキストファイルを指定された行数で分割します。
def split_text_file(input_file_path, lines_per_file=10000):
# 入力ファイルの確認
    if not os.path.exists(input_file_path):
        print("ファイルを指定してください。", file=sys.stderr)
        sys.exit(1)

    # 入力ファイルの情報を取得
    input_dir = os.path.dirname(input_file_path)
    input_file_name = os.path.splitext(os.path.basename(input_file_path))[0]
    input_file_extension = os.path.splitext(input_file_path)[1]

    # 出力ディレクトリの作成
    output_dir = os.path.join(input_dir, input_file_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # ファイルの読み込みと分割
    with open(input_file_path, 'r', encoding='utf-8') as reader:
        file_number = 1
        lines_written = 0

        # 新しいファイルを作成
        output_file_path = os.path.join(output_dir, f"output_{file_number}{input_file_extension}")
        writer = open(output_file_path, 'w', encoding='utf-8')

        try:
            for line in reader:
                if lines_written == lines_per_file:
                    writer.close()  # 現在のファイルを閉じる
                    file_number += 1
                    lines_written = 0
                    output_file_path = os.path.join(output_dir, f"output_{file_number}{input_file_extension}")
                    writer = open(output_file_path, 'w', encoding='utf-8')
                
                writer.write(line)
                lines_written += 1
        finally:
            writer.close()

    print("処理が完了しました。")

# mainの関数呼び出し
if __name__ == "__main__":
    main_func()
