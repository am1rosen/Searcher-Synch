import math
import threading
import time

st = time.time()
lines = open("text.txt", "r").read().splitlines()
words = open("words.txt", "r").read().splitlines()
output = open("output.txt", "w")
number_of_lines = len(lines)
number_of_threads = 4
index = math.floor(number_of_lines / number_of_threads)
found_words = {}

mutex_lock = threading.Lock()
semaphore = threading.BoundedSemaphore(value=1)


def search(number):
    line_number = number * index
    if number != number_of_threads - 1:
        for line in lines[number * index:(number + 1) * index]:
            for word in words:
                if word in line:
                    et = time.time()
                    if word not in found_words.keys():
                        found_words[word] = [line_number, len(found_words) + 1]
                        semaphore.acquire()
                        output.write('word "' + word + '" found. ' + "line number: " + str(line_number + 1) +
                                     ". thread number: " + str(number + 1) + ". found in: " + str(et - st) +
                                     " seconds. " + "written to output file in: " + str(time.time() - st) +
                                     " seconds" + "\n")
                        semaphore.release()
                    else:
                        if line_number < found_words[word][0]:
                            semaphore.acquire()
                            with open("output.txt", "r") as file:
                                data = file.readlines()
                            data[found_words[word][1]] = 'word "' + word + '" found. ' + "line number: " + str(line_number + 1) + ". thread number: " + str(number + 1) + ". found in: " + str(et - st) + " seconds. " + "written to output file in: " + str(time.time() - st) + " seconds" + "\n"
                            with open("output.txt", "w") as file:
                                file.writelines(data)
                            found_words[word] = [line_number, len(found_words) + 1]
                            semaphore.release()
            line_number += 1
    else:
        for line in lines[number * index:]:
            for word in words:
                if word in line:
                    et = time.time()
                    if word not in found_words.keys():
                        found_words[word] = [line_number, len(found_words) + 1]
                        semaphore.acquire()
                        output.write('word "' + word + '" found. ' + "line number: " + str(line_number + 1) +
                                     ". thread number: " + str(number + 1) + ". found in: " + str(et - st) +
                                     " seconds. " + "written to output file in: " + str(time.time() - st) +
                                     " seconds" + "\n")
                        semaphore.release()
                    else:
                        if line_number < found_words[word][0]:
                            semaphore.acquire()
                            with open("output.txt", "r") as file:
                                data = file.readlines()
                            data[found_words[word][1]] = 'word "' + word + '" found. ' + "line number: " + str(
                                line_number + 1) + ". thread number: " + str(number + 1) + ". found in: " + str(
                                et - st) + " seconds. " + "written to output file in: " + str(
                                time.time() - st) + " seconds" + "\n"
                            with open("output.txt", "w") as file:
                                file.writelines(data)
                            found_words[word] = [line_number, len(found_words) + 1]
                            semaphore.release()
            line_number += 1


# def search(number):
#     line_number = number * index
#     if number != number_of_threads - 1:
#         for line in lines[number * index:(number + 1) * index]:
#             for word in words:
#                 if word in line:
#                     et = time.time()
#                     if word not in found_words.keys():
#                         found_words[word] = [line_number, len(found_words) + 1]
#                         mutex_lock.acquire()
#                         output.write('word "' + word + '" found. ' + "line number: " + str(line_number + 1) +
#                                      ". thread number: " + str(number + 1) + ". found in: " + str(et - st) +
#                                      " seconds. " + "written to output file in: " + str(time.time() - st) +
#                                      " seconds" + "\n")
#                         mutex_lock.release()
#                     else:
#                         if line_number < found_words[word][0]:
#                             mutex_lock.acquire()
#                             with open("output.txt", "r") as file:
#                                 data = file.readlines()
#                             data[found_words[word][1]] = 'word "' + word + '" found. ' + "line number: " + str(line_number + 1) + ". thread number: " + str(number + 1) + ". found in: " + str(et - st) + " seconds. " + "written to output file in: " + str(time.time() - st) + " seconds" + "\n"
#                             with open("output.txt", "w") as file:
#                                 file.writelines(data)
#                             found_words[word] = [line_number, len(found_words) + 1]
#                             mutex_lock.release()
#             line_number += 1
#     else:
#         for line in lines[number * index:]:
#             for word in words:
#                 if word in line:
#                     et = time.time()
#                     if word not in found_words.keys():
#                         found_words[word] = [line_number, len(found_words) + 1]
#                         mutex_lock.acquire()
#                         output.write('word "' + word + '" found. ' + "line number: " + str(line_number + 1) +
#                                      ". thread number: " + str(number + 1) + ". found in: " + str(et - st) +
#                                      " seconds. " + "written to output file in: " + str(time.time() - st) +
#                                      " seconds" + "\n")
#                         mutex_lock.release()
#                     else:
#                         if line_number < found_words[word][0]:
#                             mutex_lock.acquire()
#                             with open("output.txt", "r") as file:
#                                 data = file.readlines()
#                             data[found_words[word][1]] = 'word "' + word + '" found. ' + "line number: " + str(
#                                 line_number + 1) + ". thread number: " + str(number + 1) + ". found in: " + str(
#                                 et - st) + " seconds. " + "written to output file in: " + str(
#                                 time.time() - st) + " seconds" + "\n"
#                             with open("output.txt", "w") as file:
#                                 file.writelines(data)
#                             found_words[word] = [line_number, len(found_words) + 1]
#                             mutex_lock.release()
#             line_number += 1


for thread_number in range(number_of_threads):
    t = threading.Thread(target=search, args=(thread_number,))
    t.start()
