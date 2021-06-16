import time
import uiautomator2 as u2

def swipe_up(d, t=0.3):
    width = d.info['displayWidth']
    height = d.info['displayHeight']

    x1 = width * 0.5     
    y1 = height * 0.8
    y2 = height * 0.2
    d.swipe(x1,y1,x1,y2,t)

def invoke_fb(d):
    if d(className="android.widget.TextView", text="Facebook").exists():
        d(className="android.widget.TextView", text="Facebook").click()
        time.sleep(10)
    else:
        print('找不到FB，無法啟動')
        raise Exception

def stopapp(d, package='com.facebook.katana'):
    try:
        d.app_stop(package)
        time.sleep(3)
    except:
        print('無法關閉FB')
        raise Exception

def home(d):
    try:
        d.press("home")
        time.sleep(3)
    except:
        print('無法回到模擬器主頁')
        raise Exception

def restart_fb(d):
    try:
        stopapp(d)
        home(d)
        invoke_fb(d)
        return True
    except:
        return False