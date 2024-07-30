
# 開発ガイド

## 📗 概要

この文書は「text_file_splitter」の開発ガイドです。

## 📝 単体テスト

仮想環境を起動し、以下のコマンドを実行してください。

``` powershell
\text_file_splitter> pytest tests
```

## 💾 exe化

仮想環境を起動し、以下のコマンドを実行してください。

``` powershell
pyinstaller .\main.py --clean --onefile --name=text_file_splitter.exe
```
