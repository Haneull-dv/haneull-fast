from abc import ABCMeta, abstractmethod


class AbstractStock(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, **kwargs):
        pass