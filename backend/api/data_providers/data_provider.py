from abc import ABC, abstractmethod


class DataProvider(ABC):
    @property
    @abstractmethod
    def session(self):
        pass

    @abstractmethod
    def get_class_data(self):
        pass

    @abstractmethod
    def get_grade_data(self):
        pass
