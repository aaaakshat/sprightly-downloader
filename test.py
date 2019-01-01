import os
import threading
import time
from tqdm import tqdm

'''
def threaded_function(chunk_size):
    desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
    filePath = os.path.join(desktopPath, "touch.txt")
    outputFile = open(filePath, mode='a')

    for i in range(chunk_size):
        outputFile.write("1")

    outputFile.close()

if __name__ == "__main__":
    global thread
    old = time.time()

    t = []
    threadnum = 20
    finalsize = 81500000
    chunksize = finalsize/threadnum
    for i in range(threadnum):
        thread =  threading.Thread(target=threaded_function, args=(int(chunksize),))
        t.append(thread)
        thread.start()

    for thread in t:
        thread.join()

    now = time.time()
    print("bytes written: %s threads: %s time taken: %s" % (finalsize, threadnum, now-old))
'''

def run():
    '''
    oldTime = time.time()

    downloadPath = os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), "tachyon")
    pathToWriteTo = os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), "tothisfolder")

    for i in range(0,20):
        os.rename(os.path.join(downloadPath, "text" + str(i) + ".txt"), os.path.join(pathToWriteTo, "text" + str(i) + ".txt"))

    print(time.time() - oldTime)
    '''
    old = time.time()
    downloadPath = os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), "tachyon")
    myFile = os.path.join(downloadPath, "text0.txt")
    outputFile = os.path.join(downloadPath, "text1.txt")

    with open(myFile, "a") as file:
        for i in range(0, 20):
            file.write(open(os.path.join(downloadPath, "text" + str(i) + ".txt"), "r").read())
    print(time.time() - old)

run()
