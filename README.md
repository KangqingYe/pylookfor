# pylookfor
[中文](https://github.com/KangqingYe/pylookfor/tree/main/doc/README.md)|[English](https://github.com/KangqingYe/pylookfor/blob/main/README.md)

A lightweight module searching methods in the current python environment by keywords.

## Method - pylookfor.lookfor
**pylookfor.lookfor**(key: str, num_print=0, modules=[])

Searching methods in the current python environment by keywords.

Print modules, methods and the first line of their documents if any of them contain the keywords.

**Parameters**
* **key: str**

    The keywords.
* **num_print: int, optional**
  
    The number of the methods that printed.

    Default: 0 means no limit.
* **modules: list, optional**
  
    Search methods in these modules.

    Default: [] means search all the modules.

## Example
### Install
```python
pip install pylookfor
```
### Example1
Like 'lookfor' in Matlab, it can print modules, methods and the first line of their documents if any of them contain the keywords.
```python
import pylookfor as lf
lf.lookfor('sort',num_print=5)
```
Output:
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
### Example2
It can search methods in specify modules.
```python
import pylookfor as lf
lf.lookfor('sort',modules=['scipy‘,’numpy'],num_print=10)
``` 
Output:
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
## How does it work & Thanks
**Search modules**：

* *sys.builtin_module_names* - return the names of all modules that are compiled into this Python interpreter.

* *pkgutil.walk_packages* - return the names of modules user installed.

**Search Methods**：

Use the *dir()* to return a list of valid attributes of the object, and select methods in them.

**Search documetion**：

Call the *.\_\_doc\_\_* in each modules.

**Thanks**：

Thanks for the help of [Rossil](https://github.com/Rossil2012) and the inspiration of [Jay_Wu](https://github.com/Jay-9912) and [kf-Zhang](https://github.com/kf-zhang).
