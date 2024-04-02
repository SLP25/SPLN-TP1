from collections import defaultdict
from typing import Callable, Iterator
from .Token import Base,Modifier

def enumerateWhen(it: Iterator[object], cond: Callable[[object],bool]) -> Iterator[tuple[int,object]]:
    i = -1
    for x in it:
        if cond(x):
            i += 1
        yield i, x


def collect(lis: list[Base]) -> dict[str,list[Base]]:
    d=defaultdict(list)
    for i in lis:
        d[i.text].append(i)
    return d

def collectModifiers(lis: list[Base]) -> dict[str,list[int]]:
    d=defaultdict(list)
    for i in lis:
        for mod,mask in i.modifiers:
            d[mod.text].append(mod.value*mask)
    return d