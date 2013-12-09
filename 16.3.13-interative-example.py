
# Here are a few routines we'll write as functions
# To help make it easier to follow later

def solve_eq_for(f, var_name):
    g = solve(f, var_name, solution_dict = True);
    g = g[0][var_name];
    return g;

# Return the curl of a function f
def curl(f):
    i =  f[2].derivative(y) - f[1].derivative(z)
    j =-(f[2].derivative(x) - f[0].derivative(z))
    k =  f[1].derivative(x) - f[0].derivative(y)
    return vector( [i, j, k] )

# I'm going to use these as variables
# Sage needs to be at least declare them first
x, y, z = var('x,y,z')


print '1. Define the Vector Field and Surface from the Problem'
F = vector( [x^2*z, x*y^2, z^2] )
S1 = x + y + z == 1
S2 = x^2 + y^2 == 9
r = vector( [x, y, solve_eq_for(S1, z)] )

print '2. Describe the Surface with a Position Vector'j
show("F=" + latex(F) + ", r(x,y)=" + latex(r), ", y>=0");

print '3. Plug position vector into vector field'
F_of_r = F.subs({x:r[0], y:r[1], z: r[2]});
show("F(r)=" + latex(F_of_r));

print '4. Get curl of F'
curled_F = curl(F_of_r)

print '5. Get Normal vector from Crossed partials of position'
r_x = derivative(r, x)
r_y = derivative(r, y)
r_prime = r_x.cross_product(r_y);
show('r_x=' + latex(r_x) + ',r_y=' + latex(r_y) + ',(r_x X r_y) =' + latex(r_prime))

print '6. Bring this together for the inner'
fun = curled_F.dot_product(r_prime)
show("curl F(r) \cdot  (r_x  X r_y) =" + latex(curled_F) + "\cdot" + latex(r_prime) + " = " + latex(fun))


show('\iint\limits_D ' + latex(fun) + 'dA');
show('\int_0^{2p} \! \int_0^1 \! ' + latex(fun) + 'r dr dt');


rad, t = var('rad, t')

fun = fun.subs({x: rad * cos(t), y: rad * sin(t)})
fun = fun * rad

answer = fun.integrate(rad, 0, 3).integrate(t, 0, 2*pi)

show('(a)' + latex(answer))



# Define our interactive
# We'll provide 4 parameters from the user to control
@interact
def _(
    A = slider(-10, 10, 1/2, default = 1),
    B = slider(-10, 10, 1/2, default = 1),
    C = slider(-10, 10, 1/2, default = 1),
    r = slider(1, 10, 1/2, default = 3)
    ):

    K = max(A,B,C)

    plane = A * x + B * y + C * z == K
    cyl = x^2 + y^2 == r^2

    t = var('t')
    ellipse = vector( [ r*cos(t), r*sin(t), (K/C) - (A/C)*r*cos(t) - (B/C)*r*sin(t) ] )

    max_x = max(A, B, C, r, abs((K-A)/C), abs((K-B)/C) )
    max_y = max_x
    max_z = max_x

    show(latex(ellipse))

    plane = implicit_plot3d(plane,
                        (x,-max_x,max_x),
                        (y,-max_y,max_y),
                        (z,-max_z,max_z),
                        plot_points = 75,
                        color='#00eeff')
    cyl = implicit_plot3d(cyl,
                        (x,-max_x,max_x),
                        (y,-max_y,max_y),
                        (z,-max_z,max_z),
                        plot_points = 75,
                        color='#0000dd')

    ellipse = parametric_plot3d(ellipse,
                                (t,0,2*pi),
                                color='#ff0000')
    picture = plane + cyl + ellipse
    show(picture)

