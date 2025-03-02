import json
import os

def write_to_json(tasks: list):
    file_path = "tasks.json"
    
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)
        
    print(f"-->Tasks saved to {file_path}")
    
    return {"msg": "Tasks have been written."}

def read_from_json():
    file_path = "tasks.json"
    
    if not os.path.exists(file_path):
        print(f"-->{file_path} does not exist. Creating empty task list.")
        return {"tasks": [], "msg": "No existing tasks found. Created empty list."}
    
    with open(file_path, "r") as file:
        tasks = json.load(file)
        if tasks is None:
            tasks=[]
    
    # print("Loaded tasks:", tasks)
    return {"data": tasks, "msg": "Tasks have been read."}

def hit_reset():
    file_path = "tasks.json"
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"-->{file_path} has been deleted.")
    else:
        print("-->File does not exist.")
        
if __name__ == "__main__":
    hit_reset()