import numpy as np
from numpyctypes import c_ndarray
import runner_p

r = runner_p.Runner()

array = np.zeros((3,4,2), dtype=np.int64)

r.getPrint()

r.setOutput(c_ndarray(array, dtype=array.dtype, ndim = 3, shape = array.shape))
