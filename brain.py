import time, socket
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(c):
    s.sendto(c, ("10.10.10.10", 5005))

b = BoardShim(BoardIds.MUSE_2_BOARD, BrainFlowInputParams())
ch = BoardShim.get_eeg_channels(BoardIds.MUSE_2_BOARD)[1]
b.prepare_session()
b.start_stream()

def sat():
    d = b.get_current_board_data(50)
    if d.shape[1] < 50:
        return 0
    return np.sum(np.abs(d[ch]) > 900)

print("go")
try:
    while True:
        time.sleep(0.1)
        if sat() > 35:
            time.sleep(0.3)
            if sat() > 35:
                print("DOUBLEBLINK")
                send(b"R")
            else:
                print("BLINK")
                send(b"F")
            time.sleep(2)
except KeyboardInterrupt:
    b.stop_stream()
    b.release_session()

