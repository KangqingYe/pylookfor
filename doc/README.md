# pylookfor
[中文](https://github.com/KangqingYe/pylookfor/tree/main/doc/README.md)|[English](https://github.com/KangqingYe/pylookfor/blob/main/README.md)

在当前环境下依据关键词查找库函数的轻量python库。

## 函数 - pylookfor.lookfor
**pylookfor.lookfor**(key: str, num_print=0, modules=[])

在当前python环境下搜索关键词来查找库函数。

如果库名、库函数名或者它们文档的第一行中包含关键词就把它们显示出来。

**参数**
* **key: str**

    关键词。
* **num_print: int, 可选**
 
    显示的库函数数量。

    默认: 0 表示全部显示。
* **modules: list, 可选**

    在这些库里查找库函数。
    
    默认：[] 表示在所有库里查找。

## 示例
### 安装
```python
pip install pylookfor
```
### 示例1
和Matlab里的'lookfor'函数类似，如果库名、库函数名或者它们文档的第一行中包含关键词就把它们显示出来。
```python
import pylookfor as lf
lf.lookfor('sort',num_print=5)
```
输出:
```
--------------------Modules----------------------
isort - Defines the public isort interface
isort._future - No Documentation Found.
isort.deprecated - No Documentation Found.
isort.stdlibs - No Documentation Found.
networkx.algorithms.assortativity - No Documentation Found.
networkx.algorithms.assortativity.tests - No Documentation Found.
sortedcollections - Python Sorted Collections
sortedcontainers - Sorted Containers -- Sorted List, Sorted Dict, Sorted Set
--------------------Methods----------------------
builtins.sorted - Return a new list containing all items from the iterable in ascending order.
anaconda_navigator.utils.sort_versions - Sort a list of version number strings.
cytoolz.sorted - Return a new list containing all items from the iterable in ascending order.
isort.check_file - Checks any imports within the provided file, returning `False` if any unsorted or
isort.check_stream - Checks any imports within the provided code stream, returning `False` if any unsorted or
``` 
### 示例2
它可以在特定的库里查找方法。
```python
import pylookfor as lf
lf.lookfor('sort',modules=['scipy‘,’numpy'],num_print=10)
``` 
输出:
```
--------------------Methods----------------------
scipy.argsort - scipy.argsort is deprecated and will be removed in SciPy 2.0.0, use numpy.argsort instead
scipy.lexsort - scipy.lexsort is deprecated and will be removed in SciPy 2.0.0, use numpy.lexsort instead
scipy.msort - scipy.msort is deprecated and will be removed in SciPy 2.0.0, use numpy.msort instead
scipy.searchsorted - scipy.searchsorted is deprecated and will be removed in SciPy 2.0.0, use numpy.searchsorted instead
scipy.sort - scipy.sort is deprecated and will be removed in SciPy 2.0.0, use numpy.sort instead
scipy.sort_complex - scipy.sort_complex is deprecated and will be removed in SciPy 2.0.0, use numpy.sort_complex instead
numpy.argsort - Returns the indices that would sort an array.
numpy.lexsort - lexsort(keys, axis=-1)
numpy.msort - Return a copy of an array sorted along the first axis.
numpy.searchsorted - Find indices where elements should be inserted to maintain order.
```
## 原理和感谢
**查找库**：

*sys.builtin_module_names* —— 返回内建模块的名称。

*pkgutil.walk_packages* —— 返回所有用户安装的模块的名称。

**查找库函数**：

用*dir()* 返回所有库函数及其属性，再判断其是否为可用库函数。

**查找库文档**：

调用每个模块的 *.\_\_doc\_\_* 函数。

**感谢**：

感谢[Rossil](https://github.com/Rossil2012)的帮助，[Jay_Wu](https://github.com/Jay-9912)和[kf-Zhang](https://github.com/kf-zhang)的启发。

