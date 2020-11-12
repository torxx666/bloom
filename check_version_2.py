import datetime
from  bloom2 import Bloom2


# f = open("sample-2mb-text.txt", "r") #sample-2mb-text.txt
f = open("data/emerson_essays.txt", "r")
sample = f.read()


lines = sample.splitlines()
mb = Bloom2()
false_positive = 0
new_key = 0

start_time = datetime.datetime.now()


for line  in lines:
    # print("======")
    if not mb.Add(line):
        false_positive += 1
    else: 
        new_key += 1

# print(mb.bloom_hash)
end_time = datetime.datetime.now()
print(" false_positive : %s - new_key: %s  on %s  " % (false_positive,new_key, len(lines)))
diff = (start_time-end_time).microseconds
ratio = diff / len(lines)
print("{} ms for ratio: {}".format(diff,ratio))
print(" {} LEN ".format(mb.Len()))