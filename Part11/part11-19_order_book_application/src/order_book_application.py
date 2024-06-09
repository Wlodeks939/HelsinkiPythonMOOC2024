class Task:
    total_tasks = 0
    def __init__(self,description:str,programmer: str,workload:int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        Task.total_tasks += 1
        self.id = Task.total_tasks

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        if self.finished:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"


class OrderBook:
    def __init__(self):
        self.lista = []

    def add_order(self, description, programmer, workload):
        task = Task(description,programmer,workload)    
        self.lista.append(task)

    def all_orders(self):
        return self.lista   

    def programmers(self):

        programmers = []
        for task in self.lista:
            if task.programmer not in programmers:
                programmers.append(task.programmer)
        return programmers        

    def mark_finished(self, id: int):

        found = False
        for task in self.lista:
            if task.id == id:
                task.finished = True
                found = True
        if not found:
            raise ValueError("Wrong ID")       

    def finished_orders(self):

        lista_finished = []
        for task in self.lista:
            if task.finished:
                lista_finished.append(task)

        return lista_finished        

    def unfinished_orders(self):

        lista_unfinished = []
        for task in self.lista:
            if not task.finished:
                lista_unfinished.append(task)

        return lista_unfinished    


    def status_of_programmer(self, programmer: str):

        finished_tasks = 0
        unfinished_tasks = 0
        fin_workload = 0
        unfin_workload = 0

        found = False

        for task in self.lista:
            if task.programmer == programmer:

                found = True
                if task.finished:
                    finished_tasks += 1
                    fin_workload += task.workload
                else:
                    unfinished_tasks += 1
                    unfin_workload += task.workload

        if not found:
            raise ValueError("programmer does not exists")            


        return [finished_tasks, unfinished_tasks, fin_workload, unfin_workload]
    

class App:
    def __init__(self):
        self.orderbook = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")  
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order_app()

            elif command == "2":
                self.finished_tasks()

            elif command == "3":
                self.unfinished_tasks()

            elif command == "4":
                self.mark_finished()    

            elif command == "5":
                self.programmers_app()   

            elif command == "6":
                self.status_of_programmer_app()         
         
            else:
                self.help()   
                
    def add_order_app(self):

        description = input("description: ")    
        lista = input("programmer and workload estimate: ").split()      
        programmer = lista[0]   
        workload = 0

        try:  
            if len(lista) != 2:
                print("erroneous input")  
                return 
            else:
                workload = int(lista[1])

        except ValueError:
            workload = -1    

        if workload > 0:
            self.orderbook.add_order(description, programmer,workload)
            print("added!")

        else:
            print("erroneous input")    


    def finished_tasks(self):

        if len(self.orderbook.finished_orders()) == 0:
            print("no finished tasks")
        else:
            lista = self.orderbook.finished_orders()

            for task in lista:
                print(task)
        
    def unfinished_tasks(self):

        lista = self.orderbook.unfinished_orders()

        for task in lista:
            print(task)

    def mark_finished(self):

        try:
            id = int(input("id: "))
        except ValueError:
            id = -1

        lista_id = []  

        for task in self.orderbook.lista:
            lista_id.append(task.id)   

        if id not in lista_id or id < 0:      

            print("erroneous input")   

        else:
            for task in self.orderbook.lista:
                if task.id == id:
                    task.mark_finished()

            print("marked as finished")        

    def programmers_app(self):

        lista = self.orderbook.programmers()

        for programmer in lista:
            print(programmer)

    def status_of_programmer_app(self):

        lista_programmers = self.orderbook.programmers()
        programmer = input("programmer: ") 

        if programmer not in lista_programmers:
            print("erroneous input")   

        else:    

            lista =  self.orderbook.status_of_programmer(programmer)  

            print(f"tasks: finished {lista[0]} not finished {lista[1]}, hours: done {lista[2]} scheduled {lista[3]}")  



app = App()       
app.execute()        