import unittest


def verify_diff_partition(I, S, H):

    # 過度に長い解とヒントを拒絶
    if len(S) > len(I) or len(H) > len(I):
        return 'unsure'

    if S == 'no':
        return 'unsure'

    # 数値をリストに
    w_list = [int(x) for x in I.split()]
    # 解答
    (w_res_1, w_res_2) = [int(x) for x in S.split()]

    # ヒントをリストに
    hint_list = [int(x) for x in H.split()]

    # ヒントが重みリストにあることを確認する
    # なければexceptに飛ぶ
    for x in hint_list:

        if x in w_list:
            continue
        else:
            return 'unsure'

    # ヒント以外の重みリストを用意する
    res_list = []
    for x in w_list:
        if x in hint_list:
            continue
        else:
            res_list.append(x)

    # 以下の2つを確認する。
    # ヒントリストと、残りの重さリストの中に提案された解がが含まれているか
    # 重さの合計が一致しているか
    cond_1 = (w_res_1 in hint_list) & (w_res_2 in res_list)
    cond_2 = (w_res_1 in res_list) & (w_res_2 in hint_list)

    if (cond_1 | cond_2) & (sum(hint_list) == sum(res_list)):
        return 'correct'
    else:
        return 'unsure'


class TestVerify(unittest.TestCase):

    def test_positive(self):
        I = '2 4 6 8'
        S = '2 6'
        H = '2 8'
        self.assertEqual(verify_diff_partition(I, S, H), 'correct')

    def test_negative(self):
        I = '2 8 14 23'
        S = '2 5'
        H = '8 14'
        self.assertEqual(verify_diff_partition(I, S, H), 'unsure')

        S = '2 14'
        H = '8 23'
        self.assertEqual(verify_diff_partition(I, S, H), 'unsure')

    def test_wrong_answer(self):
        I = '2 4 6 8'
        S = '2 8'
        H = '2 6'
        self.assertEqual(verify_diff_partition(I, S, H), 'unsure')

        H = '2 4'
        self.assertEqual(verify_diff_partition(I, S, H), 'unsure')


if __name__ == '__main__':
    unittest.main()
