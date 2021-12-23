import os, json

files_size = {}

for root, dirs, files in os.walk('my_project'):
    for file in files:
        key_dict = os.stat(os.path.join(root, file)).st_size // 10 *10 +10
        f_ext = file.rsplit('.')[-1]
        if key_dict in files_size:
            files_size[key_dict][1].append(f_ext)
            files_size[key_dict] = (files_size[key_dict][0] + 1, list(set(files_size[key_dict][1])))
        else:
            files_size.setdefault(key_dict, (1, [f_ext]))

res_d = {k: files_size[k] for k in sorted(files_size.keys())}
with open('result.json', 'w') as f:
    json.dump(res_d, f)
with open('result.json', 'r') as f:
    print(json.load(f))


