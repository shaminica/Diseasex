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

    try:
        # ヒントが重みリストにあることを確認する
        # なければexceptに飛ぶ
        for x in hint_list:
            x in w_list


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

    except:
        return 'unsure'


if __name__ == '__main__':
    I = '2 4 6 8'
    S = '2 6'
    H = '2 8'

    verify_diff_partition(I, S, H)
