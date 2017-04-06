import sys

len_arg = len(sys.argv)
print("Number of inputs = ", len_arg)
for i in range(0, len_arg):
    print("Input ",i,": Text=",str(sys.argv[i]),",\tType=", str(type(sys.argv[i])))   
