import numpy as np 
import time
import h5py





############## Import Channel Matrix ##################
# H_file = h5py.File('../1_out_3_all.hdf5','r')
# H_r = np.array(H_file.get('H_r'))
# H_i = np.array(H_file.get('H_i'))
# # H_i = np.transpose(H_i,(2,1,0))
# # H_r = np.transpose(H_r,(2,1,0))
# # print("H_r shape is:", H_r.shape)
# # print("H_i shape is:", H_i.shape)
# H = np.array(H_r + 1j*H_i)
# # print("H shape is:", H.shape)

# H = np.squeeze(H[6,:,:])

def usr_group(H):
    
    N_UE = 16
    ur_group = [[] for i in range(N_UE)]
    group_idx = np.zeros(N_UE)


    # print('Begining grouping:', ur_group)
    ur_group[0].append(0)
    N_group = 1
    # print('Begining grouping:', ur_group)
    corr_h = 0.5
    meet_all = 0
    assigned = 0

    for i in range (1,N_UE):
    # print('UE and assigned:',i,assigned)
        for j in range (N_group):
            for k in ur_group[j]:
                g_i = np.matrix(np.reshape(H[:,i],(64,1))).getH()
                # print('g_i size:', g_i.shape)
                corr = abs(np.dot(g_i,np.reshape(H[:,k],(64,1))))/(np.linalg.norm(np.reshape(H[:,i],(64,1)))*np.linalg.norm(np.reshape(H[:,k],(64,1))))
                # print('corr is:', corr)
                if corr > corr_h:
                    # print('new group')
                    break
                else:
                    if k == ur_group[j][-1]:
                        meet_all = 1
            if meet_all == 1:
                ur_group[j].append(i)
                meet_all = 0
                assigned = 1
                # print('UE grouping (old):', ur_group)
                break
        if assigned == 0:
            ur_group[N_group].append(i)
            N_group += 1
            # print('UE grouping (new):', ur_group)
        else:
            assigned = 0

    print('UE grouping and N_group:', ur_group, N_group)

    for i in range (N_group):
        for j in ur_group[i]:
            group_idx[j] = i
    

    return group_idx
    


