#!/usr/bin/python3
'''
Author: Ryan McCormick
Date:   02/25/2019

Small tool to lint the outputs of rendered helm templates. This was created 
because the yaml linter's I used did not like the helm/golang template syntax.
'''

import os
import sys
import subprocess

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('USAGE: python3 helm_template_linter.py <HELM CHART>')

    # pip3 install yamllint OR sudo apt install yamllint
    try:
        cp = subprocess.run(["yamllint", "-v"], stdout=subprocess.PIPE)
    except FileNotFoundError:
        print('ERROR: yamllint not found.')
        sys.exit('>> Please install yamllint. Try `pip3 install yamllint`.')

    CHART_DIR = sys.argv[1]
    # Render individual template file
    #TEMPLATE = sys.argv[2]
    #cp = subprocess.run(["helm", "template", CHART_DIR, "-x", TEMPLATE], stdout=subprocess.PIPE)

    # Render all template files
    cp = subprocess.run(["helm", "install", "--dry-run", "--debug", CHART_DIR], stdout=subprocess.PIPE)
    # Split each rendered yaml template by their '---' headers
    yaml_files = cp.stdout.decode().split('---\n')[1:]

    # Write each rendered yaml template to a local file for linting
    filenames = []
    for i, yaml_lines in enumerate(yaml_files):
        # Get file path from first line of rendered output
        filename = yaml_lines.split('\n', 1)[0].split(' ')[-1]
        # Get only filename at the end of the file path
        filename = 'rendered-' + os.path.basename(os.path.normpath(filename))
        #filename = f'template{i}.yaml'
        filenames.append(filename)
        print(f'Writing {filename} ...')

        with open(filename, 'w') as yf:
            yaml_lines = '---\n' + yaml_lines
            yf.write(yaml_lines)

    for filename in filenames:
        cp = subprocess.run(["yamllint", "-d", "{extends: default, rules: {line-length: {level: warning}}}", filename], stdout=subprocess.PIPE)
        output = cp.stdout.decode().strip()
        if output:
            print(output)
