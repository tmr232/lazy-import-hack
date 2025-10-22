# Lazy Import Hack

A terrible hack around `wrapt.lazy_import` to allow writing lazy imports as follows:

```python
from lazy import json
# Or
from lazy.json import dumps
```

## Known Issues

Does not work for subpackage imports:

```python
>>> from lazy.os.path import join

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 996, in _find_and_load_unlocked
KeyError: 'lazy.os'
```

I'm not sure why, and I put too much time into this hack already.


## Extra Reading

- [Lazy Imports Using Wrapt](https://grahamdumpleton.me/posts/2025/10/lazy-imports-using-wrapt/)
- [PEP 810 - Explicit Lazy Imports](https://peps.python.org/pep-0810/)