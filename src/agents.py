import random

class PlannerAgent:
    """Simulates planning and refining of user stories."""

    def refine(self, story: str) -> str:
        """Offline dummy refinement."""
        improvements = [
            "Added acceptance criteria for clarity.",
            "Simplified objectives for better understanding.",
            "Enhanced structure and readability.",
            "Added measurable goals and expected results.",
            "Improved sentence flow and precision."
        ]
        change = random.choice(improvements)
        return f"{story.strip()} ({change})"


class CriticAgent:
    """Simulates a critic agent that scores stories."""

    def score(self, story: str) -> int:
        """Returns a pseudo score between 40–100."""
        return random.randint(40, 100)
