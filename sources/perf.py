#Performance and logging functionalities
#Contains  functions to measure correlation and predictions //
#Dynamic time warping with the data predicted data
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

def inf_perf(model,X_test,Y_test, hist):
    pred = model.evaluate(X_test,Y_test)

def dtw_fast(X,Y):
    #Measures the dynamic time warping between two sequences
    #X,Y are np.arrays
    distance, path = fastdtw(X, Y, dist=euclidean)
    print(distance)
    return distance, path