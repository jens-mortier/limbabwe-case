from libs.data_helper import *;
import numpy;


def V():
    return [1] * len(dataread("./data/matrix.txt"));

def E():
    return [1] * len(dataread("./data/matrix.txt"))**2;

def C():
    return [1] * 200;
