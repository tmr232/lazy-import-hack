# Lazy Import Hack

A terrible hack around `wrapt.lazy_import` to allow writing lazy imports as follows:

```python
from lazy import json
# Or
from lazy.json import dumps
```

## Try it out!

One-off

```shell
uv run --isolated --with https://github.com/tmr232/lazy-import-hack.git python
```

Or install it

```shell
uv add https://github.com/tmr232/lazy-import-hack.git
```

## Extra Reading

- [Lazy Imports Using Wrapt](https://grahamdumpleton.me/posts/2025/10/lazy-imports-using-wrapt/)
- [PEP 810 - Explicit Lazy Imports](https://peps.python.org/pep-0810/)
