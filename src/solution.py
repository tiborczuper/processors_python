from __future__ import annotations
from itertools import chain
from typing import cast
from model import cpu
from queries import Queries
from common.repository import Repository

class Solution(Repository, Queries):
    @staticmethod
    def type_mapper(values: dict[str, any]) -> cpu | cpu.smartphone:
        match values:
            case {"id":_}:
                cp = cpu(**values)
                for v in cpu.manufacturer:
                    if v.value == cp.company:
                        cp.company = v
                        break
                return cp
            case{"year":_}:
                return cpu.smartphone(**values)

    @property
    def entities(self) -> list[object]:
        return cast(list[object],super().entities)

    def count_cpus(self) -> int:
        return len(self.entities)
    def order(self) -> list[cpu]:
        return sorted(
            self.entities, key= lambda x :(-x.core,-x.speed)
        )
    def getcpusbyid(self,id) -> cpu:
        for v in self.entities:
            if v.id == id:
                return v
    def year(self, year) -> list[cpu.smartphone]:
        telefonok = []
        for v in self.entities:
            for t in v.connected_phones:
                if t.year > year:
                    telefonok.append(t)
        return telefonok
    def group_by_manufacturer(self) -> dict[cpu.manufacturer,list[cpu]]:
        csoportos = {}
        for v in cpu.manufacturer:
            csoportos[v] = []
        for v in self.entities:
            csoportos[v.company].append(v)
        return csoportos

def main():
    repository = Solution(r"../data/data.json")
    for cpu in repository.entities:
        print(cpu)

    a = repository.count_cpus()
    print(f"\nÖsszesen {a} db processzor található.")

    b = repository.order()
    print(f"\n{b}")

    c = repository.getcpusbyid(2)
    print(f"\n{c}")

    d = repository.year(2018)
    print(f"\n{d}")

    f = repository.group_by_manufacturer()
    print()
    for k,v in f.items():
        print(k,v)

if __name__ == '__main__':
    main()