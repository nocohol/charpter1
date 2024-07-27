"""module providing a function time controlling"""
import time

def connect() -> None:
    """connect to internet"""    
    print('Connect to server ...')
    time.sleep(3)
    print('Connected!')


if __name__ == '__main__':
    connect()
