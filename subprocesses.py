import subprocess

# Данный модуль позволяет перейти от mainMenu к my_server и my_client наиболее простым путём


def start_server():
    subprocess.Popen(["python", "my_server.py"])


def start_client():
    subprocess.Popen(["python", "my_client.py"])
