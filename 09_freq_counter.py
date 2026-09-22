inp_string = input("Enter the string: ")

freq_counter = {}

for chr in inp_string.lower():
    freq_counter[chr] = freq_counter.get(chr,0) +1


print(freq_counter)