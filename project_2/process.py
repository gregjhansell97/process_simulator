#This class describes the memory attributes of a process
#
#Variables:
#letter: the name of the process like 'A', 'B' ... (assumed to be length 1)
#size: how many frames the process needs of memory
#start: when the process starts needing the memory (given clock time)
#end: when the process ends needing the memory (given clock time)
class Process(object):

    #Parameters
    #letter: the name of the process like 'A', 'B' ... (assumed to be length 1)
    #size: how many frames the process needs of memory
    #start: when the process starts needing the memory (given clock time)
    #length: how long the process needs the memory for
    def __init__(self, letter, size, start, length):
        self.arrived = True
        self.start = start
        self.size = size
        self.end = start + length
        self.letter = letter
        self.in_memory = False

    #overriden system functions (used for sorting and printing/casting)
    def __str__(self):
        return self.letter
    def __lt__(self, other):
        if(self.start < other.start):
            return True
        elif(self.start > other.start):
            return False
        elif(self.start == other.start):
            return self.letter < other.letter
    def __gt__(self, other):
        if(self < other or self == other):
            return False
    def __eq__(self, other):
        return self.start == other.start and self.letter == other.letter
    def __le__(self, other):
        return self < other or self == other
    def __ge__(self, other):
        return self > other or self == other

    #Parameters
    #time:
    #
    #Return
    def is_done(self, time):
        return time == self.end

    def is_past(self, time):
        return time > self.end

    def should_start(self, time):
        return time == self.start

    #Parameters
    #time:
    #amount:
    #
    #Return
    def shift_time(self, time, amount):
        if time <= self.start:
            self.start += amount
        if time <= self.end:
            self.end += amount




def parse_process_file(file_name):
    f = open(file_name)
    processes = list()
    for line in f:
        if len(line) <= 4:
            continue
        if line[0] == "#" or line[0] == " " or line[0] == "\t":
            continue

        buff = ""
        split_spaced = list()
        for c in line:
            if c == " " or c == "\t":
                if len(buff) > 0:
                    split_spaced.append(buff)
                    buff = ""
                continue
            buff += c
        if buff != "":
            split_spaced.append(buff)
        #split_spaced = line.split(" ")
        letter = split_spaced[0]
        del(split_spaced[0])
        size = int(split_spaced[0])
        del(split_spaced[0])
        for start_end in split_spaced:
            split_slash = start_end.split("/")
            start = int(split_slash[0])
            length = int(split_slash[1])
            processes.append(Process(letter, size, start, length))
    processes.sort()
    return processes
