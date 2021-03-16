#!/usr/bin/env python

# Copyright (C) 2021 Bibliotheca Alexandrina <http://www.bibalex.org/>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# This program generates a random dataset and calculates the average.


from mpi4py import MPI
import numpy as np
import scipy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
N = 10**6

if rank == 0:
    data = np.random.normal(size=N*nprocs)

    for i in range (1, nprocs):
        comm.Send(data[i*N:(i+1)*N], dest=i)

    slice_avgs = np.empty(nprocs)

    for i in range (1, nprocs):
        slice_avgs[i] = comm.recv(source=i)

        print("Received slice average from source: {}".format(i))

    print('average =', scipy.mean(slice_avgs))
else:
    my_data = np.empty(N)
    comm.Recv(my_data, source=0)
    comm.send(scipy.mean(my_data), dest=0)
