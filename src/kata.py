import shlex
import sys


#
# Apply Method
# @param input
# @param it
# @return
#    
def apply(list,it):
    #your code here
    return list;

def main() -> int:
    phrase = shlex.join(sys.argv)
    print(apply(["2","2"]))
    return 0

if __name__ == '__main__':
    sys.exit(main()) 