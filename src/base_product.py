from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, который заставляет переопределять __init__ в каждом дочернем классе"""
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass
