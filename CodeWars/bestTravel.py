#https://www.codewars.com/kata/best-travel/train/python
import itertools
def choose_best_sum(t, k, ls):
    max = 0

    posiblePositions = (list(itertools.combinations(ls, k)))
    for elements in posiblePositions:
        sumTotal = 0
        for number in elements:
            sumTotal = sumTotal + number

        if sumTotal >= max and sumTotal <= t:
            max = sumTotal

    if max != 0:
        return max
    else:
        return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
