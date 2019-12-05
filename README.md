# YoriAnkiWordData
**此项目为个人使用，功能为生成Anki可用格式的英文单词数据**

数据来源为[有道](https://www.youdao.com/)，如侵权请联系删除



## GenerateImportData介绍：

生成Anki可导入的txt格式数据，顺序为

**单词** **音标** **释义** **例句**

使用前需要准备一个txt格式包含你需要的单词表单的文件，txt内容例：

```
aunt
brother cousin，couple
dad,daughter
family;father
grandchild
granddaughger
grandfather
```

单词间使用**换行符、逗号、空格、分号**进行分割

使用时直接拖拽准备好的单词表单txt到GenerateImportData程序上就会自动获取数据并生成一个utf-8编码的data.txt文件，
直接使用Anki导入后使用AwesomeTTS获取语音即可，Anki详细设置不在此处描述

## GenerateWords介绍：

从下载的词汇表中生成GenerateImportData程序需要的单词表单，
使用前需要从网上下载一份词汇表文档，项目中有份小升初词汇表word文件，把word文件中的文本全选复制粘贴到一个新建的txt
中，之后拖动此txt文件到GenerateWords上后会自动生成一个words.txt文件，再将此文件拖动到GenerateImportData上就能产生需要的导入文件。

所有示例都在项目中，如需使用请勿宣传T.T
