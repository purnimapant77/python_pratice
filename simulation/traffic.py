# Traffic Light Simulation

def traffic_light_simulation():

    green_duration  = int(input("Enter GREEN light duration: "))
    yellow_duration = int(input("Enter YELLOW light duration: "))
    red_duration    = int(input("Enter RED light duration : "))
    num_cycles      = int(input("Enter number of cycles: "))

    total_cycle_time = green_duration + yellow_duration + red_duration
    total_sim_time   = total_cycle_time * num_cycles

    print("\nCycle Duration:", total_cycle_time, "seconds")
    print("Total Simulation Time:", total_sim_time, "seconds (", round(total_sim_time/60,2), "minutes )\n")

    current_time = 0

    for cycle in range(1, num_cycles+1):
        # GREEN
        start = current_time
        end = start + green_duration
        print("Cycle", cycle, "GREEN", start, "-", end, "sec -> Vehicles GO!")
        current_time = end

        # YELLOW
        start = current_time
        end = start + yellow_duration
        print("Cycle", cycle, "YELLOW", start, "-", end, "sec -> Slow Down!")
        current_time = end

        # RED3
        start = current_time
        end = start + red_duration
        print("Cycle", cycle, "RED", start, "-", end, "sec -> STOP!")
        current_time = end

    print("\nSimulation Summary:")
    print("Total Cycles     :", num_cycles)
    print("Time in GREEN    :", green_duration * num_cycles, "sec (", round(green_duration * num_cycles / total_sim_time*100,1), "% )")
    print("Time in YELLOW   :", yellow_duration * num_cycles, "sec (", round(yellow_duration * num_cycles / total_sim_time*100,1), "% )")
    print("Time in RED      :", red_duration * num_cycles, "sec (", round(red_duration * num_cycles / total_sim_time*100,1), "% )")
    print("Total Sim Time   :", total_sim_time, "sec")

traffic_light_simulation()