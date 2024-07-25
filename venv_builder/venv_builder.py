# Virtual Environment Commands
# | Command | Linux/Mac | GitBash |
# | ------- | --------- | ------- |
# | Create | `python3 -m venv venv` | `python -m venv venv` |
# | Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
# | Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
# | Deactivate | `deactivate` | `deactivate` |

# python3 -m venv venv

# source venv/bin/activate

import os
import subprocess

def install_package(package_name):
    print(f'Will you use {package_name}? (yes/no)')
    response = input().strip().lower()
    if response == 'yes':
        subprocess.run(['pip', 'install', package_name])

# Check if the user is creating a new project
response = input('Are you creating a new project (yes/no)? ').strip().lower()
is_creating_new_project = response == 'yes'

if is_creating_new_project:
    # Create a virtual environment
    os.system('python3 -m venv venv')
    
    # Activate the virtual environment
    if os.name == 'nt':
        activate_script = '.\\venv\\Scripts\\activate'
    else:
        activate_script = 'source venv/bin/activate'
    
    os.system(activate_script)
    
    # Prompt for each package
    install_package('pandas')
    install_package('numpy')
    install_package('matplotlib')
    install_package('plotly')
    install_package('scikit-learn')
