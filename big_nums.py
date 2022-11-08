import sys
print(sys.float_info)

def useLargeNumbers():
    initial = 10
    power   = 100000
    result = initial**power
    print(result)

if __name__ == '__main__':
    # python has no practical limitations to the size of data members it can handle
    # However, be careful - python can exhaust the resources of your system
    useLargeNumbers()

