
### make app deamon or move to nas. Imports do not work

import signal
import requests

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

stream_url = 'http://your-stream-source.com/stream'

r = requests.get(stream_url, stream=True)


with open('stream.mp3', 'wb') as f:
    # Start the timer. Once 5 seconds are over, a SIGALRM signal is sent.
    signal.alarm(5)    
    # This try/except loop ensures that 
    #   you'll catch TimeoutException when it's sent.
    try:
        for block in r.iter_content(1024):
            f.write(block)
    except TimeoutException:
        continue # continue the for loop if function A takes more than 5 second
    else:
        # Reset the alarm
        signal.alarm(0)
