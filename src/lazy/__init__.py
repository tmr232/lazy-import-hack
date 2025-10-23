import wrapt
import sys

from importlib.abc import Loader, MetaPathFinder
import importlib.util


class ModuleAttributeProxy:
    def __init__(self, base: str):
        self.base = base

    def __getattr__(self, item):
        module = sys.modules.get(self.base)
        if isinstance(module, ModuleAttributeProxy):
            del sys.modules[self.base]
        return lazy_import(self.base, item)


class LazyLoader(Loader):
    def create_module(self, spec):
        return ModuleAttributeProxy(spec.name)

    def exec_module(self, module):
        pass


class MetaFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=...):
        lazy, _, requested = fullname.partition(".")
        if lazy == __name__:
            return importlib.util.spec_from_loader(requested, LazyLoader())


sys.meta_path.insert(0, MetaFinder())

class MyLazyObjectProxy(wrapt.LazyObjectProxy):
    def __call__(self, *args, **kwargs):
        return self.__wrapped_get__()(*args, **kwargs)

def lazy_import(name, attribute=None):
    # Based on wrapt.lazy_import, but adds support for callables.
    def _import():
        module = __import__(name, fromlist=[""])
        if attribute is not None:
            return getattr(module, attribute)

        return module

    # Support packages
    sys.modules[f"lazy.{name}"] = ModuleAttributeProxy(name)

    return MyLazyObjectProxy(_import)


def __getattr__(name: str):
    return lazy_import(name)
