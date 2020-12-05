# pylookfor
A lightweight module searching methods in the current python environment by keywords.

---
## method - pylookfor.lookfor
**pylookfor.lookfor**(key: str, num_print=0, modules=[])
Searching methods in the current python environment by keywords.
Print modules, methods and the first line of their documents if any of them contain the keywords.

**Parameters**
* **key: str**
The keywords.
* **num_print: int, optional**
            The number of the methods that printed.
            default: 0 means no limit.
* **modules: list, optional**
            Search methods in these modules.
            default: [] means search all the modules.

**Example**
Like 'lookfor' in Matlab, it can print modules, methods and the first line of their documents if any of them contain the keywords.
```python
import pylookfor as lf
lf.lookfor('sort')
```
Part of the output:
```
--------------------Modules----------------------
isort - Defines the public isort interface
isort._future - Defines the public isort interface
isort.deprecated - Defines the public isort interface
isort.stdlibs - Defines the public isort interface
sortedcollections - Python Sorted Collections
sortedcontainers - Sorted Containers -- Sorted List, Sorted Dict, Sorted Set
--------------------Methods----------------------
builtins.sorted - Return a new list containing all items from the iterable in ascending order.
cytoolz.sorted - Return a new list containing all items from the iterable in ascending order.
isort.check_file - Checks any imports within the provided file, returning `False` if any unsorted or
isort.check_stream - Checks any imports within the provided code stream, returning `False` if any unsorted or
isort.sort_code_string - Sorts any imports within the provided code string, returning a new string with them sorted.
isort.sort_file - Sorts and formats any groups of imports imports within the provided file or Path.
isort.sort_stream - Sorts any imports within the provided code stream, outputs to the provided output stream.
``` 
It can search methods in specify modules,
```python
import pylookfor as lf
lf.lookfor('sort',modules = ['scipy'])
``` 
The output:
```
--------------------Methods----------------------
scipy.argsort - scipy.argsort is deprecated and will be removed in SciPy 2.0.0, use numpy.argsort instead
scipy.lexsort - scipy.lexsort is deprecated and will be removed in SciPy 2.0.0, use numpy.lexsort instead
scipy.msort - scipy.msort is deprecated and will be removed in SciPy 2.0.0, use numpy.msort instead
scipy.searchsorted - scipy.searchsorted is deprecated and will be removed in SciPy 2.0.0, use numpy.searchsorted instead
scipy.sort - scipy.sort is deprecated and will be removed in SciPy 2.0.0, use numpy.sort instead
scipy.sort_complex - scipy.sort_complex is deprecated and will be removed in SciPy 2.0.0, use numpy.sort_complex instead
```
It can limit the number of method printed.
```python
import pylookfor as lf
lf.lookfor('sort',modules = ['scipy'],num_print = 5)
``` 
The output:
```
--------------------Methods----------------------
scipy.argsort - scipy.argsort is deprecated and will be removed in SciPy 2.0.0, use numpy.argsort instead
scipy.lexsort - scipy.lexsort is deprecated and will be removed in SciPy 2.0.0, use numpy.lexsort instead
scipy.msort - scipy.msort is deprecated and will be removed in SciPy 2.0.0, use numpy.msort instead
scipy.searchsorted - scipy.searchsorted is deprecated and will be removed in SciPy 2.0.0, use numpy.searchsorted instead
scipy.sort - scipy.sort is deprecated and will be removed in SciPy 2.0.0, use numpy.sort instead
```