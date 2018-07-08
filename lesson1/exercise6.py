from __future__ import unicode_literals, print_function
import yaml
import json

def main():
    ytest = 'test.yml'
    jtest = 'test.json'
    dictionary = {
        'type':'cisco',
        'device':'switch',
        'use':'branches'
    }
    testlist = [
        'hello',
        123,
        'world'
    ]
    with open(ytest, "w") as f:
        f.write(yaml.dump(testlist, default_flow_style=False))
    with open (jtest, "w") as f:
        json.dump(testlist, f)



if __name__ == "__main__":
    main()
