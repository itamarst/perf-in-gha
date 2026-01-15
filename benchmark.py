from py_perf_event import measure, Hardware

def normalize():
    def f():
        l = []
        l.append(1)
        l.extend([3, 4])

    def g(i):
        x = {"x": f(), i: i}
        f()
        x["y"] = 500
        return x

    for i in range(1000):
        g(i)


def wordcount(txt):
    result = {}
    for word in txt.split():
        word = word.lower()
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

def wordcount2(txt):
    result = {}
    for word in txt.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    final_result = {}
    for word, count in result.items():
        word = word.lower()
        if word in final_result:
            final_result[word] += count
        else:
            final_result[word] = count
    return final_result

text = open("emma.txt").read()
baseline = measure([Hardware.INSTRUCTIONS], normalize)[0]
cpu_instructions = measure([Hardware.INSTRUCTIONS], wordcount, text)[0]
print(cpu_instructions)
print(cpu_instructions / baseline)
cpu_instructions = measure([Hardware.INSTRUCTIONS], wordcount2, text)[0]
print(cpu_instructions)
print(cpu_instructions / baseline)
