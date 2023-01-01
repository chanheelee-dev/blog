from abc import ABC, abstractmethod
from product import Product, ConcreteProduct1, ConcreteProduct2

class Creator(ABC):
    """
    Creator의 가장 중요한 responsibility는 바로 공통의 코어 비즈니스 로직을 관리하는 것이다.
    이런 비즈니스 로직은 Product라는 인터페이스가 가지고 있는 attr, method를 가지고 구현한다.
    이 인터페이스에서 제품들의 일반적인 행동을 정의하고 있다고 가정한다.
    """

    @abstractmethod
    def factory_method(self):
        """
        구체적인 구현은 ConcreteCreator에서 관여한다.
        디폴트 부분을 여기서 구현할 수도 있다.
        """
        pass

    def business_logic(self) -> str:
        """
        factory_method로 어떤 종류의 제품이 생성될지는 ConcreteCreator에서 정할 것이다. 
        이제 factory_method 및 제품의 행동이 잘 정의됐다고 치고,
        코어 비즈니스 로직을 실행한다.

        이 로직이 어떤 팩토리인지 종류마다 달라질 경우에는 다른 패턴을 사용하는 것이 좋을 것이다.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(Creator):
    """
    ConcreteCreator들의 가장 중요한 responsibility는 
    구체적인 제품 type을 정해서 생성해주는 것이다.
    Creator의 인터페이스 부분을 override해서 구현한다.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


if __name__ == "__main__":
    # test code
    cc1 = ConcreteCreator1()
    cc2 = ConcreteCreator2()

    print(cc1.business_logic())
    print(cc2.business_logic())
