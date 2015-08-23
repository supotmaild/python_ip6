import socket,sys,time,threading
import Tkinter as tk
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
global time,tk,t,threading,on_closing,server_start,keep_running,click,KEEP_RUNNING
global socket,server,HTTPServer,SimpleHTTPRequestHandler,HTTPServerV6,MyHandler
global label1

class MyHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/ip':
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write('Your IP address is %s' % self.client_address[0])
      return
    else:
      return SimpleHTTPRequestHandler.do_GET(self)

class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6

def on_closing():
  global server,KEEP_RUNNING
  KEEP_RUNNING = False
  server.server_close()
  print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
  win.destroy()

KEEP_RUNNING = False

def keep_running():
    global KEEP_RUNNING
    return KEEP_RUNNING

def server_start():
  global server
  server = HTTPServerV6(('::', 80), MyHandler)
  while keep_running():
    server.handle_request()
  #server.serve_forever()

def click():
  global t,label1,KEEP_RUNNING
  if KEEP_RUNNING:
    label1.configure(text='Server off')
    KEEP_RUNNING = False
  else:
    label1.configure(text='Server on')
    KEEP_RUNNING = True
    t = threading.Thread(target=server_start)
    t.start()

def main():
  global label1
  win=tk.Tk()
  win.title('ip6 Web Server 1.0')
  win.protocol("WM_DELETE_WINDOW", on_closing)
  frame1 = tk.Frame(
    master = win,
    width = 640,
    height = 550,
    bg = '#808000'
  )
  button1=tk.Button(frame1,width=20,height=1,text='SERVER START',command=click)
  button1.place(x=20,y=20)
  label1=tk.Label(frame1,text='Server off',fg='#ffffff', bg='#808000')
  label1.place(x=180,y=20)
  frame1.pack(fill='both', expand='yes')
  win.mainloop()

main()
