from typing import List
from db.connection.base_maria_db import BaseMariaDb


class LottoRuleCmdDb(BaseMariaDb):
    def get_last_week_num(self) -> List:
        """
        :return: 지난주 당첨번호 목록
        """

        query = "select * from lotto_round_num where round_key = (" \
                "select max(cast(round_key as integer)) as max_count from lotto_round_num )" \
                "AND bonus_tf=false ORDER BY num asc"
        result_round_num = self.exec_query(sql=query, params=None)

        return result_round_num

    def get_analysis_num_list(self) -> List:
        """
        :return: 첫번째 룰베이스(?)
        """

        query = "SELECT a.* FROM" \
                "(SELECT num, COUNT(num) AS num_count FROM lotto_round_num " \
                "WHERE round_date >= SUBDATE(NOW(), INTERVAL 6 MONTH) AND round_date <= NOW() AND bonus_tf=FALSE AND " \
                "num NOT IN (SELECT num FROM lotto_round_num WHERE round_key=(SELECT MAX(round_key+0) " \
                "FROM lotto_round_num)) GROUP BY num ORDER BY num,num_count DESC) AS a " \
                "WHERE a.num_count >= 3 AND a.num_count <= 4 ORDER BY a.num+0 ASC"
        result_analysis_num_list = self.exec_query(sql=query, params=None)

        return result_analysis_num_list

