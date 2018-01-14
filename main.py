import itertools
import math

possible_rankings = []

possible_evals = 3

for i in range(possible_evals):
    for j in range(possible_evals):
        for k in range(possible_evals):
            for l in range(possible_evals):
                for m in range(possible_evals):
                    new_list = [i, j, k, l, m]
                    possible_rankings.append(new_list)

p_rankings = possible_rankings
e_rankings = possible_rankings

possible_combinations = []
for comb in itertools.combinations(possible_rankings, 2):
    possible_combinations.append(comb)

def precision_rank(ranking, rank):
    relevant = 0
    for i in range(rank):
        if ranking[i] > 0:
            relevant += 1
    return relevant /rank


p_precision = precision_rank(p_rankings[100], 3)
print(p_precision)

def NDCG(ranking, rank):
    total_dcg = 0
    total_ideal_dcg = 0

    for i in range(rank):
        total_dcg += ((2**ranking[i])-1)/math.log2(1+i+1)
        ideal_ranking = sorted(ranking, reverse=True)
        total_ideal_dcg += ((2**ideal_ranking[i])-1)/math.log2(1+i+1)
    return total_dcg/total_ideal_dcg

p_ndcg = NDCG(p_rankings[10], 5)
print(p_ndcg)

#def epected_effort(ranking, rank):
