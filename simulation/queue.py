# Single Server Queue Simulation (M/M/1)

import random

def single_server_queue():

    n = int(input("Enter number of customers: "))
    mean_inter = float(input("Enter mean inter-arrival time: "))
    mean_service = float(input("Enter mean service time: "))

    arrival_time = 0
    service_end = 0
    total_wait = 0
    total_idle = 0
    total_service = 0

    print("\nCust  InterArr  Arrival  Wait  ServStart  ServTime  ServEnd  Idle")

    for i in range(1, n+1):

        inter_arrival = random.expovariate(1.0/mean_inter)
        arrival_time += inter_arrival

        service_time = random.expovariate(1.0/mean_service)
        total_service += service_time

        if arrival_time >= service_end:
            idle = arrival_time - service_end
            total_idle += idle
            service_start = arrival_time
            wait = 0
        else:
            service_start = service_end
            wait = service_start - arrival_time
            total_wait += wait
            idle = 0

        service_end = service_start + service_time

        print(i, round(inter_arrival,3), round(arrival_time,3), round(wait,3),
              round(service_start,3), round(service_time,3),
              round(service_end,3), round(idle,3))

    avg_wait = total_wait / n
    avg_service = total_service / n
    throughput = n / service_end
    utilization = ((service_end - total_idle) / service_end) * 100

    print("\nAverage Waiting Time:", round(avg_wait,4))
    print("Average Service Time:", round(avg_service,4))
    print("Total Idle Time:", round(total_idle,4))
    print("Server Utilization:", round(utilization,2), "%")
    print("Throughput:", round(throughput,4), "customers/min")


single_server_queue()