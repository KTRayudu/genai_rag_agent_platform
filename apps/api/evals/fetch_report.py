import os
import datetime
from langsmith import Client
import csv

def main():
    ls_client = Client()
    projects = list(ls_client.list_projects(reference_dataset_name="ollama-70b-amazon-dataset"))
    if not projects:
        print("No evaluation projects found.")
        return

    # Get the latest evaluation project
    latest_project = sorted(projects, key=lambda p: getattr(p, "start_time", p.id), reverse=True)[0]
    
    # We know the app model is llama3.3:70b
    app_model = "llama3.3-70b"
    project_name = latest_project.name # e.g. retriever-eval_2026-09-24_...
    timestamp = project_name.replace("retriever-eval_", "")
    
    # Create results folder
    results_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(results_dir, exist_ok=True)
    
    # 1. Write the Detailed Markdown Report
    report_filename = os.path.join(results_dir, f"report_{app_model}_{timestamp}.md")
    runs = list(ls_client.list_runs(project_name=latest_project.name, is_root=True))
    
    total_scores = {}
    score_counts = {}

    with open(report_filename, "w") as f:
        f.write(f"# Evaluation Report: {project_name}\n")
        f.write(f"**Target Application Model:** {app_model}\n\n")
        
        for i, run in enumerate(runs):
            question = run.inputs.get("question", "Unknown Question") if run.inputs else "Unknown"
            answer = run.outputs.get("answer", "No Answer") if run.outputs else "No Answer"
            
            f.write(f"### Question {i+1}: {question}\n")
            f.write(f"**App Answer:** {answer}\n\n")
            
            feedbacks = list(ls_client.list_feedback(run_ids=[run.id]))
            if feedbacks:
                f.write("**Scores:**\n")
                for fb in feedbacks:
                    score = fb.score if fb.score != None else "N/A"
                    f.write(f"- **{fb.key}**: {score}\n")
                    
                    if fb.score != None:
                        total_scores[fb.key] = total_scores.get(fb.key, 0) + fb.score
                        score_counts[fb.key] = score_counts.get(fb.key, 0) + 1
            else:
                f.write("**Scores:** No scores recorded.\n")
            f.write("\n---\n\n")
            
    print(f"Detailed Q&A report saved to: {report_filename}")

    # 2. Append Average Scores to a CSV History Log
    csv_filename = os.path.join(results_dir, "evaluation_history.csv")
    file_exists = os.path.isfile(csv_filename)
    
    averages = {key: round(total / score_counts[key], 4) for key, total in total_scores.items()}
    
    # Ensure standard column order
    metric_keys = ["ragas_responce_relevancy", "ragas_faithfulness", "ragas_context_precision_id_based", "ragas_context_recall_id_based"]
    
    with open(csv_filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Timestamp", "App Model", "Project Name"] + metric_keys)
        
        row = [timestamp, app_model, project_name]
        for key in metric_keys:
            row.append(averages.get(key, "N/A"))
            
        writer.writerow(row)
        
    print(f"Average scores appended to: {csv_filename}")
    print("Averages:", averages)

if __name__ == "__main__":
    main()
