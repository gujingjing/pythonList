### Python 爬虫实战

#### 升级版本

[mac升级python版本](https://pigjian.com/article/mac-rapid-upgrade-python)

[mac升级python版本](https://www.jianshu.com/p/87ea74b94811)

####补充
列出当前安装的包：

-	pip list
- 
列出可升级的包：

- pip list --outdate

升级一个包：

- pip install --upgrade requests  // mac,linux,unix 在命令前加 sudo -H

升级所有可升级的包：

- pip freeze --local | grep -v '^-e' | cut -d = -f 1  | xargs -n1 pip install -U

$ for i in `pip list -o --format legacy|awk '{print $1}'` ; do pip install --upgrade $i; done





1. requests 网络请求库
	- 安装 pip install requests
	- 升级 pip install --upgrade requests
	- [requests快速上手手册](http://cn.python-requests.org/zh_CN/latest/user/quickstart.html)


### PyCharm 编译器使用

1. [hellow world](https://blog.csdn.net/chenggong2dm/article/details/9366805)
2. 注意中文格式,开头指定
	- # coding:utf-8

### 正则表达式

[正则表达式](http://www.runoob.com/regexp/regexp-syntax.html)

### XPath

> 安装 pip install lxml

>XPath即为XML路径语言，它是一种用来确定XML（标准通用标记语言的子集）文档中某部分位置的语言。XPath基于XML的树状结构，提供在数据结构树中找寻节点的能力。起初 XPath 的提出的初衷是将其作为一个通用的、介于XPointer与XSLT间的语法模型。但是 XPath 很快的被开发者采用来当作小型查询语言。

#### XPath语法
XPath你只需要知道这些语法

[XPath语法](https://cuiqingcai.com/2621.html)

|表达式|	描述|
|---|---|
|nodename|	选取此节点的所有子节点。|
|/	|从根节点选取。|
|//|	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。|
|.	|选取当前节点。|
|..|	选取当前节点的父节点。|
|@	|选取属性。|



### BeautifulSoup

BeautifulSoup，Python Html 解析库，相当于 Java 的 jsoup。

- 安装 pip install beautifulsoup4 --user



### 词频统计 jieba
- 安装 pip install jieba













