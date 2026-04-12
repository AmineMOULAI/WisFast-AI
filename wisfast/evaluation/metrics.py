from typing import List

def precision_at_k(actual: List[int], predicted: List[int], k: int) -> float:
    """Computes Precision@K."""
    if not actual or k == 0:
        return 0.0
    pred_k = predicted[:k]
    relevant_retrieved = sum(1 for p in pred_k if p in actual)
    return relevant_retrieved / k

def recall_at_k(actual: List[int], predicted: List[int], k: int) -> float:
    """Computes Recall@K."""
    if not actual:
        return 0.0
    pred_k = predicted[:k]
    relevant_retrieved = sum(1 for p in pred_k if p in actual)
    return relevant_retrieved / len(actual)

def average_precision(actual: List[int], predicted: List[int], k: int) -> float:
    """Computes Average Precision@K for a single query."""
    if not actual:
        return 0.0
    score = 0.0
    num_hits = 0.0
    for i, p in enumerate(predicted[:k]):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)
    return score / min(len(actual), k)

def mean_reciprocal_rank(actual: List[int], predicted: List[int]) -> float:
    """Computes Mean Reciprocal Rank for a single query."""
    for i, p in enumerate(predicted):
        if p in actual:
            return 1.0 / (i + 1)
    return 0.0