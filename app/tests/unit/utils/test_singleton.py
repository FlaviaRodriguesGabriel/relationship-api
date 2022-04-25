from threading import Thread
from typing import List

from utils import Singleton


class Klass(Singleton):
    attribute: str = "default_attribute"


class KlassWithAnotherKlass(Singleton):
    klass: Klass

    def __init__(self, *args, **kwargs) -> None:
        self.klass = Klass()
        super().__init__(*args, **kwargs)


def add_new_instance_klass(instances: List[Klass]) -> None:
    k = Klass()
    k.attribute = "new_attribute"
    instances.append(k)


def add_new_instance_klass_with_another_klass(
    instances: List[KlassWithAnotherKlass],
) -> None:
    k = KlassWithAnotherKlass()
    k.klass.attribute = "new_attribute"
    instances.append(k)


def add_new_thread_klass(instances: List[Klass], threads: List[Thread]) -> None:
    thread = Thread(target=add_new_instance_klass, args=(instances,))
    thread.start()
    threads.append(thread)


def add_new_thread_klass_with_another_klass(
    instances: List[KlassWithAnotherKlass], threads: List[Thread]
) -> None:
    thread = Thread(target=add_new_instance_klass_with_another_klass, args=(instances,))
    thread.start()
    threads.append(thread)


def test_singleton():
    instances: List[Klass] = []
    threads: List[Thread] = []
    add_new_thread_klass(instances, threads)  # Thread 0
    add_new_thread_klass(instances, threads)  # Thread 1

    for thread in threads:
        thread.join()

    assert instances[0].attribute == "new_attribute"
    assert instances[0].attribute == instances[1].attribute
    assert id(instances[0]) == id(instances[1])


def test_singleton_with_another_singleton():
    instances: List[KlassWithAnotherKlass] = []
    threads: List[Thread] = []
    add_new_thread_klass_with_another_klass(instances, threads)  # Thread 0
    add_new_thread_klass_with_another_klass(instances, threads)  # Thread 1

    for thread in threads:
        thread.join()

    assert instances[0].klass.attribute == "new_attribute"
    assert instances[0].klass.attribute == instances[1].klass.attribute
    assert id(instances[0].klass) == id(instances[1].klass)
    assert id(instances[0]) == id(instances[1])
