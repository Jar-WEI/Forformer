**（创意编程）（下面是原文文档）**
# **Forformer** 
Forformer是一款强大的英语词形变化题库生成器，它不仅支持按单词出题，还支持语法出题，多词出题，一句多词等。

## 导入
在正式操作之前，您需要导入一些必要文件。
**语料库**是本程序出题的核心，所有语句和出的题目均会在语料库内索引。语料库可以是小说集，英语字典，英语教科书集。语料库的格式不做要求，Forformer会找出语料库内所有的句子，***请确保语料库的编码为UTF-8***。**单词列表**是本程序关键部分，它的格式如下:

```
    wordA1,wordA2,wordA3...
    wordB1,wordB2...
    .
    .
    .
```
其中单行为一类单词，不同词性的单词用英文逗号隔开。不同行为不同种类的单词，在出题时，Forformer会按需在单词列表部分选取。***同样的，导入单词列表的文件编码也必须是UTF-8。***

## 语法
语法索引是Forformer的一项重要功能，它的格式如下：
```
to #
be #
have #
to be #
.
.
.
```
其中，#代表要匹配的单词，单行只能放一种语法形式。如果您启用了语法索引，题目中括号内出题的单词即为#(原词组删去语法部分)。如果您想匹配任意单词，而不受单词列表的束缚，您可以启用 *在语法范围内匹配所有单词* 功能。    
## 索引方式
Forformer提供了两种索引方式，分别为 *快速索引* 和 *包含索引*
### 快速索引
快速索引将严格按照提供的单词列表进行索引，在单词列表之外的单词均不会匹配到。但有时候，一个词根可以有多个单词相配，单词列表列不下时，就要用到包含索引。
### 包含索引
与快速索引不同的是，包含索引会匹配所有包含单词列表内单词的单词。如：
在包含模式下您可以这样写：
```
    judge,judg
```
这样，Forformer会自动匹配 *judgment,judging,judgely* 等单词。并且出题时只会出在单词列表行里的第一个单词(也就是示例的judge)作为题目中括号内的单词。

## 导出题库
Forformer提供了两种导出形式，题目类型会将答案标在每题末尾，试卷类型将删去答案，并标上序号。
