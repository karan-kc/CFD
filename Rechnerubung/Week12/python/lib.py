import numpy as np
################################################################################
################################################################################
def read_snapshot(path2file, name, index, ngrid, *args, **kwargs):
    """
    Reads binary file of 3D snapshot from Xcompact3d simulation.
    Parameters:
        - path2file:    to '../data/'
        - name:         name of snapshot: 'ux','uy','uz','pre','phi1',...
        - index:        index number of snapshot
        - ngrid:        list with gridpoints of 3D field
    """
    # check optional arguments
    if kwargs:
        ndigits = kwargs.get('ndigits', None)
    else:
        ndigits = 3
    # read grid properties
    nx = ngrid[0]; ny = ngrid[1]; nz = ngrid[2]

    # read binary
    filename =  name + ("{:0" + str(ndigits) + "}").format(index)
    filepath = path2file + filename
    print("Reading binary file: " + filepath, end=" ")
    data = np.fromfile(filepath, dtype='<f8').reshape((nx,ny,nz),order='F')
    print("done")

    return data
################################################################################
################################################################################
