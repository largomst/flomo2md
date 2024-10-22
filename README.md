# flomo exporter

# Design

具体的需求:

输入输出:

1. 输入: 一个HTML文件(包含多条笔记)
2. 输出: 多个Markdown文件,每条笔记生成一个文件
3. 输出目录: 用户指定的单个目录

文件命名与时间:
1. 文件名格式: yyyy-MM-dd hh.mm.ss.md
2. 需要设置文件的系统创建时间为笔记的创建时间

内容转换规则:
HTML到Markdown的标签映射:
<strong> → **文本**
<u> → _文本_
<mark> → ==文本==
<ul><li> → -
<ol><li> → 1.

图片链接保持原有的相对路径不变
以#开头的标签保持原样,不转换为Markdown标题
不处理标签的嵌套情况
不需要处理特殊转义字符
不处理表格和代码块

处理流程应该是:

1. 解析HTML文件,提取出所有class为"memo"的div
2. 对每个memo:
    1. 获取time内的创建时间
    2. 转换content中的HTML标签为Markdown格式
    3. 保持files中的图片链接不变
3. 为每个处理后的笔记生成对应的Markdown文件
4. 设置文件的系统时间

## Installation

## Usage
