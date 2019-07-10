W, H = 1000, 1000
newPage(W,H)

start = (0, 0.25, 1, 0.1)
end = (0, 0.4, 0.5, 0.75)
iterations = 20

def interp(a,b,f):
    return a+f*(b-a)

transform

for step in range(0,iterations): 

    f = step / iterations
    
    print(f)
    fill(interp(start[0],end[0],f), interp(start[1],end[1],f), interp(start[2],end[2],f), interp(start[3],end[3],f))
   

    rect(0,H/iterations*(iterations-step-1),W, H/iterations)

