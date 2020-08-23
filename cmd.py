
import subprocess
import sys
import random


insultlist = ['By popular demand your code is in /dev/null/', 'Your code is so bad, your child processes disowned you', 'Your mom circulates like a pulic key, seving more requests that HTTP', 'God must have had a broken GPU when he made you', 'This is the goverments plan to see if monkeys can type. And I have to say, they successfully accomplished that.', 
             'N00b', 'I never believed in chaos theory until I saw your code!']

initcommand = sys.argv[1]

cmd = [initcommand]

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, text=True)
 
out, err = p.communicate()


if out != '':
    print(out)
    
else:
    print(random.choice(insultlist))
