print("UAA DEMO RUNNING")

allowed = 100

def execute(amount):
    if amount <= allowed:
        print("EXECUTE:", amount)
    else:
        print("BLOCK:", amount)

execute(50)
execute(250)
