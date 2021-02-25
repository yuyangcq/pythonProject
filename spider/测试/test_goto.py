import goto
import label as label
from goto import *

@with_goto
def func():
    label .begin
    for i in range(8):
        for j in range(8):
            if(i==1):
                goto .end
    label .end
    return (i, j)

if __name__ == '__main__':
    print(func())