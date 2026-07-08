# === Stage 61: Add performance timing for core list and search operations ===
# Project: MealWorkshop
import time
from datetime import timedelta


class PerformanceTimer:
    """Compact timing utility for core list and search operations."""

    _timings = {}

    @classmethod
    def measure(cls, operation_name, func):
        start = time.perf_counter()
        result = func()
        elapsed_ms = (time.perf_counter() - start) * 1000
        cls._timings[operation_name] = {
            "avg_ms": elapsed_ms,
            "count": getattr(cls, operation_name, {}).get("count", 0) + 1,
            "total_ms": getattr(cls, operation_name, {}).get("total_ms", 0) + elapsed_ms,
        }
        return result

    @classmethod
    def get_report(cls):
        report = {}
        for name, data in cls._timings.items():
            avg = data["avg_ms"] / max(data["count"], 1)
            report[name] = {
                "average_ms": round(avg, 2),
                "total_calls": data["count"],
                "total_time_ms": round(data["total_ms"], 2),
            }
        return report

    @classmethod
    def clear(cls):
        cls._timings.clear()


# Example usage: measure a list search operation
class RecipeSearch:
    recipes = [
        {"name": "Pasta", "ingredients": ["pasta", "tomato sauce"], "cost": 5.0},
        {"name": "Salad", "ingredients": ["lettuce", "tomato"], "cost": 3.0},
        {"name": "Soup", "ingredients": ["broth", "vegetables"], "cost": 2.5},
    ]

    @staticmethod
    def find_recipes_by_ingredient(ingredient):
        return [r for r in RecipeSearch.recipes if ingredient.lower() in {i.lower() for i in r["ingredients"]}]


# Benchmarking the search operation with performance timing
def benchmark_search():
    print("Running benchmarks...")

    # Warm-up run
    _ = find_recipes_by_ingredient("tomato")

    # Measure multiple calls to get a meaningful average
    def perform_search(ingredient):
        return RecipeSearch.find_recipes_by_ingredient(ingredient)

    PerformanceTimer.measure("search_by_tomato", lambda: perform_search("tomato"))
    PerformanceTimer.measure("search_by_pasta", lambda: perform_search("pasta"))
    PerformanceTimer.measure("search_by_vegetables", lambda: perform_search("vegetables"))

    report = PerformanceTimer.get_report()
    print("\nPerformance Report:")
    for op, stats in report.items():
        print(f"  {op}: avg={stats['average_ms']}ms, calls={stats['total_calls']}, total={stats['total_time_ms']}ms")


if __name__ == "__main__":
    benchmark_search()
