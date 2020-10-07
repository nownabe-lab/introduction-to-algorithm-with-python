import itertools

populations = [
    ('北海道', 5381733),
    ('青森県', 1308265),
    ('岩手県', 1279594),
    ('宮城県', 2333899),
    ('福井県', 786740),
    ('岐阜県', 2031903),
    ('鳥取県', 573441),
    ('徳島県', 755733),
    ('佐賀県', 832832),
    ('長崎県', 1377187),
]

target = 10000000

# combinations = []
#
# for n in range(1, len(populations) + 1):
#     for comb in itertools.combinations(populations, n):
#         combinations.append(list(comb))
#
# max_comb = None
#
# for comb in combinations:
#     sum = 0
#     for pref in comb:
#         sum += pref[1]
#
#     if max_comb is None:
#         max_comb = (comb, sum)
#
#     if abs(target - max_comb[1]) > abs(target - sum):
#         max_comb = (comb, sum)
#
# print(max_comb)

min_total = 0

def search(total, pos):
    global min_total
    if pos >= len(populations):
        return
    if total < target:
        if abs(target - (total + populations[pos][1])) < abs(target - min_total):
            min_total = total + populations[pos][1]
        search(total + populations[pos][1], pos + 1)
        search(total, pos + 1)

search(0, 0)
print(min_total)


