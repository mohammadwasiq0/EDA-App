# EDA App

**Compression on `pickle (.pkl)` file in python
```python
from compress_pickle import dump, load
obj = dict(key1=[None, 1, 2, "3"] * 10000, key2="Test key")
fname1 = "similarity.pkl"  # We can save to an uncompressed pickle file
dump(obj, fname1)
```
