import secrets
import numpy as np

### Client-side functions ###
def createXorMasks(num_servers, database_len, data_index):

    mask_len_bytes = database_len // 8
    remainder_bits = database_len % 8

    if remainder_bits > 0:
        mask_len_bytes += 1
        last_bits = 128
        for i in range(remainder_bits-1):
            last_bits = last_bits >> 1
            last_bits += 128


    rand_masks = []
    cumulative_xor = np.zeros((mask_len_bytes,), dtype='uint8')

    # Create random bit masks
    for i in range(num_servers-1):
        mask = np.zeros((mask_len_bytes,), dtype='uint8')

        for j in range(mask_len_bytes-1):
            mask[j] = secrets.randbits(8)
            cumulative_xor[j] ^= mask[j]

        mask[mask_len_bytes-1] = secrets.randbits(8)
        mask[mask_len_bytes-1] &= last_bits
        cumulative_xor[j] ^= mask[mask_len_bytes-1]

        rand_masks.append(mask)

    # Debug
    # i = 0
    # for mask in rand_masks:
    #     print("Mask", i, ":")
    #     for j in range(mask_len_bytes):
    #         print("  byte", j, ":", "{:08b}".format(mask[j]))
    #     i += 1

    # Create index array i.e. the request
    index_array = np.zeros((mask_len_bytes,), dtype='uint8')
    byte_index  = data_index // 8
    bit_index   = 7 - (data_index % 8)
    index_array[byte_index] = 2**bit_index

    # Debug
    # print("Index array:")
    # for j in range(mask_len_bytes):
    #     print("  byte", j, ":", "{:08b}".format(index_array[j]))

    #Create last mask
    last_mask = np.zeros((mask_len_bytes,), dtype='uint8')
    for j in range(mask_len_bytes):
        last_mask[j] = (index_array[j] ^ cumulative_xor[j])

    # Debug
    # print("Last mask:")
    # for j in range(mask_len_bytes):
    #     print("  byte", j, ":", "{:08b}".format(last_mask[j]))

    # Debug
    # verify = np.zeros((mask_len_bytes,), dtype='uint8')
    # for j in range(mask_len_bytes):
    #     verify[j] = (last_mask[j] ^ cumulative_xor[j])

    # Debug
    # print("Verification:")
    # for j in range(mask_len_bytes):
    #     print("  byte", j, ":", "{:08b}".format(verify[j]))

    return rand_masks, last_mask

# masks, last_mask = createXorMasks(3, 10, 2)
# print(masks)
# print(last_mask)
