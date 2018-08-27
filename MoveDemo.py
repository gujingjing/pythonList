from urllib import request

import inline as inline
import matplotlib as matplotlib
from bs4 import BeautifulSoup
import re
import jieba  # 分词包
import pandas
import numpy  # numpy计算包

Moveurl = "https://movie.douban.com/cinema/nowplaying/shanghai/"


# 获取电影资源列表
def getNowPlayingList(url):
    resp = request.urlopen(url)

    # 获取网页html代码
    html_data = resp.read().decode('utf-8')

    # print(html_data)

    # 解析html代码，获取需要数据
    # 第一个参数 解析的内容,第二个参数，解析器
    soup = BeautifulSoup(html_data, 'html.parser')
    # find_all 读取html标签中的内容
    # 查找 div 标签， id为nowplaying
    nowplaying_movie = soup.find_all('div', id='nowplaying')
    # print(nowplaying_movie[0])

    # 查找，li 列表 ,class为 list-item的所有元素  取出找到的第一个元素
    nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
    # print(nowplaying_movie_list)

    nowplaying_list = []
    # 遍历电影列表信息，获取电影 id 和名称
    for item in nowplaying_movie_list:
        nowplaying_dict = {}
        nowplaying_dict['id'] = item['data-subject']
        # 查找list-i标签内的内容，找到img标签
        for tag_img_item in item.find_all('img'):
            nowplaying_dict['name'] = tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)

    return nowplaying_list


# 获取电影评论列表
def getMoveCommmentList(playingmovelist):
    print(len(playingmovelist))

    nowPlaying_comment_list = []

    for nowplaying_list in playingmovelist:
        # 解析电影的评论内容
        requrl = 'https://movie.douban.com/subject/' + nowplaying_list[
            'id'] + '/comments' + '?' + 'start=0' + '&limit=20'
        resp = request.urlopen(requrl)
        html_data = resp.read().decode('utf-8')
        soup = BeautifulSoup(html_data, 'html.parser')
        # 查找电影评论的标签id
        comment_div_lits = soup.find_all('div', class_='mod-bd')

        # print(comment_div_lits)

        # 遍历出里面所有评论一句评论的人名称

        for item in comment_div_lits:
            nowplaying_comment = {}
            avatar = item.find_all('div', class_='avatar')[0]
            # print(avatar)
            nowplaying_comment['avatar_name'] = avatar.find_all('a')[0]['title']

            comment_p = item.find_all('p')[0]
            comment_span = comment_p.find_all('span', class_='short')[0]

            if comment_span.string is not None:
                # print(comment_span)
                nowplaying_comment['comment'] = comment_span.string
                nowPlaying_comment_list.append(nowplaying_comment)

    return nowPlaying_comment_list


# 电影资源列表
nowPlayingList = getNowPlayingList(Moveurl)
print(nowPlayingList)

# 电影评论列表
moveComment = getMoveCommmentList(nowPlayingList)
print(moveComment)

# 电影评论组合起来
comments = ''
for comment in moveComment:
    comments = comments + comment['comment'].strip()

print(comments)

# 取出评论中的标点符号
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)

print(cleaned_comments)

# 分词统计
segment = jieba.lcut(cleaned_comments)
words_df = pandas.DataFrame({'segment': segment})

print(words_df)

# 使用 stopwords.txt 停用词剔除
stopwords = pandas.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                            encoding='utf-8')  # quoting=3全不引用
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
print(words_df)

# 词评率统计
words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)

print(words_stat)


# 使用词云展示
# import matplotlib.pyplot as plt
# %matplotlib inline
# import matplotlib
# matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
# from wordcloud import WordCloud#词云包
#
# wordcloud=WordCloud(font_path="SimHei.ttf",background_color="white",max_font_size=80) #指定字体类型、字体大小和字体颜色
# word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}
# word_frequence_list = []
# for key in word_frequence:
#     temp = (key,word_frequence[key])
#     word_frequence_list.append(temp)
#
# wordcloud=wordcloud.fit_words(word_frequence_list)
# plt.imshow(wordcloud)





