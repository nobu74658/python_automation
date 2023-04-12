from pytrends.request import TrendReq
import pandas as pd

# ライブラリを初期化
pytrends = TrendReq()

# 今日の人気検索ワードを取得する
trending_searches_today = pytrends.trending_searches(pn='japan')
pd = pd.DataFrame(trending_searches_today)

for i in range(len(pd)):
    print(pd[0][i])
