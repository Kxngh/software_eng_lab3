class Process:
    def __init__(self, p_id, name, start_time, prio):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.prio = prio

class Table:
    def __init__(self):
        self.process = []

    def add_process(self, process):
        self.process.append(process)

    def sort_by_pid(self):
        for i in range(len(self.process)):
            for j in range(len(self.process) - i - 1):
                if self.process[j].p_id > self.process[j + 1].p_id:
                    self.process[j], self.process[j + 1] = self.process[j + 1], self.process[j]

    def starttime_sort(self):
        for i in range(len(self.process)):
            for j in range(len(self.process) - i - 1):
                if self.process[j].start_time > self.process[j + 1].start_time:
                    self.process[j], self.process[j + 1] = self.process[j + 1], self.process[j]

    def prio_sort(self):
        priority_order = {"High": 1, "MID": 2, "Low": 3}
        for i in range(len(self.process)):
            for j in range(len(self.process) - i - 1):
                if priority_order[self.process[j].prio] > priority_order[self.process[j + 1].prio]:
                    self.process[j], self.process[j + 1] = self.process[j + 1], self.process[j]

    def display(self):
        print("{:<5} {:<10} {:<15} {}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
        print("=" * 40)
        for process in self.process:
            print("{:<5} {:<10} {:<15} {}".format(process.p_id, process.name, process.start_time, process.prio))

def main():
    table = Table()

    table.add_process(Process("P1", "VSCode", 100, "MID"))
    table.add_process(Process("P23", "Eclipse", 234, "MID"))
    table.add_process(Process("P93", "Chrome", 189, "High"))
    table.add_process(Process("P42", "JDK", 9, "High"))
    table.add_process(Process("P9", "CMD", 7, "High"))
    table.add_process(Process("P87", "NotePad", 23, "Low"))

    while True:
        print("\nSelect sorting parameter:")
        print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            table.sort_by_pid()
        elif choice == "2":
            table.starttime_sort()
        elif choice == "3":
            table.prio_sort()
        elif choice == "4":
            break
        else:
            print("Wrong Input, Please pick between (1/2/3)")

        table.display()

if __name__ == "__main__":
    main()
    