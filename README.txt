'''Engpy is a free and open-source Python library for Engineering computing

    Engpy is targeted to take care of most engineering problems like caculus,
    transforms, graphs, complex algebraic expressions, Matrices manipulation,
    vector analysis, analyzing signals.

    The Engpy consist of mainly 3 Datatypes:
    1. Expr
        This is the core datatype of Engpy. Most other engpy are based on this class
        This class is responsible for any algebraic manipulations.

            1.  Simple Algebra: Addition, Subtraction, Multiplication, Division
                                Substitution of Expressions; a subject of the formula,
                                clear brackets, and fractions.
            2.  Caculus: linear and partial differentiation, integration, gradient
            3.  Trigonometry
            4.  logarithmic Expressions
            5.  Transforms: Laplace, Z-Transforms
            6.  Visualization: Graphs
            7.  Table of Values
            8.  Complex Number Manipulation
            9.  Solving Expressions
            10. Support the engpy AI Implementation for manipulating expressions

        Expr can be imported from engpy
        >>> from engpy import Expr

        See the doc file or Expr documentation to learn its usage

        To interact with Expr as Discrete objects, use the interface module.
        the interface module bridges between Expr Class and Expr datatypes.

        For example, y  = 2xcos3(2θ) - 7y^2sin(2ω) - ln(sqrt(z +3)); s = y - cos(5z)
        This can be enter directly into the Expr Class
        >>> from engpy import Expr
        >>> w = Expr('2xcos3(2theta) - 7y^2sin(2omega) - ln(sqrt(z +3)); s = y - cos(5z)')
        >>> s = w - 'cos(5z)'
        >>> w
        2xcos3(2θ) - 7y^2sin(2ω) - ln(sqrt(z + 3))
        >>> s
        2xcos3(2θ) - 7y^2sin(2ω) - ln(sqrt(z + 3)) - cos(5z)

        In Discrete form
        >>> from interface import *
        >>> o,x,t,y,z = Var('omega', 'x', 'theta','y','z')
        >>> w = 2*x*cos(2*t)**3 - 7*y**2*sin(2*o) - ln(sqrt(z + 3))
        >>> w
        2xcos3(2θ) - 7y^2sin(2ω) - ln(sqrt(z + 3))
        >>> s = w - cos(5*z)
        >>> s
        2xcos3(2θ) - 7y^2sin(2ω) - ln(sqrt(z + 3)) - cos(5z)


        Note that to cast Expr to string: use str(ExprObj) or format(ExprObj), repr(ExprObj)
        str(ExprObj) will return the ExprObj in its simplest lowest form
        format(ExprObj) will return the ExprObj in its normal form
        repr(ExprObj) will return the ExprObj in the most readable form

        it's recommended to use format or repr as they faster than str. Only use str when necessary
        
        




    2. Matrix
        This datatype handles all Matrix operations and manipulations. This datatype
        rest on Expr Class.

        1. Simple Matrix Algebra: Addition, Subtraction, Multiplication, Division
                                  Substitution of Matrices
        2. Determinant, Minors, Cofactors, Adjoin, transpose, rank
        3. Reduction: echelon, canonical, triangular decomposition

        4. Row and column Transformation operations
        5. Decomposition: Triangular, Symmetric, hermitian decomposition
        6. Matrix Geometry: eigenvalues, modal, spectral, nullspace
                           algebraic multiplicity, geometric multiplicity
                           of a Matrix
        7. Differentiation
        8. Solving and comparing Matrices

        The matrix module or Matrix Class/datatype comes in two implementations.
        as Matrix or Matrix_
        Both can be import from engpy
        >>> from engpy import Matrix
        or
        >>> from engpy import Matrix_
        
        See the Matrix_doc file or engpy Arrays documentation to learn its usage
        

    3. Vector
        This data type holds the keys to vector analysis.
        1. Simple Vector Algebra: Addition, Subtraction, Substitution, Modulus
                                  of Vectors
        2. Angles between Vectors
        3. Multiplication of Vector: Dot, and scalar product
        4. Vector Calculus: Differentiation and Integration
        5. Vector Operations: Tangents, normals, grad, directional derivatives,
                              div, curl
        6. Validating properties: solenoidal, irrotational, coplanar, orthogonality
        7. Scalar, Vector Triple product

        Vector Class can also be imported from engpy
        >>> from engpy import Vector


    Note that All these three datatypes works with python operators, +, -, /, *, ~
    e.g MatObj1 + MatObj2
'''        
        