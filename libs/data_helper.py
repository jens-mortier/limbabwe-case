import numpy;

map = [];
indices = [];

def dataread( filename ):
    try:
        current_matrix = map[indices.index(filename)];
    except ValueError:
        map.append(numpy.loadtxt('./' + filename, delimiter=' '));
        indices.append(filename);
        current_matrix = dataread(filename);

    return current_matrix;