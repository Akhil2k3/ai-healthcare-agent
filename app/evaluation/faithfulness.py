def faithfulness_score(answer: str, context: str) -> float:
    answer_tokens = set(answer.lower().split())
    context_tokens = set(context.lower().split())

    if not answer_tokens:
        return 0.0

    overlap = answer_tokens.intersection(context_tokens)
    score = len(overlap) / len(answer_tokens)

    return round(score, 2)