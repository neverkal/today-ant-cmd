from config import LOTTO_URL
from db.query.lotto_cmd_db import LottoCmdDb

import requests
import json
import time


class LottoCmd(object):

    def lotto_num_cmd(self, draw_len: int) -> None:
        """
        :param draw_len: 수집하려는 회차
        :return: None
        """

        for i in range(draw_len):
            lotto_get_param = {
                'method': 'getLottoNumber',
                'drwNo': i + 1
            }

            url = LOTTO_URL

            res = requests.get(url=url, params=lotto_get_param)
            res_decode = json.loads(res.content)

            cmd_db = LottoCmdDb()

            cmd_db.delete_lotto_num(round_key=i + 1)

            cmd_db.insert_lotto_num(i + 1, res_decode['drwtNo1'], res_decode['drwNoDate'], False)
            cmd_db.insert_lotto_num(i + 1, res_decode['drwtNo2'], res_decode['drwNoDate'], False)
            cmd_db.insert_lotto_num(i + 1, res_decode['drwtNo3'], res_decode['drwNoDate'], False)
            cmd_db.insert_lotto_num(i + 1, res_decode['drwtNo4'], res_decode['drwNoDate'], False)
            cmd_db.insert_lotto_num(i + 1, res_decode['drwtNo5'], res_decode['drwNoDate'], False)
            cmd_db.insert_lotto_num(i + 1, res_decode['drwtNo6'], res_decode['drwNoDate'], False)
            cmd_db.insert_lotto_num(i + 1, res_decode['bnusNo'], res_decode['drwNoDate'], True)

            time.sleep(1)

            print(res_decode)
            print("{}번째 회차 수집 완료".format(i + 1))


if __name__ == '__main__':
    lotto_cmd = LottoCmd()
    print(lotto_cmd.lotto_num_cmd(draw_len=3))
