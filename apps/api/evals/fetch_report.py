import os
from langsmith import Client

def main():
    ls_client = Client()
    projects = list(ls_client.list_projects(reference_dataset_name="ollama-70b-amazon-dataset"))
    if not projects:
        print("No evaluation projects found.")
        return

    # Get the latest evaluation project
    latest_project = sorted(projects, key=lambda p: getattr(p, "start_time", p.id), reverse=True)[0]
    print(f"# Evaluation Report: {latest_project.name}\n")
    
    runs = list(ls_client.list_runs(project_name=latest_project.name, is_root=True))
    
    for i, run in enumerate(runs):
        question = run.inputs.get("question", "Unknown Question") if run.inputs else "Unknown"
        answer = run.outputs.get("answer", "No Answer") if run.outputs else "No Answer"
        
        print(f"### Question {i+1}: {question}")
        print(f"**App Answer:** {answer}\n")
        
        feedbacks = list(ls_client.list_feedback(run_ids=[run.id]))
        if feedbacks:
            print("**Scores:**")
            for fb in feedbacks:
                score = fb.score if fb.score != None else "N/A"
                print(f"- **{fb.key}**: {score}")
        else:
            print("**Scores:** No scores recorded.")
        print("\n---\n")

if __name__ == "__main__":
    main()
