#
#    File:   vicsek.jl
#    Author: Allen Sanford (ras9841@rit.edu)
#    Language:   julia 0.4.5
#    Description: 
#        Simulates a system of self-propelled particles in a 2D 
#        square domain. Each particle has a constant velocity and
#        progresses in a direction based on the average direction of
#        its neighbors. For more information, see the following paper:
#        
#        Tamas Vicsek et al., 'Novel Type of Phase Transition in a 
#        System of Self-Driven Particles', Physical Review Letters,
#        1995
#   Requirements:
#        PyPlot julia library installed

# Libraries
#using PyPlot

type SPP 
    velocity::Float64
    x_loc::Float64
    y_loc::Float64
    rad::Float64
end
function vicsek(num_particles, num_iter)
    println("Starting the Vicsek simulation with N=$num_particles")
    println("Simulation running for $num_iter iterations")
    
    #= Simulation parameters =#
    v0 = 1              # velocity for each cell
    neighborhood = 2    # neighboorhood radius
    max_length = 10     # boundary square length
    init_gap = 2        # initial min distance from boundary

    spps = []
    for num = 1:num_particles
        x0 = num
        y0 = num
        spps = [spps SPP(v0, x0, y0, neighborhood)]
    end
    
    
    
end

vicsek(10,100)
