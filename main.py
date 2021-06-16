from multiprocessing import Pool
from device import adb_devices, connect_single_device  # type: ignore
from appControl import invoke_fb, restart_fb, swipe_up  # type: ignore

def main_program(emulator):
    
    # 連接模擬器
    try:
        d = connect_single_device(emulator)
    except:
        print(emulator, '無法連接，將停止運作')
        return

    # 開啟FB
    try:
        invoke_fb(d)
    except:
        print(emulator, '無法開啟FB，將停止運作')
        return

    # 瀏覽動態牆
    for i in range(10):
        try:
            swipe_up(d)
        except:
            if not restart_fb(d):
                print(emulator, '無法重啟FB，將停止運作')
                return


if __name__ == '__main__':
    
    # 取得所有模擬器
    try:
        emulators = adb_devices()
        emulator_amount = len(emulators)  # 模擬器總數
    except:
        print('無法取得模擬器列表，將結束程式，請用adb devices檢查模擬器是否啟動')
        exit()

    # multi-processing
    pool = Pool(emulator_amount)
    for emulator_index in emulators.keys():
        pool.apply_async(func=main_program, args=(emulators[emulator_index],))  # args裡面的逗號不可少
    pool.close()
    pool.join()
    pool.terminate()