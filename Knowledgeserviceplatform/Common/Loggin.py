import logging.handlers
import time
#采用单例封装logger日志
class Log():
    logger=None
    @classmethod
    def getLoggin(cls):
        if cls.logger is None:
            # 获取 日志器
            cls.logger = logging.getLogger()
            # 设置 日志器 级别
            cls.logger.setLevel(logging.INFO)

            # 获取处理器 控制台
            sh = logging.StreamHandler()
            # 获取处理器 文件-以时间分隔
            #interval: 滚动周期，单位有when指定，比如：when=’D’,interval=1，表示每天产生一个日志文件
            #backupCount: 表示日志文件的保留个数
            times = time.strftime("%Y%m%d%H%M".format(time.localtime()))
            th = logging.handlers.TimedRotatingFileHandler("E:\\python-pycharm\\pythonProject\\Knowledgeserviceplatform\\Login\\" + times + ".log",
                                                              when="D", interval=1, backupCount=30, encoding="utf-8")

            # 设置格式器
            fm = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s")
            # 将格式器添加到 处理器 控制台
            sh.setFormatter(fm)
            # 将格式器添加到 处理器 文件
            th.setFormatter(fm)
            # 将处理器添加到 日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger

# if __name__=="__main__":
#     logger2=Log().getLoggin()
#     for i in range(100):
#         logger2.info("info被信息被执行")
#         logger2.error("error被信息执行")
#         time.sleep(1)