from llama_index.core.indices.managed.base import BaseManagedIndex
from llama_index.indices.managed.vertexai import VertexAIIndex


def test_class():
    names_of_base_classes = [b.__name__ for b in VertexAIIndex.__mro__]
    assert BaseManagedIndex.__name__ in names_of_base_classes
