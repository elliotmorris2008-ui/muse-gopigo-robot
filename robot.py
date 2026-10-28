import socket
import easygopigo3 as e
g = e.EasyGoPiGo3()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5005))
print("ready")
while True:
    d = s.recvfrom(16)[0].decode()
    if d == "F":
        g.drive_cm(20)
    if d == "R":
        g.turn_degrees(45)
