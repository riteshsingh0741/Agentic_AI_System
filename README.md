# 🤖 Agentic AI System

## 📋 Overview
The **Agentic AI System** simulates an intelligent pipeline that refines user stories through two conceptual agents:

- **PlannerAgent** – Improves and rewrites stories for clarity and structure.  
- **CriticAgent** – Scores each story before and after refinement.

This project works **offline (without OpenAI API)** by simulating AI behavior locally using Python logic.

---

## 🧠 Workflow
1. Read raw user stories from `data/raw_user_stories.csv`.  
2. Refine stories using simulated agents.  
3. Score both raw and refined stories.  
4. Save improved stories and performance metrics.  
5. Visualize average improvement with a bar chart.

---

## 🗂️ Project Structure

Agentic_AI_System/
├── data/
│ ├── raw_user_stories.csv               # Input: contains 'id' and 'story' columns
│ └── refined_user_stories/              # Output: contains AI-refined/improved user stories after processing
├── reports/
│ ├── metrics_report.txt                 # Output: improvement metrics
│ └── story_scores.csv (optional)
├── src/
│ ├── agents.py                          # PlannerAgent & CriticAgent classes
│ ├── evaluator.py                       # Computes improvement metrics
│ └── utils.py                           # Handles CSV and directory management
├── main.py                              # Runs the entire pipeline
├── visualize_results.py                 # Generates bar chart visualization
├── requirements.txt                     # Dependencies list
└── README.md                            # Documentation

---

## 🪜 Step-by-Step Setup Summary

| Step | Action | Command |
|------|--------|---------|
| 🏗️ 1 | Create project folders | `mkdir -p Agentic_AI_System/{data,reports,src}` |
| 📄 2 | Add your `.py` files (`main.py`, `agents.py`, etc.) | 
| 🧾 3 | Create `requirements.txt` | copy above |
| 📘 4 | Create `README.md` | copy above |
| 🧩 5 | Install packages | `pip install -r requirements.txt` |
| ▶️ 6 | Run pipeline | `python main.py` |
| 📊 7 | Visualize improvement | `python visualize_results.py` |

---

## ⚙️ Dependencies
The project requires the following Python packages (listed in `requirements.txt`):

- `pandas`          # For reading/writing CSVs
- `numpy`           # For numerical calculations (optional)
- `tqdm`            # For progress bars (optional)
- `regex`           # For advanced pattern matching (optional)
- `jupyter`         # If using notebooks

> ❌ Note: `openai`, `langchain`, and `python-dotenv` are **not required** because the system runs offline.

---

## 📂 Notes
- Place your **raw stories** in `data/raw_user_stories.csv`.  
- The **refined stories** will automatically be saved in `data/refined_user_stories/`.  
- Metrics and scoring results are stored in `reports/`.  

---

## 🖼️ Visualization
Use `visualize_results.py` to generate bar charts showing the **average improvement** of user stories after AI refinement.
