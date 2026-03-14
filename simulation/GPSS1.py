# GPSS Simulation: Manufacturing Shop (Student Version)

import random

def manufacturing_shop_simulation():

    num_parts = int(input("Enter number of parts to simulate: "))

    clock = 0
    inspector_busy_until = 0
    total_wait_time = 0
    parts_rejected = 0
    parts_accepted = 0
    parts_waited = 0

    print("\nPart  Arrive  InspFree  Wait  InspStart  InspTime  InspEnd  Result")

    for part_no in range(1, num_parts + 1):
        # Parts arrive every 5 minutes
        arrive_time = part_no * 5
        inspector_free_at = inspector_busy_until

        # Wait time calculation
        if arrive_time >= inspector_free_at:
            wait = 0
            insp_start = arrive_time
        else:
            wait = inspector_free_at - arrive_time
            insp_start = inspector_free_at
            total_wait_time += wait
            parts_waited += 1

        # Inspection time: uniform 1-7 minutes (4 ± 3)
        insp_time = random.randint(1, 7)
        insp_end = insp_start + insp_time
        inspector_busy_until = insp_end

        # Determine if part is rejected (10% chance)
        if random.random() < 0.10:
            result = "REJECTED"
            parts_rejected += 1
        else:
            result = "Accepted"
            parts_accepted += 1

        print(f"{part_no:<5} {arrive_time:<7} {inspector_free_at:<9} {wait:<5} {insp_start:<9} {insp_time:<8} {insp_end:<8} {result}")

    total_time = num_parts * 5
    rejection_rate = (parts_rejected / num_parts) * 100

    # Simulation summary
    print("\nSimulation Summary:")
    print("Total Parts Produced  :", num_parts)
    print("Parts Accepted        :", parts_accepted)
    print("Parts Rejected        :", parts_rejected, f"({rejection_rate:.1f}%)")
    print("Parts that Waited     :", parts_waited)
    if parts_waited > 0:
        print("Avg Wait (those who waited):", round(total_wait_time/parts_waited, 2), "min")
    print("Overall Avg Wait Time :", round(total_wait_time/num_parts, 2), "min")
    print("Total Production Time :", total_time, "minutes")
    print("Inspector finished at :", inspector_busy_until, "minutes")

manufacturing_shop_simulation()