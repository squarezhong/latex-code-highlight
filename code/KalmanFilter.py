from numpy import *

class KalmanFilter(object):

    def __init__(self):
        print('successfully called')

    def predict(self, x0, P0, u0, A, B, Q):
        x_predict = dot(A, x0) + dot(B, u0) 
        P_predict = dot(A, dot(P0, A.T)) + Q 
        return(x_predict,P_predict)

    def kf_update(self, x_predict, P_predict, z, H, R):
        K = dot(P_predict, dot(H.T, linalg.inv(dot(H, dot(P_predict, H.T)) + R ))) 
        x = x_predict + dot(K, (z - dot(H, x_predict))) 
        P = P_predict - dot(K, dot(H, P_predict)) 
        return (x, P)

    # 1 dimension case
    def simple_predict(self, x0, P0, u0, A, B, Q):
        x_predict = dot(A, x0) + dot(B, u0) 
        P_predict = dot(A, dot(P0, A)) + Q 
        return(x_predict,P_predict)

    # 1 dimension case
    def simple_update(self, x_predict, P_predict, z, H, R):
        K = dot(P_predict, dot(H, 1 / (dot(H, dot(P_predict, H)) + R ))) 
        x = x_predict + dot(K, (z - dot(H, x_predict))) 
        P = P_predict - dot(K, dot(H, P_predict)) 
        return (x, P)