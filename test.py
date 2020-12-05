
n_cages, years = int(input()), int(input())
cages = [list(map(int, input().split()))[:-1] for _ in range(n_cages)]


def update_cage(cage):
    sick, healthy = cage
    if sick == 0:
        return cage
    if healthy == 0:
        return [0, 0]
    return [min(healthy, 2*sick), max(healthy-2*sick, 0)]


# print(cages)

for year in range(years):
    cages = list(map(update_cage, cages))
    summ = sum([sum(cage) for cage in cages])
    print(summ)
    if summ == 0:
        break
