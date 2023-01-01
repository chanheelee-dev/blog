from __future__ import annotations
from abc import ABC, abstractmethod
from creator import *


def client_code(creator: Creator) -> None:
    """
    client 입장에서는 특정한 concrete creator를 하나 불러와서 실행시킨다.
    concrete creator들이 Creator에서 지정해놓은 동작을 변경하지 않고 돌아가도록 짜야한다.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.business_logic()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
    print("")
