import logging.config
import os
import sys
from pathlib import Path

# 親ディレクトリをアプリケーションのホーム(${app_home})に設定
# app_home: str = str(Path(__file__).resolve().parent.parent)
app_home = str(Path(__file__).parents[1])
# ${app_home}をライブラリロードパスに追加
sys.path.append(app_home)


app_home = str(Path(__file__).parents[1])
# ロガーの設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "production": {
            "format": "%(asctime)s [%(levelname)8s] " "%(name)s: %(message)s"
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(app_home, "log", "app.log"),
            "formatter": "production",
            "when": "D",
            "interval": 1,
            "backupCount": 10,
            "delay": False,
        },
    },
    "loggers": {
        # 自分で追加したアプリケーション全般のログを拾うロガー
        "": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
logging.config.dictConfig(LOGGING)


class MyBatchConf(object):
    key1 = "key1_value"
    key2 = True
