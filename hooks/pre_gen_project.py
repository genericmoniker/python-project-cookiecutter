import re
import sys

DIST_REGEX = r'^[a-zA-Z][_\-a-zA-Z0-9]+$'
dist_name = '{{ cookiecutter.distribution_name }}'

MODULE_REGEX = r'^[a-zA-Z][_a-zA-Z0-9]+$'
package_name = '{{ cookiecutter.package_name }}'

if not re.match(DIST_REGEX, dist_name):
    print('ERROR:', dist_name, 'is not a valid Python distribution name!')
    sys.exit(1)

if not re.match(MODULE_REGEX, package_name):
    print('ERROR:', package_name, 'is not a valid Python package name!')
    sys.exit(1)
