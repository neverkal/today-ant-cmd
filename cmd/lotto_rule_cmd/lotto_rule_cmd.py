import random

from typing import List
from db.query.lotto_rule_cmd_db import LottoRuleCmdDb


class LottoRuleCmd(object):
    def last_week_analysis_num(self) -> List:
        """
        :return: 지난주 로또 번호를 분석하여 나오는 이번주 로또 번호 6개
        """

        lotto_rule_cmd_db = LottoRuleCmdDb()

        last_week_lotto_list = lotto_rule_cmd_db.get_last_week_num()
        analysis_num_list = lotto_rule_cmd_db.get_analysis_num_list()

        lotto_num_list = []

        for i, last_week_lotto in enumerate(last_week_lotto_list):
            lotto_num_list.append([int(last_week_lotto["num"])])

            lotto_set_no_duplicate = []

            while len(lotto_set_no_duplicate) < 5:
                lotto_set_num = int(analysis_num_list[random.randrange(len(analysis_num_list))]['num'])
                if lotto_set_num not in lotto_set_no_duplicate:
                    lotto_set_no_duplicate.append(lotto_set_num)

            lotto_num_list[i].extend(lotto_set_no_duplicate)
            lotto_num_list[i].sort()

        return lotto_num_list


if __name__ == '__main__':
    lotto_cmd = LottoRuleCmd()
    print(lotto_cmd.last_week_analysis_num())
