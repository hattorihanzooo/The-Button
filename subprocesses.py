import subprocess


def start_server():
    subprocess.Popen(["python", "my_server.py"])


def start_client():
    subprocess.Popen(["python", "my_client.py"])
