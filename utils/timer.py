# Vehicle weights for density calculation
WEIGHTS = {
    "motorcycle": 1,
    "car": 2,
    "bus": 6,
    "truck": 8
}

# Signal timing configuration
TOTAL_CYCLE_TIME = 80
MIN_GREEN_TIME = 10
MAX_GREEN_TIME = 30


def calculate_density(vehicle_counts):
    """
    Calculate traffic density score.
    """
    score = 0

    for vehicle, count in vehicle_counts.items():
        score += WEIGHTS[vehicle] * count

    return score


def allocate_timers(road_scores):
    """
    Allocate green signal times based on density.

    Roads with zero vehicles are skipped (0 seconds).
    """

    total_score = sum(score for _, score in road_scores if score > 0)

    result = []

    # If all roads are empty
    if total_score == 0:
        for road, score in road_scores:
            result.append((road, score, 0))
        return result

    for road, score in road_scores:

        # Skip empty roads
        if score == 0:
            timer = 0
        else:
            timer = round((score / total_score) * TOTAL_CYCLE_TIME)

            # Keep timer between 10 and 30 seconds
            timer = max(MIN_GREEN_TIME, min(timer, MAX_GREEN_TIME))

        result.append((road, score, timer))

    # Highest density first
    result.sort(key=lambda x: x[1], reverse=True)

    return result