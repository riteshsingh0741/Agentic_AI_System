import os
from src.utils import ensure_data_dir, read_csv, save_csv
from src.agents import PlannerAgent, CriticAgent
from src.evaluator import evaluate_dataset

def main():
    print("Loading stories...")
    ensure_data_dir()
    stories = read_csv("data/raw_user_stories.csv")

    # ✅ Add this line:
    print(f"Total stories loaded: {len(stories)}")

    print("Refining stories through Planner and Critic Agents...")
    planner, critic = PlannerAgent(), CriticAgent()
    refined_stories, raw_scores, refined_scores, ids = [], [], [], []

    for story_id, story_text in stories:
        plan = planner.refine(story_text)
        refined_stories.append(plan)
        ids.append(story_id)
        raw_scores.append(critic.score(story_text))
        refined_scores.append(critic.score(plan))

    print("Saving refined stories...")
    save_csv(ids, refined_stories, "data/refined_user_stories.csv")

    print("Evaluating improvements...\n")
    metrics = evaluate_dataset(raw_scores, refined_scores)

    print("Process completed successfully!")
    print(metrics)

if __name__ == "__main__":
    main()
