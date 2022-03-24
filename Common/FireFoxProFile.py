from selenium import webdriver

def FireFoxProFile():
    # 用来取消window系统弹出的下载管理器，直接跳过去下载
    profile = webdriver.FirefoxProfile()
    # 指定下载路径
    # profile.set_preference('browser.download.dir', 'E:\\firefox下载\\')
    # 0表示下载到桌面，1表示下载到默认路径，2表示使用自定义下载路径
    profile.set_preference("browser.download.folderList", 1)
    # 开始下载时是否显示下载管理器  true表示弹出   false表示不弹出
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    # 下载文件的类型 看下载接口的content-type类型
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                           "application/json,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return profile