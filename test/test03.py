import json

addr01 = "/workspace/dialogSystem/GraftNet/datasets/wikimovie/10k_train_kb_05/test.json"
addr02 = "/workspace/dialogSystem/GraftNet/datasets/wikimovie/10k_train_kb_01/test.json"
tweets = []
for line in open(addr01, 'r'):
    tweets.append(json.loads(line))

print (tweets[0])

tweets = []
for line in open(addr02, 'r'):
    tweets.append(json.loads(line))

print (tweets[0])

"""
/workspace/dialogSystem/GraftNet/datasets/wikimovie/10k_train/dev.json
train 10000
dev 10000
test 9952
"""