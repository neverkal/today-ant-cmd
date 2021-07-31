from db.connection.base_maria_db import BaseMariaDb

class LottoCmdDb(BaseMariaDb):
    def delete_lotto_num(self, round_key: int) -> None:
        """
        :param round_key: 회차
        :return: None
        """
        query = "DELETE FROM lotto_round_num WHERE round_key={}".format(round_key)

        self.exec_query(sql=query, params=None, with_commit=True)

    def insert_lotto_num(self, round_key: int, num: int, round_date: str, bonus_tf: bool) -> None:
        """
        :param round_key: 회차
        :param num: 로또 번호
        :param round_date: 로또 당첨일
        :param bonus_tf: 보너스 번호
        :return: None
        """
        query = "INSERT INTO lotto_round_num (round_key, num, round_date, bonus_tf) VALUES (?, ?, ?, ?)"
        params = (round_key, num, round_date, bonus_tf)

        self.exec_query(sql=query, params=params, with_commit=True)
