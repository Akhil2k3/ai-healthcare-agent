def confidence_score(answer: str, context: str) -> float:
    answer_len = len(answer.split())
    context_len = len(context.split())

    if context_len == 0:
        return 0.0

    ratio = min(answer_len / context_len, 1.0)
    return round(ratio, 2)