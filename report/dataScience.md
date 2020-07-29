# 数据科学大作业

## 一、小组信息：


### 1.小组人数： 3人
### 2.成员信息
	181250051_黄孟斌_181250051@smail.nju.edu.cn  Python完成题数185 数据格式转换、数据模糊匹配、if_else结构分析
	181250029_段晓文_181250029@smail.nju.edu.cn  Python完成题数177  gui界面
	181250179_袁易锋_181250179@smail.nju.edu.cn  Python完成题数200 数据下载、if_else结构分析


## 二、研究问题：“面向用例”检测

### 1.研究背景
在本次的200道Python练习题中，因为结果显示中可以看到正确的答案，所以就可以通过简单的方法来获取一对对的用例和相应的结果，在这样的情况下就可以通过判断来确定一个输入对应的是什么答案。这就是“面向用例”编程。我们组本次的研究问题就是通过一定的方法来检测出这些“面向用例”的代码

### 2.应用场景
分析同学们的代码，查看出同学们有没有用“面向用例”的方法作弊

## 三、代码说明

### 1.代码开源地址

https://github.com/huangmengbin/UserCase-Oriented-Detection

### 2.代码目录说明

1. foo：转换test_data.json文件的储存格式。让最终下载的文件的格式是：按照题目下载，每个题目下是每个人做的代码文件。

2. gui：用来展示的gui

3. Resources：下载的代码、转化下载的代码的文件格式储存。下载代码的json文件。
4. String_match：提取下载的数据来与用例匹配

5. Structural_analysis：主要是分析代码中的if_else（因为“面向用例”大多都会用到大量的if_else）
6. Time_analysis：分析时间，限制时间的修饰器


## 四、研究方法

### 1.数据获取
1. 给出的test_data.json的格式是user然后其中包含这个user的所有题目。我们做的更改是把格式改为：题目，然后每个题目中包含了所有做这个题的同学的代码。
2. 根据更改后的humSB.json文件来下载文件
3. 对于下载的文件，把多余的信息去掉，只留下每个同学的答题代码。当然不是用Python写的代码就被我们删掉了

### 2.数据匹配

数据提取：

根据解析出来的ast树，提取出有效常量信息作为该代码的关键词，放入一个message列表。

对于较长的output，拆成列表，为了提高算法效率，可以适当牺牲精确度。提取前面部分有效成分作为其关键词列表，一般是67个左右，总字符数不超过300。

对于较长的input，拆成列表，分别提取头、尾部分有效成分，分别进行分析，类似output。


匹配：

对message列表，也是为了效率，选择其所有长度不超过用例列表2倍、总字符长度不超用例列表总字符数2倍的子序列，分别聚合成字符串，再与用例列表串进行比较。比较算法是Jaro-Winkler distance，是由William E. Winkler在Jaro distance的基础上进一步改进的算法，用于求解两个字符串之间的相似性，并且对公共前缀的权重有所提高。
返回所有相似度的最大值，以及对应子列表的始末下标，为了以后给该段信息标红。若最大值有多个，则所有始末下标都要返回。


数据分析：

以上仅为单个用例的相似度，要得出最终结果，需要进一步处理。首先，定义检测的有效度，代表结果的可信性。若用例极其短，甚至仅包含“ok”“0”“True”，即使十分相似，完全匹配，也是不可信的。而长的用例，基本一旦匹配就是面向用例，不匹配一般就认定是面向用例了。有效度根据用例列表的列表长度、字符串总长度、字符串平均长度，字符串最大值综合计算得出，绝大部分是根据用例决定。它和相似度无必然联系，大概就是给予了一个‘弃权’的机会。

然后根据所有输入输出的相似度、有效度，计算出总相似度、有效度.一般来说，output匹配比input更优先一些。总相似度为各相似度根据对应有效度进行加权，从而算出的平均值。



### 3.if_else分析
首先把下载下来的文件中的代码取出来。通过ast.parse方法对代码进行分析
通过Python带的ast的方法对代码进行分析，找出所有的if节点，并存入一个allIf表中。
提取解析用例，把每个用例存储在testInput中，结果存储在testOut中
最后把依次把if中的body部分制为None，再通过complie和exec函数运行代码，用sys.stdout跟testOut比较正确情况。这样就可以得到一个0,1的矩阵，通过分析这个矩阵就可以基本判断该代码是不是“面向用例”的代码
当然，对if的次数也进行分析，如果if次数与用例的个数差不多的话，就是有“面向用例”的嫌疑的



### 4.时间分析
运用Package func_timeout中的func_set_timeout(time)的方法可以避免终止运行中的超时问题


### 5.gui展示
通过上述方法得到的数据，在gui中展示出来，可以让使用者很直观的看到一些“面向用例”的情况

### 6.使用的开源库

1. ast
2. json
3. Resources.cut_paste_rename
4. sys
5. func_timeout.exceptions
6. func_timeout
7. tkinter
8. Resources.cut_paste_rename
9. String_match.extract_data
10. matplotlib.pyplot
11. numpy
12. urllib.request
13. urllib.parse
14. os
15. zipfile
16. shutil
17. re
18. String_match.partial_ratio
19. String_match.format
20. typing
21. astunparse
22. Levenshtein
23. math

## 五、案例分析







## 六、想说的话

	上了一学期的网课，感受十分不好。希望期末考老师助教小哥哥小姐姐手下留情。
	也很遗憾没能和有趣可爱的陈老师见面。。。。。。。。。


## 附录


