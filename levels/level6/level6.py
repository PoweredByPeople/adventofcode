"""
Day 6!
"""

def start_of_packet(filename):
    with open(filename, encoding="utf-8") as datastream_buffer:
        data = datastream_buffer.read()
        l, r = 0, 14

        while r < len(data):
            chars = data[l:r]
            if len(chars) > len(set(chars)):
                l += 1
                r += 1
            else:
                print(r)
                break

start_of_packet("levels/level6/level6data.txt")