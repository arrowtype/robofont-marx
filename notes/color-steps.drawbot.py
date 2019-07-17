W, H = 1000, 1000
newPage(W,H)
iterations = 30

start = (0.25, 1, 1, 0.125)
end = (0, 0, 0.25, 1)

# factor = 0.15

def interp(a,b,f):
    return a+f*(b-a)


for step in range(0,iterations): 
    f = step / iterations
    
    fill(interp(start[0],end[0],f), interp(start[1],end[1],f), interp(start[2],end[2],f), interp(start[3],end[3],f))

    rect(W/iterations*step,0,W/iterations, H)
