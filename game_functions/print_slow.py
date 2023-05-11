#---Imports---#
import time

#type writer effect, as if the words are being typed as they are presented
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)
    print()
   