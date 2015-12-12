# todoist-cli

If I have time for it, I will expand to hit the other endpoints. But for now, this was merely an hour long adventure to allow me to quickly add tasks to todoist from the commandline.  

## Configuration
You are required to have a .todoist.cfg file in your home directory storing the token and default project name. This is in the format of:

```
[DEFAULT]
TOKEN = GetTokenFromYourTodoistSettings
DEFAULT_PROJECT_NAME = YourProjectNameHere
```

## Functions
```
$ python todoist.py -h 
usage: todoist.py [-h] [-p PROJECT] [-c CONTENT] [-d DUE] [-u URL] function
 
positional arguments:
function              Function to call: add, list, query, undo

optional arguments:  
  -h, --help            show this help message and exit  
  -p PROJECT, --project PROJECT  
                        project to add task to  
  -c CONTENT, --content CONTENT  
                        desired task, or query  
  -d DUE, --due DUE     Due when?  
  -u URL, --url URL     URL?
```

## Example usage

### Query
Queries the given content, if no content is given, return default content of today's tasks.
```
$ python todoist.py query -c "tomorrow"
> Inbox: Wake up early!
```

### List
Lists all available projects.
```
$ python todoist.py list               
[u'Inbox']
```

### Add
Adds a task with the given content, to the given project, with the given due date.
* due date defaults to None
* project defaults to Inbox
* content is required
```
$ python todoist.py add -c "update readme" -d "today" -p "Todoist-Cli"
update readme 
due Sun 13 Dec 2015 04:59:59 +0000 
added to project Todoist-Cli
```

### Undo
Undo last added todo item added with the add command.
```
$ python todoist.py undo
removed 176329184
```
