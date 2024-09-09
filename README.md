# CustomWebdriver

CustomWebdriverは、Seleniumとundetected_chromedriverを使用したウェブ自動化のためのカスタムクラスです。異なる設定プロファイルを使用して、ボット対策、高速処理、プライバシーとセキュリティに焦点を当てた設定など、様々なシナリオに対応できます。

## 特徴

- 複数の設定プロファイル（ボット対策、高速処理、プライバシー重視）
- 安全な要素検索と操作
- ポップアップウィンドウの処理
- 柔軟な設定オプション

## インストール

必要な依存関係をインストールします：

```
pip install selenium undetected-chromedriver
```

## 使用方法

### 基本的な使用

```python
from CustomWebdriver import CustomWebdriver
from selenium.webdriver.common.by import By

# CustomWebdriverのインスタンスを作成
custom_driver = CustomWebdriver(config_name='config_1')

# ドライバーを作成
driver = custom_driver.create_driver()

# ウェブサイトにアクセス
driver.get("https://example.com")

# 要素を安全に見つけて操作
email_input = custom_driver.find_element_safely(By.ID, "email")
if email_input:
    email_input.send_keys("example@email.com")

# ブラウザを閉じる
custom_driver.quit()
```

### 設定プロファイルの選択

CustomWebdriverは複数の設定プロファイルをサポートしています：

- `config_1`: ボット対策設定
- `config_2`: 高速処理設定
- `config_3`: プライバシーとセキュリティ重視の設定

設定を選択するには、インスタンス作成時に`config_name`パラメータを使用します：

```python
custom_driver = CustomWebdriver(config_name='config_2')  # 高速処理設定を使用
```

### カスタム設定の適用

追加の設定オプションを適用するには、キーワード引数を使用します：

```python
custom_driver = CustomWebdriver(config_name='config_1', headless=True, window_size="1920,1080")
```

## 主要なメソッド

- `create_driver()`: WebDriverインスタンスを作成します。
- `find_element_safely(by, value, timeout=10)`: 要素を安全に見つけます。
- `wait_and_click(by, value, timeout=10)`: 要素が
クリック可能になるまで待ち、クリックします。
- `switch_to_popup(timeout=10)`: 新しいポップアップウィンドウに切り替えます。
- `switch_to_main_window()`: メインウィンドウに戻ります。
- `close_current_window()`: 現在のウィンドウを閉じます。
- `quit()`: ブラウザを閉じ、全てのリソースを解放します。

## 設定ファイル

各設定プロファイルは別々のPythonファイルで定義されています：

- `config_1.py`: ボット対策設定
- `config_2.py`: 高速処理設定
- `config_3.py`: プライバシーとセキュリティ重視の設定

これらのファイルには`WEBDRIVER_CONFIG_X`辞書と`apply_config`関数が含まれており、特定のユースケースに合わせてカスタマイズできます。

## 注意事項

- プロキシ設定を使用する場合は、環境に応じて適切に設定してください。
- ヘッドレスモードを使用する場合、一部のウェブサイトで検出される可能性があります。
- ウェブサイトの利用規約を確認し、自動化ツールの使用が許可されているか確認してください。

## トラブルシューティング

問題が発生した場合は、以下を確認してください：

- Chromeブラウザとchromedriver
のバージョンが一致していること。
- 必要な依存関係が全てインストールされていること。
- ネットワーク接続が安定していること。
- プロキシ設定を使用している場合、プロキシサーバーが利用可能であること。

## カスタマイズ

新しい設定プロファイルを追加するには、新しい設定ファイル（例：`config_4.py`）を作成し、`WEBDRIVER_CONFIG_4`辞書と`apply_config`関数を定義します。その後、`CustomWebdriver`クラスで新しい設定を使用できます。
