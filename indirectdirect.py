import numpy as np
def sigmav_fit(x):
    ''' Experimental annihilation cross section, lower limit taken
    from b bbar as a function of the dark matter mass, dawarf galaxies 
    Fermi limit 2014 http://arxiv.org/pdf/1503.02641.pdf
    '''
    a = -61.0275315866
    b = 0.231740700807
    c = 0.0695392085778
    g1=np.exp(a + b*np.log(x) + c*np.log(x)**2)
    return g1  

def LUXconstraint_official(x):
    '''Evaluate LUX limits for DD [arXiv: astro-ph.CO/1310.8214 ]'''
    m = np.array([7.89119649, 10., 12., 17., 30., 200., 450., 1000., 2000., 3500., 5000.])
    A = np.array([0.00000000e+00, 8.48911168e-41, 1.95004609e-42, 3.75121862e-44, 3.28089421e-45, 5.80846495e-46, 1.39568112e-45, 3.05245738e-45, 5.63013735e-45, 1.07867168e-44, 1.93910180e-44])
    B = np.array([0.00000000e+00, -9.02408269e-01, -5.20772861e-01, -1.90971186e-01, -5.03032503e-02, 7.66657692e-03, 3.11852240e-03, 1.34049663e-03, 7.28957975e-04, 3.94487035e-04, 2.23523977e-04])
    imax=10
    for i in range(1,imax+1):
        if x>=m[i-1] and x<=m[i]:
            limit = A[i]*np.exp(B[i]*x)
        if x<m[0] or x>m[imax]:
            limit = 0.0	
            print 'ERROR: Out of range'
    return limit*1E36

def sigmaSI_f(x):
    import numpy as np
    x=np.asarray(x)
    if not x.shape: 
        x=[x] 
    
    return map(LUXconstraint_official,x)