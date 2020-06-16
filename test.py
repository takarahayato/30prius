# coding:utf-8
def calculation(combination_list, x) :
    goods = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}# 品物
    weight = [3,6,5,4,8,5,3,4,3,5,6,4,8,7,11,8,14,6,12,4]# 重量
    price = [7,12,9,7,13,8,4,5,3,10,7,5,6,14,5,9,6,12,5,9]# 価格
    better_weight =0 # 重量制限下で価値が一番高い時のナップザックの重量
    limit_weight = 55 # 重量制限
    max_price = 0  #combination_list内の一番良い値段
    knapsack_weight = 0 # ナップザックの重量
    knapsack_price = 0 # ナップザックの中にある品物の価値
    best_combination = [] # 一番良い組み合わせ
    count = 0            # リストの一つ一つを区切るためのcount変数
   
#test
    for goods in combination_list :
        if len(goods) < 12:#一番軽いの同士の組み合わせでも11個が限界なので12個以上は計算するまでもなく重量オーバー
            for number in goods :
                knapsack_weight += weight[number-1]# ナンバーが示す番号の価格と重量を加算する
                knapsack_price += price[number -1]
                count += 1
            

                if count == x :
                    if max_price < knapsack_price: # ナンバー加算が全て終わったら一番高い値段と比べる
                        if knapsack_weight <= limit_weight:
                            max_price = knapsack_price
                            best_combination = goods
                            better_weight = knapsack_weight

                if count == x : #一つのリストをループし終わったら初期化する
                    knapsack_weight = 0
                    knapsack_price = 0
                    count =0
    return [max_price, best_combination,better_weight]
