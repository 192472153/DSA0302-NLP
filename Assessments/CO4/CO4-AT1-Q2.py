# Smart Manufacturing using Predicate Logic

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

print("Machine Production Status:\n")

for machine, status in machines.items():
    
    if status == "Active":
        print(machine, "is Active")
        print(machine, "is Producing")
    
    else:
        print(machine, "is under Maintenance")
        print(machine, "is Not Producing")
    
    print()
