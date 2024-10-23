from __future__ import annotations
from abc import abstractmethod, ABC

from model import cpu

class Queries(ABC):
    @abstractmethod
    def count_cpus(self) -> int:
        """
        megszámolja hány cpu van.
        """
    def order(self) -> list[cpu]:
        """
        A rendezési szempont lambda kifejezéssel kerül megadásra.
        core csökkenő, speed csökkenő
        """
    def getcpusbyid(self,id) -> cpu:
        """
        Id-t kap meg, és kilistázza azt a processzort, amely azzal az id-val rendelkezik.
        """
    def year(self, year) -> list[cpu.smartphone]:
        """
        Ki listázza azokat a telefonokat, amely a megadott évszám után gyártottak.
        """
    def group_by_manufacturer(self) -> dict[cpu.manufacturer,list[cpu]]:
        """
        Gyártó alapján kigyújti azokat a processzorokat, amelyeket az a gyártó gyártotta
        """