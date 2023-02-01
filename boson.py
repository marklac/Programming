class bosonic_operator:
    def creation(q,p):
        c=q
        d=p
        a = 1/2**(1/2)*complex(c,d)    
        return a
    def annihilation(q,p):
        c=q
        d=-p
        ad = 1/2**(1/2)*complex(c,d)
        return ad