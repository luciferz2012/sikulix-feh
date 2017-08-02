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
    if tryWaitAndClick("menu.png", w2=4) \
            and tryWaitAndClick("auto battle 1.png", w1=4) \
            and tryWaitAndClick("auto battle 2.png", w1=4):
        for i in range(256):
            if tryWaitAndClick("clear.png"):
                return True
            elif tryWaitAndClick("lose.png"):
                return False

commons = [
       "1499785682235.png",
       "1499785699548.png",
       "fight1.png",
       "fight2.png",
       "ok.png",
       "close.png",
       ]

def main():
    # for i in range(64):
    for i in range(64 * 64):
        findClick(commons)
        auto()

if __name__ == '__main__':
    main()