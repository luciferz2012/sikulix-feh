def tryWaitAndClick(p, w1=0.1, w2=0):
    try:
        print(p)
        m = wait(p, w1)
        wait(w2)
        click(m)
        return True
    except:
        pass

def findClick(ps):
    for p in ps:
        tryWaitAndClick(p)

def auto():
    if tryWaitAndClick("1499786291662.png", w2=4) \
            and tryWaitAndClick("1499786340986.png", w1=4) \
            and tryWaitAndClick("1499786373715.png", w1=4):
        for i in range(256):
            if tryWaitAndClick("1499786636807.png"):
                return True
            elif tryWaitAndClick("1499786835386.png"):
                return False

commons = [
       "1499785682235.png",
       "1499785699548.png",
       "1499786073887.png",
       "1499865066440.png",
       "1499786983787.png",
       "1499788779460.png",
       ]

def main():
    for i in range(64):
        findClick(commons)
        auto()

if __name__ == '__main__':
    main()