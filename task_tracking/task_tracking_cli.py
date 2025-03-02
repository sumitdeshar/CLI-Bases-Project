from json_utils import write_to_json, read_from_json
import cmd
import os


class TaskTrackingCLI(cmd.Cmd):
    prompt='TaskTracker-> '
    intro='Welcome to TaskTracker. Type "help" for available commands.'
    
    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()
        self.tasks_list = read_from_json()['data']
        print(self.tasks_list)
        # print(self.tasks_list.type)
        if self.tasks_list is None:
             self.tasks_list= []

    def do_view_cwd(self, line):
        """List files and directories in the current directory."""
        files_and_dirs = os.listdir(self.current_directory)
        for item in files_and_dirs:
            print(item)
    
    def do_add(self, line):
        """
        Add a new task.
        Usage: add <task_description>
        """
        if line:
            print('line',line)
            task_json = {"title": str(line), "status": "todo"}
            self.tasks_list.append(task_json)
            # print('task list',self.tasks_list)
            write_to_json(self.tasks_list)
            self.do_list_all()
        else:
            print("Usage: add <task_description>")
    
    def do_update(self, line):
        """
        Update existing task
        Usage: update index <task_description>
        """
        temp=line.split(" ",1)
        if len(temp) < 2:
            print("Usage: update index <task_description>")
            return
        try:
            pos = int(temp[0])-1
            # print(f"pos saved:",pos)
            task = temp[1]
            # print(f"task saved:",task)
            self.tasks_list[pos]['title']= task
            write_to_json(self.tasks_list)
            self.do_list_all()
        except(ValueError, IndexError):
            print("Invalid postion")

        
    def do_delete(self, line):
        """
        Delete existing task
        Usage: delete index
        """
        try:
            pos= int(line.strip()) - 1
            # print(pos)
            deleted_task= self.tasks_list[pos]
            confirm = input(f"Are you sure you want to delete '{deleted_task['title']} -on {deleted_task['status']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                self.tasks_list.pop(pos)
                write_to_json(self.tasks_list)
                print(f"Task {pos+1} deleted: {deleted_task['title']} -on {deleted_task['status']}")
                self.do_list_all()
            else:
                print("Deletion canceled.")
        except ValueError:
            print("Please enter a valid index!")
        except IndexError:
            print("Task index out of range!")
            
        
    
    def do_list_all(self, line=None):
        """List all existing tasks."""
        if self.tasks_list:
            print('-Title', '\t\t\t-Status')
            for index, task in enumerate(self.tasks_list):
                print(f"{index+1}. -{task['title']}\t-{task['status']}")
        else:
            print('No task has been added.')
            
    def do_list(self,line=str):
        """List existing tasks according to status."""
        if self.tasks_list:
            print('-Title', '\t\t\t-Status')
            for index, task in enumerate(self.tasks_list):
                if task["status"] == str(line):
                    print(f"{index+1}. -{task['title']}\t-{task['status']}")
        else:
            print('No task has been added.')
    
    def do_mark(self, line=str):
        """
        Update existing task's status
        Usage: update index <task_status>
        """
        temp=line.split(" ",1)
        if len(temp) < 2:
            print("Usage: update index <task_status>")
            return
        try:
            pos = int(temp[0])-1
            status = temp[1]
            self.tasks_list[pos]['status']= str(status)
            write_to_json(self.tasks_list)
            self.do_list_all()
        except(ValueError, IndexError):
            print("Invalid postion")

    def do_quit(self, line):
        """Exit the CLI."""
        return True
    
if __name__ == '__main__':
    TaskTrackingCLI().cmdloop()

        



