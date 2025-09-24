# for loops = execute a block of code a fixed number of time
# iterate over a range, string, sequence, etc.

# # iterate a range
# for x in range(1,11):
#     print(x)

# # iterate backwards
# for x in reversed(range(1,11)):
#     print(x)

# #iterate with step 2
# for x in range(1,11,2):
#     print(x)

# use continue to skip an execution
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)


