import subprocess
import os
text = 'Please tokenize this text.'
command = ['java', 'edu.stanford.nlp.process.PTBTokenizer',text, '-preserveLines']
p = subprocess.call(command)
out, err = p.communicate()
print out