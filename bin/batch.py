import logging
from urllib.parse import quote_plus

import click
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import setting

# ベースクラスの作成
base = declarative_base()


# モデルクラスの作成
class Test_python(base):
    __tablename__ = "TEST_PYTHON"

    no = Column(Integer, primary_key=True)
    comment = Column(String(20))


# コマンドライン引数のハンドリング. must_argは必須オプション、optional_argは任意オプション
@click.command()
@click.option("--must_arg", "-m", required=True)
@click.option("--optional_arg", "-o", default="DefaultValue")
def cmd(must_arg: str, optional_arg: str) -> None:

    # ロガー
    logger = logging.getLogger("main")

    # 処理開始

    try:
        # ログ出力
        logger.info("start")

        user = "pypeach"
        password = "Pypeach@1234"
        host = "192.168.232.10"
        db_name = "pypeach"
        password = quote_plus(password)

        # engineの設定
        engine = create_engine(
            f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}"
        )

        # セッションの作成
        with scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=engine)
        ) as db_session:

            # 対象レコードをすべてリストで取得
            list_a = (
                db_session.query(Test_python).order_by(Test_python.no).all()
            )
            for r in list_a:
                logger.info((r.no, r.comment))

        # コマンドライン引数の利用
        logger.error(f"must_arg = {must_arg}")
        logger.error(f"optional_arg = {optional_arg}")

    except Exception as e:
        # キャッチして例外をログに記録
        logger.exception(e)


if __name__ == "__main__":
    cmd()
