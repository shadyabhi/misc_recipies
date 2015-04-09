from multiprocessing import Pool
 
# parallelize function
def product(a,b):
    print a*b
 
# auxiliary funciton to make it work
def product_helper(args):
    return product(*args)
 
p = Pool(5)

p.map(product_helper, [(5,5),(1,1),(2,2)])
