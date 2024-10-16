import pandas as pd
import mutli_threads

NUMBER_OF_THREAD = int(input("Enter number of threads: "))
USERNAME_FILE = "usernames.txt"
PROXY_FILE = "proxylist.txt"

username_list = []
with open(USERNAME_FILE, "r", encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        username_list.append(line.strip())

proxy_list = []
with open(PROXY_FILE, "r", encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        proxy_list.append(line.strip())

# Determine the number of rows per thread
num_rows = len(username_list)
rows_per_thread = num_rows // NUMBER_OF_THREAD

# Creating and starting threads
# threads_smart = []
username_list_array = []   
for i in range(NUMBER_OF_THREAD):
    start_index = i * rows_per_thread
    end_index = start_index + rows_per_thread
    if i == NUMBER_OF_THREAD - 1:
        end_index = num_rows  # Ensure the last thread covers the remainder

    # threads_smart.concurrent_run_bots()
    username_list_array.append(username_list[start_index:end_index])

num_rows = len(proxy_list)
rows_per_thread = num_rows // NUMBER_OF_THREAD

proxy_list_array = []   
for i in range(NUMBER_OF_THREAD):
    start_index = i * rows_per_thread
    end_index = start_index + rows_per_thread
    if i == NUMBER_OF_THREAD - 1:
        end_index = num_rows  # Ensure the last thread covers the remainder

    # threads_smart.concurrent_run_bots()
    proxy_list_array.append(proxy_list[start_index:end_index])

mutli_threads.concurrent_run(NUMBER_OF_THREAD, username_list_array, proxy_list_array)
