import secrets
import numpy as np

### Client-side functions ###
def createXorMasks(num_servers, database_len, data_index):

    rand_masks = []
    cumulative_xor = np.zeros((database_len,), dtype='bool')

    # Create random bit masks
    for i in range(num_servers-1):
        mask = np.zeros((database_len,), dtype='bool')

        for j in range(database_len):
            mask[j] = bool(secrets.randbits(1))
            cumulative_xor[j] ^= mask[j]

        rand_masks.append(mask)

    index_array = np.zeros((database_len,), dtype='bool')
    index_array[data_index] = True

    # Create last mask
    last_mask = np.zeros((database_len,), dtype='bool')
    for j in range(database_len):
        last_mask[j] = (index_array[j] ^ cumulative_xor[j])

    # verify = np.zeros((database_len,), dtype='bool')
    # for j in range(database_len):
    #     verify[j] = (last_mask[j] ^ cumulative_xor[j])
    # print("Verification: ", verify)


    return rand_masks, last_mask

# masks, last_mask = createXorMasks(3, 10, 2)
# print(masks)
# print(last_mask)

### Server-side fucntions ###
database_len = 10
word_size_bits = 8
index = 7

database = np.zeros((database_len, word_size_bits), dtype='bool')
database[0,:] = np.array([False, False, True, False, True, True, True, False])
database[1,:] = np.array([False, False, True, False, True, False, False, False])
database[2,:] = np.array([True, True, False, True, True, False, False, False])
database[3,:] = np.array([False, True, True, True, True, True, False, False])
database[4,:] = np.array([False, False, False, True, False, True, False, False])
database[5,:] = np.array([True, True, False, True, False, True, True, True])
database[6,:] = np.array([True, False, False, True, True, False, True, True])
database[7,:] = np.array([True, True, True, True, False, True, True, True])
database[8,:] = np.array([False, False, False, False, False, True, False, True])
database[9,:] = np.array([False, False, False, False, True, True, False, False])

def processDBrequest(index_array):
    # print(database)
    # print(index_array)
    response = np.matmul(index_array.astype(np.int), database.astype(np.int))
    response %= 2
    response = np.array(response, dtype='bool')
    return response


# response = processDBrequest(np.array([False, False, True, False, False, True, True, False, False, True]))
# print(response)

### Testing ###
print("Database:")
for j in range(database_len):
    print(" Index", j, ":", database[j,:].astype(np.int))

print("------------------------")

masks, last_mask = createXorMasks(num_servers=3, database_len=10, data_index=index)
print("Random masks generated:")
for mask in masks:
    print(mask.astype(np.int))

print("Last mask:")
print(last_mask.astype(np.int))


server_responses = []
data_requested = np.zeros((word_size_bits,), dtype='bool')

for rand_mask in masks:
    response = processDBrequest(rand_mask)
    server_responses.append(response)
    data_requested ^= response
    # for j in range(word_size_bits):
    #     data_requested[j] ^= response[j]

response = processDBrequest(last_mask)
server_responses.append(response)
data_requested ^= response
# for j in range(word_size_bits):
#     data_requested[j] ^= response[j]

print("Server responses:")
for response in server_responses:
    print(response.astype(np.int))

print("Data requested at index", index, "is:")
print(data_requested.astype(np.int))
