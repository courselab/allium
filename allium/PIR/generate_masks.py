import secrets

### Client-side functions ###
def createXorMasks(num_servers, database_len, data_index):

    rand_masks = []
    cumulative_xor = [0 for j in range(database_len)]

    # Create random bit masks
    for i in range(num_servers-1):
        mask = []
        for j in range(database_len):
            mask.append(secrets.randbits(1))
            cumulative_xor[j] ^= mask[j]

        rand_masks.append(mask)

    index_array = [0 for j in range(database_len)]
    index_array[data_index] = 1

    # Create last mask
    last_mask = []
    for j in range(database_len):
        last_mask.append(index_array[j] ^ cumulative_xor[j])

    return rand_masks, last_mask

masks, last_mask = createXorMasks(3, 10, 2)
print(masks)
print(last_mask)
# verify = []
# for j in range(database_len):
#     verify.append(last_mask[j] ^ cumulative_xor[j])
#
# print("Verification: ", verify)

### Server-side functions ###
#def processRequest(data_index):
