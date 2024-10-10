from concurrent.futures import ThreadPoolExecutor


def concurrent_run(count_threads, usernam_list):

    def perform_task(usernam_list):
        print(usernam_list)

    with ThreadPoolExecutor(max_workers=count_threads) as executor:
        executor.map(perform_task, usernam_list)
