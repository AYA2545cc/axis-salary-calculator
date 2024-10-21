# プロジェクトのセットアップ手順

このプロジェクトをセットアップするための手順は以下の通りです。

## 1. .env ファイルの作成

まず、プロジェクトのルートディレクトリにある .env.template をコピーして、.env という名前に変更します。

```bash
cp .env.template .env
```

## 2. 環境変数の設定

.env ファイルを開き、以下の変数に必要な値を入力してください。

```bash
ID="0000000"
PASSWORD="your_password"
HOURLY_RATE=
ROUND_TRIP_COST=
```

各変数にあなたの情報を入力してください。

## 3. 必要なパッケージのインストール

次に、プロジェクトで必要なPythonパッケージをインストールします。以下のコマンドを実行してください。

```bash
pip install -r requirements.txt
```

## 4. プログラムの実行

すべての準備が整ったら、以下のコマンドでプログラムを実行します。

```bash
python main.py
```
