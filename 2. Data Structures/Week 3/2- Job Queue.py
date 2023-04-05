# python3

from collections import namedtuple
import heapq


AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    worker_heap = [(0, i) for i in range(n_workers)]
    heapq.heapify(worker_heap)
    for job in jobs:
        start_time, worker_id = heapq.heappop(worker_heap)
        result.append(AssignedJob(worker_id, start_time))
        start_time += job
        heapq.heappush(worker_heap, (start_time, worker_id))
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
