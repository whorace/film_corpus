from extraction import Extraction
import time
startTime = time.time()
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(startTime)) 
extract1 = Extraction()
extract1.loadData()
extract1.run()
endTime = time.time()
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(endTime)) 
seconds = endTime - startTime
print seconds
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print "%d:%02d:%02d" % (h, m, s)
