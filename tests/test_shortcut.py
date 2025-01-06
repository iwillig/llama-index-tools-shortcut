from llama_index.core.tools.tool_spec.base import BaseToolSpec
from llama_index.tools.shortcut import ShortcutToolSpec

def test_class():
    name_of_base_cls = [a.__name__ for a in ShortcutToolSpec.__mro__]
    assert BaseToolSpec.__name__ in name_of_base_cls
