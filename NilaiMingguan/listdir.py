import os

for dirname, dirnames, filenames in os.walk('.'):
    if '.git' in dirnames:
        dirnames.remove('.git')

    # print path to all filenames.
    for filename in filenames:
        fname = os.path.join(dirname, filename)
        print('#### ', fname, "####" )
        with open(fname, 'r') as fin:
           print fin.read()
