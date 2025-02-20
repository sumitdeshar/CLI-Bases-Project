import cmd

class TaskTrackingCLI(cmd.Cmd):
    prompt='TaskTracker-> '
    intro='Welcome to TaskTracker. Type "help" for available commands.'
    
    def __init__(self):
        super().__init__()
        self.tasks = []
        
    def do_add(self,line):
        """Add a new task"""
        
        



