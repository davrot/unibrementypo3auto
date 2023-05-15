import numpy as np


def make_drop_map(center_x: list[int], center_y: list[int]) -> np.ndarray:
    center_x_np = np.array(center_x)
    center_y_np = np.array(center_y)

    center_x_np_unique = np.unique(center_x_np)
    center_y_np_unique = np.unique(center_y_np)

    organization_matrix = np.full(
        (center_y_np_unique.shape[0], center_x_np_unique.shape[0]), -1, dtype=np.int64
    )

    for y in range(0, organization_matrix.shape[0]):
        to_find_y = center_y_np_unique[y]
        idx_y = np.where(center_y_np == to_find_y)[0]

        to_find_x = center_x_np[idx_y]

        for x in range(0, to_find_x.shape[0]):
            idx_x = np.where(center_x_np[idx_y] == to_find_x[x])[0]
            assert idx_x.shape[0] == 1

            pos_x = np.where(center_x_np_unique == to_find_x[x])[0]
            assert pos_x.shape[0] == 1

            organization_matrix[y, pos_x] = idx_y[idx_x]

    return organization_matrix
