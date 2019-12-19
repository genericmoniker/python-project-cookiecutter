import datetime
import sys

def replace_in_file(filename, search, replace):
    with open(filename) as f:
        project_file = f.read()
        project_file = project_file.replace(search, replace)

    with open(filename, 'w') as f:
        f.write(project_file)
    

python_version = str(sys.version_info.major) + '.' + str(sys.version_info.minor)

replace_in_file('pyproject.toml', '{python_version}', python_version)
