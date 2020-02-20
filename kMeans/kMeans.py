import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm 

def normsamp(n,mu):

    sigx = 0.5
    sigy = 0.5
    rho = 0.05
    covmat = np.array([[sigx**2,rho*sigx*sigy],[rho*sigx*sigy,sigy**2]])
    data = np.random.multivariate_normal(mu,covmat,size = n) 
    return data

if __name__ == "__main__": 
    n = 100  # number of data points 
    mu1 = np.array([1.,1.])
    mu2 = np.array([1.,0.])
    mu3 = np.array([-1.,-1.])
    
    dat1=normsamp(n,mu1)
    dat2=normsamp(n,mu2)
    dat3=normsamp(n,mu3)
    
    dat = np.append(dat1,dat2,axis=0)
    dat = np.append(dat,dat3,axis=0)

    # Lloyd's methods 
    k = 3 # number of cluster 

    muinds = np.random.permutation(3*n)[0:k]
    mus = [dat[ind] for ind in muinds]
    newmus = mus
    error = 1.

    cntr = 0

    while error > 1e-6:
        cntr = cntr + 1
        print(cntr)

        grps = []
        mus = newmus

        for pt in dat: 
            dsts = [np.sqrt(np.sum((pt-mu)**2)) for mu in mus]
            grp = np.argmin(dsts)
            grps.append(grp)

        newmus = []
        for i in np.arange(k):
            newmu = np.mean(dat[np.array(grps)==i],axis=0)
            newmus.append(newmu)

        error = np.sum([np.sqrt(norm(newmus[i] - mus[i])) for i in np.arange(k)])

    newmus = np.array(newmus)

    plt.figure()
    plt.plot(dat[:,0],dat[:,1],'bx')
    plt.plot(newmus[:,0],newmus[:,1],'r*')
    plt.axis('equal')
    plt.show()

    



