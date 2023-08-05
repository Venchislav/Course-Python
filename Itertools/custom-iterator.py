from typing import Self


class NumberIter:
    num: int = 0

    def __init__(self, max_num=10) -> None:
        self.max_num = max_num

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.num < self.max_num:
            self.num += 1
            return self.num
        else:
            raise StopIteration


if __name__ == '__main__':
    ni = NumberIter(1000)
    for i in ni:
        print(i)
