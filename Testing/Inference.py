pose_net = caffe.Net(model['deployFile'], model['caffemodel'], caffe.TEST)
pose_net.forward() # dry run to avoid GPU synchronization later in caffe
output_blobs_array = [dict() for dummy in range(num_people)]
for p in range(num_people):
    input_4ch = np.ones((model['boxsize'], model['boxsize'], 4))
    input_4ch[:,:,0:3] = person_image[:,:,:,p]/256.0 - 0.5 # normalize to [-0.5, 0.5]
    input_4ch[:,:,3] = gaussian_map
    pose_net.blobs['data'].data[...] = np.transpose(np.float32(input_4ch[:,:,:,np.newaxis]), (3,2,0,1))
    start_time = time.time()
    one_output_blobs = pose_net.forward()
    output_blobs_array[p] = copy.deepcopy(one_output_blobs[one_output_blobs.keys()[0]])
    print('For person %d, pose net took %.2f ms.' % (p, 1000 * (time.time() - start_time)))
