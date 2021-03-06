# a class decorator:
# It does essentially the same thing as the wrapper() function in our earlier examples.
# Note that you need to use the functools.update_wrapper() function instead of @functools.wraps.
from dataclasses import dataclass
from decoratorexamples import timer

@dataclass
class PlayingCard:
    rank: str
    suit: str

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])