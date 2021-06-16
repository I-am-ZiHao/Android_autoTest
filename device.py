import os
import uiautomator2 as u2

def adb_devices():  # 取得所有模擬器名稱與狀態
    cmd = 'adb devices'
    process = os.popen(cmd)
    result = process.read().split('\n')
    text = []
    for line in result:
        if 'List of devices' not in line and line != '' and line != ' ':  # 去掉標題跟空白字串
            text.append(line)
    devices = {}
    for i in range(len(text)):
        words = text[i].split('\t')  # 格式: emulator-5554\tdevice
        if 'device' in words[1]:  # 只存有啟動的模擬器
            devices[i] = words[0]  # 用模擬器index當key
    if len(devices) == 0:
        print('無啟動中的模擬器，請檢查')
        raise Exception
    return devices

def connect_single_device(emulator: str):
    try:
        d = u2.connect(emulator)
        return d
    except:
        print('無法連接模擬器')
        raise Exception

