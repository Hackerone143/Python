# First Come First Serve Scheduling
print("FIRST COME FIRST SERVE SCHEDULING")
n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    arrival_time = int(input(f"Enter arrival time of process P{i+1}: "))
    burst_time = int(input(f"Enter burst time of process P{i+1}: "))
    processes.append((f"P{i+1}", arrival_time, burst_time))

# Sort processes by arrival time
processes.sort(key=lambda x: x[1])

# Calculate Exit Time, Turnaround Time, and Waiting Time
exit_time = 0
results = []

for process in processes:
    name, arrival, burst = process
    exit_time += burst
    turnaround_time = exit_time - arrival
    waiting_time = turnaround_time - burst
    results.append((name, arrival, burst, exit_time, turnaround_time, waiting_time))

# Calculate average waiting time
avg_waiting_time = sum(result[5] for result in results) / n

# Print the results
print("\nProcess | Arrival | Burst | Exit | Turnaround | Wait |")
for result in results:
    print(f" {result[0]} | {result[1]} | {result[2]} | {result[3]} | {result[4]} | {result[5]} |")

print(f"Average Waiting Time: {avg_waiting_time:.2f}")
