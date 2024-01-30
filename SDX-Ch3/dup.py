import sys
from hashlib import sha256

def find_groups(filenames):
    file = open("known_files.txt", "a+")
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()      
        flag = False
        for line in file.readlines():
            if str(hash_code) == line:
                flag = True
                break
        if not flag:
            groups[hash_code] = set()    
            file.write(str(hash_code) + "\n")
        groups[hash_code].add(fn)
    file.close()
    return groups
    


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))


