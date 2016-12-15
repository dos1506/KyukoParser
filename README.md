# KyukoParser
仙台高専休講掲示板をパースして辞書形式にするやつです。

# 使い方
## 休講情報を辞書形式で取得する場合
```Python
from kyuko import fetchKyukoInfo
data = fetchKyukoInfo()
```
## falconを使用してAPIサーバを立てる場合
main.pyをuwsgiで動かしてください
