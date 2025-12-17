



tasks = []
try:
    with open("tasks.txt","r") as file:
        for line in file:
            tasks.append(line.strip())
except:
    pass

while True:
    print("\n---TO DO LIST---\n")
    print("1.Add tasks")
    print("2.View tasks")
    print("3.Remove tasks")
    print("4.Exit")

    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        task= input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
          if not tasks:
              print("No tasks found.")
          else:
              for i, task in enumerate(tasks):
                  print(i+1,".",task)


    elif choice == "3":
        if not tasks:
            print("no tasks to remove.")
        else:
            num=int(input("Enter task number: "))
            if 1<=num<=len(tasks):
                removed=tasks.pop(num-1)
                print("Removed:",removed)
            else:
                print("Invalid task number.")


    elif choice == "4":
        with open("tasks.txt","w")as file:
            for task in tasks:
                file.write(task+"\n")
        print("tasks saved. bye!")
        break

    else:
        print("Invalid choice.")