
di_path = 'dinosaurs'
dinosaurs = None

def get_reverse_dinosaurs():
    global di_path
    global dinosaurs   

    dinosaurs = []
    f = open(di_path, 'r')
    for line in f:
        dinosaurs.append(line.strip()[::-1])

    dinosaurs.sort()

    return dinosaurs

def get_suffix(di_list, max_length, min_length):
    min_count = 3
    suffix = {}

    for i in range(max_length, min_length, -1):
        s = ''
        count = 0
        for d in di_list:
            if s == d[:i] and not is_suffix(suffix, d[:i+1]):
                count += 1
            else:
                if count > min_count:
                    suffix[s] = count
                s = d[:i]
                count = 1
    return suffix

def is_suffix(suffix_list, suffix):
    l = len(suffix)
    for s in suffix_list.keys():
        if s[:l] == suffix:
            return True
    return False

def save_list(list, filepath):
    f = open(filepath, 'w')
    for l in list:
        if l.strip() != '':
            f.write(l + '\n')  
    f.close()

def calc_prob(di_list):

    sum_v = 0
    for v in di_list.values():
        sum_v += v

    for k in di_list.keys():
        di_list[k] = float(di_list[k]) / float(sum_v)

    return di_list


def reverse_dict(di_dict):
  new_dict = {}
  for key in di_dict.keys():
    new_key = key[::-1]
    new_dict[new_key] = di_dict[key]
  return new_dict


if __name__ == '__main__':
    dinosaurs = get_reverse_dinosaurs()
    suffix = get_suffix(dinosaurs, 8, 2)
    suffix = calc_prob(suffix)
    
    print suffix
    in_order_suffix = reverse_dict(suffix)
    f = open('suffix_dict.py', 'w+')
    f.write('dino_dict = ')
    f.write(str(in_order_suffix))
    f.close()
    

