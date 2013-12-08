# Technically, this is SageWS a variant of py

# Declaring our common variables
x, y, z = var('x,y,z')
a, b, c = var('a,b,c')

# Define some quadtraick equations we'd like observe
quadrics = {
            'Ellipsoid':a*x^2+b*y^2+c*z^2-1,
            'Elliptic paraboloid':a*x^2+b*y^2-c*z,
            'Hyperbolic paraboloid':a*x^2-b*y^2-c*z,
            '1-Sheeted Hyperboloid':a*x^2+b*y^2-c*z^2-1,
            '2-Sheeted Hyperboloid':a*x^2-b*y^2-c*z^2-1,
            'Cone':a*x^2+b*y^2-c*z^2
            }

# Define our interactive
# We'll provide 4 parameters from the user to control
@interact
def quadratic_examples(
                       quadratic = selector(quadrics.keys()),
                       A = slider(0, 10, 1/2, default = 1),
                       B = slider(0, 10, 1/2, default = 1),
                       C = slider(0, 10, 1/2, default = 1)
                       ):
    # Pick out the equeation to use for F
    f = quadrics[quadratic];
    # Fill in our variables
    f = f.subs({ a:A, b:B, c:C })
    # Draw our example
    html('<center>$'+latex(f)+'$ </center>')
    p = implicit_plot3d(f,
                        (x,-2,2),
                        (y,-2,2),
                        (z,-2,2),
                        plot_points = 75)
    show(p)


</script></div>
