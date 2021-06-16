# Android AutoTest

用Android Debug Tool (ADB) 搭配uiautomator2在雷電模擬器上做到App自動化測試。

此repo模擬自動瀏覽Facebook動態牆:
* 開啟多個模擬器。
* 在命令提示字元輸入`adb devices`直到所有模擬器的狀態都是`device`。
* `python main.py`開始執行。
* 自動開啟所有模擬器的Facebook (假設都已事先登入好帳號)。
* 所有模擬器自動開始滑動動態牆。