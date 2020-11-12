# Bloom Filter
2 versions Bloom filter based on https://en.wikipedia.org/wiki/Bloom_filter 


## Installation
```shell
git clone https://github.com/torxx666/bloom.git
cd bloom
python -m venv venv
source ./venv/bin/activate

```

## Run
You have 2 versions : 
- python check_version_1.py
- python check_version_2.py

if you want to change the file against the script is tested, replace `emerson_essays.txt` by `sample-2mb-text.txt`


see line 6 :
```python
f = open("emerson_essays.txt", "r")
```

## Testing


```
pip install pytest
```
You have 2 tests for the 2 algorithms versions : 
- python test_version_1.py
- python test_version_2.py