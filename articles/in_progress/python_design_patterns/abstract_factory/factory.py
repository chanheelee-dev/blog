from abc import ABC, abstractmethod
from product import *

class AbstractFactory(ABC):
    """
    AbstractFactory는 각 팩토리들의 생성 method들을 선언해주는 인터페이스이다.
    이 생성 method는 AbstractProduct, 즉 추상적인 제품을 생성한다.
    구체적인 제품의 종류는 각 팩토리에서 구현한다.

    Factory method와 가장 크게 다른 점은 여기에 비즈니스 로직이 포함되지 않는다는 것이다.
    그저 생성에 대한 인터페이스만 제공한다.

    여기서 생성되는 제품들은 하나의 family라고 불리며, high-level 수준의 개념적으로 연관돼있다.
    Family는 여러 variant가 있을 수는 있지만, 
    서로 다른 variant끼리는 일반적으로 호환이 안된다. 
    (Family 내부 제품끼리 협업 가능성도 있기 때문에)
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


if __name__ == "__main__":
    # test code for ConcreteFactory1
    cf1 = ConcreteFactory1()

    p1a = cf1.create_product_a()
    p1b = cf1.create_product_b()

    print(p1a.useful_function_a())
    print(p1b.another_useful_function_b(p1a))
