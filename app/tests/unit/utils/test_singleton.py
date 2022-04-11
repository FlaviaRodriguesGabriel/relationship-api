from threading import Thread
from typing import List

from utils import SingletonMeta


class Klass(metaclass=SingletonMeta):
    attribute: str = "default_attribute"


def add_new_instance(instances: List[Klass]) -> None:
    k = Klass()
    k.attribute = "new_attribute"
    instances.append(k)


def add_new_thread(instances: List[Klass], threads: List[Thread]) -> None:
    thread = Thread(target=add_new_instance, args=(instances,))
    thread.start()
    threads.append(thread)


def test_singleton():
    instances: List[Klass] = []
    threads: List[Thread] = []
    add_new_thread(instances, threads)  # Thread 0
    add_new_thread(instances, threads)  # Thread 1

    for thread in threads:
        thread.join()

    assert instances[0].attribute == "new_attribute"
    assert instances[0].attribute == instances[1].attribute
    assert id(instances[0]) == id(instances[1])
