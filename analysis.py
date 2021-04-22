import os
from collections import defaultdict

import pandas as pd
from textblob import TextBlob

data_path = './dataset/MINDsmall/'


def process_behaviors(behaviors_path, save_path):
    if os.path.exists(save_path):
        print("You have processed before!")
        return

    behaviors_df = pd.read_csv(behaviors_path, sep='\t', header=None,
                               names=['Impression ID', 'User ID', 'Time', 'History', 'Impressions'])
    behaviors_df = behaviors_df[['User ID', 'History', 'Impressions']]

    df = pd.DataFrame(columns=['User ID', 'History', 'Impressions'])
    user_set = set()
    for index, item in behaviors_df.iterrows():
        # 去掉没有'History'字段的行（冷启动用户）
        if type(item['History']) != str:
            continue

        # 合并User ID相同的行
        if item['User ID'] not in user_set:
            df = df.append(item, ignore_index=True)
            user_set.update([item['User ID']])
        else:
            df.loc[df['User ID'] == item['User ID'], 'Impressions'] += ' ' + item['Impressions']

    df.to_csv(save_path, sep='\t', index=False)


def process_news(processed_behaviors_path, news_path, save_path):
    if os.path.exists(save_path):
        print("You have processed before!")
        return

    behaviors_df = pd.read_csv(processed_behaviors_path, sep='\t', names=['User ID', 'History', 'Impressions'])
    news_df = pd.read_csv(news_path, sep='\t', header=None,
                          names=['News ID', 'Category', 'SubCategory', 'Title', 'Abstract', 'URL', 'Title Entities',
                                 'Abstract Entites'])

    # 统计新闻在behaviors的Impressions中被点击的次数
    count_click_imp = defaultdict(int)
    for index, row in behaviors_df.iterrows():
        item_list = row['Impressions'].split(' ')
        for item in item_list:
            if item[-1] == '0':
                continue
            news_id = item[:-2]
            count_click_imp[news_id] += 1

    # 统计新闻在behaviors的Impressions中被点击的次数
    count_click_his = defaultdict(int)
    for index, row in behaviors_df.iterrows():
        item_list = row['History'].split(' ')
        for item in item_list:
            count_click_his[item] += 1

    # 保存统计数据
    news_df = news_df[['News ID', 'Category', 'SubCategory', 'Title']]
    column_name = news_df.columns.tolist()
    column_name.insert(3, "title_sentiment_polarity")  # 情感极性
    column_name.insert(4, "imp_click_count")  # Impressions中点击次数
    column_name.insert(5, "his_click_count")  # History中点击次数
    news_df = news_df.reindex(columns=column_name)
    for index, row in news_df.iterrows():
        # 添加标题的情感极性
        title_text = row["Title"]
        blob = TextBlob(title_text)
        news_df.loc[index, "title_sentiment_polarity"] = blob.sentiment.polarity
        # 添加点击次数
        news_id = row['News ID']
        news_df.loc[index, "imp_click_count"] = int(count_click_imp[news_id])
        news_df.loc[index, "his_click_count"] = int(count_click_his[news_id])

    news_df.to_csv(save_path, sep='\t', index=False)


if __name__ == '__main__':
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    behaviors_path = data_path + 'MINDsmall_train/behaviors.tsv'
    news_path = data_path + 'MINDsmall_train/news.tsv'
    processed_behaviors_path = data_path + 'MINDsmall_train/behaviors_processed.tsv'
    processed_news_path = data_path + 'MINDsmall_train/news_processed.tsv'
    process_behaviors(behaviors_path, save_path=processed_behaviors_path)
    process_news(processed_behaviors_path, news_path, save_path=processed_news_path)
