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


        return finished_tasks, unfinished_tasks, fin_workload, unfin_workload

