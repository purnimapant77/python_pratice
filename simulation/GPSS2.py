# GPSS Simulation: Barber Shop (Student Version)

import random

def barber_shop_simulation():

    # Shop time: 9 AM to 4 AM next day = 1140 minutes
    shop_close = 1140

    barber_free_at   = 0
    current_time     = 0
    customer_count   = 0
    total_wait       = 0
    total_service    = 0
    customers_waited = 0
    barber_idle_time = 0

    def to_clock(sim_min):
        total_mins = 9*60 + sim_min
        hour = (total_mins // 60) % 24
        minute = total_mins % 60
        period = "AM" if hour < 12 else "PM"
        display_hour = hour if hour <= 12 else hour - 12
        if display_hour == 0:
            display_hour = 12
        return f"{display_hour:02d}:{minute:02d} {period}"

    print("Shop Hours:", to_clock(0), "to", to_clock(shop_close))
    print("No.  Arrive(min)  Arrive(time)  Wait  Chair at  Haircut  Done at  Status")

    while True:
        # Next customer arrives 10 +- 2 minutes
        inter_arrival = random.randint(8, 12)
        current_time += inter_arrival
        if current_time > shop_close:
            break

        customer_count += 1

        # Haircut time 13 +- 2 minutes
        haircut_time = random.randint(11, 15)
        total_service += haircut_time

        # Check barber availability
        if current_time >= barber_free_at:
            idle = current_time - barber_free_at
            barber_idle_time += idle
            wait = 0
            chair_time = current_time
        else:
            wait = barber_free_at - current_time
            total_wait += wait
            customers_waited += 1
            chair_time = barber_free_at

        done_time = chair_time + haircut_time
        barber_free_at = done_time

        status = "Waited" if wait > 0 else "No wait"

       # print(customer_count, current_time, to_clock(current_time), wait, to_clock(chair_time), haircut_time, "min", to_clock(done_time), status)

    # Summary
    print("\nSimulation Summary:")
    print("Total Customers       :", customer_count)
    print("Customers Who Waited  :", customers_waited)
    print("Customers Served Immediately:", customer_count - customers_waited)
    if customer_count > 0:
        print("Average Wait Time     :", round(total_wait/customer_count, 2), "min")
    if customers_waited > 0:
        print("Avg Wait (who waited) :", round(total_wait/customers_waited, 2), "min")
    print("Average Haircut Time  :", round(total_service/customer_count, 2), "min")
    print("Barber Idle Time      :", round(barber_idle_time, 2), "min")
    utilization = (1 - barber_idle_time / shop_close) * 100
    print("Barber Utilization    :", round(utilization, 1), "%")
    print("Barber Finished Work  :", to_clock(barber_free_at))

barber_shop_simulation()