import time
from valkka.core import *

live_out_filter =InfoFrameFilter("live_out_filter")

livethread =LiveThread("livethread")

ctx =LiveConnectionContext(LiveConnectionType_udp, \
		"192.168.54.1:65415", 1, live_out_filter)
# 192.168.54.10:49152 

livethread.startCall()
livethread.registerStreamCall(ctx)
livethread.playStreamCall(ctx)
time.sleep(5)
livethread.stopCall()
print("bye")
