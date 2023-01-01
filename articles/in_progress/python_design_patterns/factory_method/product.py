from abc import ABC, abstractmethod


class Product(ABC):
    """
    모든 종류의 제품들이 실행할 행동을 선언해주는 인터페이스이다.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    """
    ConcreteProduct들에서 위의 Product의 인터페이스에 맞는 구현을 한다.
    """
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"