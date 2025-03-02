import cmd
import os
import json
from my_server import my_http

class Caching(cmd.Cmd):
    prompt='Cache_Server-> '
    intro='Welcome to TaskTracker. Type "help" for available commands.'
    
    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()
        
    def do_clear_cache(self, line=None):
        """ Clears cache data."""
        file_path = "json_cache.json"
    
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"-->{file_path} has been deleted.")
        else:
            print("-->File does not exist.")
    
    def do_fetch_data(self, line, update:bool =False):
        
        """Give request and get response.
        Format: fetch_data <dummyjson.com/products:get> as in <url>/<endpoint>:get   
        """
        url=line.split('/')[0]
        endpoint,method=line.split('/')[1].split(':')
        print(url, endpoint, method)
        
        json_cache= 'json_cache.json'
        if update:
            json_data = None
        else:
            try:
                with open(json_cache, 'r') as file:
                    json_data = json.load(file)
                    print('Fetched data from local cache!')
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f'No local cache found... ({e})')
                json_data = None

        if not json_data:
            print('Fetching new json data... (Creating local cache)')
            json_data = my_http(url=url, method=method.upper(), endpoint=f'/{endpoint}')
            with open(json_cache, 'w') as file:
                json.dump(json_data, file)
                
        first_five = json_data[:5]
        filtered_data = [{k: item[k] for k in ['title', 'tags', 'stock']} for item in first_five]
        print(filtered_data) 

    
    def do_quit(self, line):
        """Exit the CLI."""
        return True
    
if __name__ == '__main__':
    Caching().cmdloop()