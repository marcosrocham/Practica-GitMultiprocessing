from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value

def f(c):
    for i in range(100):
        c.value = c.value + 1
        print (f"hola soy {current_process().pid}, vuelta: {i}, contador: {c.value}")

def g():
    print ("adios")
    
if __name__ == "__main__":
    N = 8
    lp = []
    c = Value('i', 0)
    for i in range(N):
        lp.append(Process(target=f, args=(c,)))
    print (f"Valor inicial del contador {c.value}")
    
    for p in lp:
        p.start()
    for p in lp:
        p.join()

    q = Process(target=g)
    q.start()
    q.join()
    print (f"Valor final del contador {c.value}")
    print ("fin")