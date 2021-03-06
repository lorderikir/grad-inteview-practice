class TimSort:
    def __init__(self, array, run_size=32):
        self.array = array
        self.run_size = run_size

    def insertionSort(self, array, left_index, right_index):
        """ performs insertion sort on a given array
        :param array: the array to sort
        :param left_index: the lower bound of the array to sort
        :param right_index: the upper bound of the array to sort

        :raises:

        :rtype:
        """
        for index in range(left_index + 1, right_index):
            temp = array[index]
            upper_pointer = index - 1
            # short the section
            while array[upper_pointer] > temp and upper_pointer >= left_index:
                # swap the elements
                array[upper_pointer + 1] = array[upper_pointer]
                # decrement pointer
                upper_pointer -= 1
            array[upper_pointer + 1] = temp
        return array

    def merge(self, arr, l, m, r):
        # original array is broken in two parts
        # left and right array
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(arr[l + i])
        for i in range(0, len2):
            right.append(arr[m + 1 + i])

        i, j, k = 0, 0, l
        # after comparing, we merge those two array
        # in larger sub array
        while i < len1 and j < len2:

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # copy remaining elements of left, if any
        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1

        # copy remaining element of right, if any
        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1

    def sort(self):
        arr = self.array
        n = len(arr)
        # Sort individual subarrays of size RUN
        for i in range(0, n, self.run_size):
            self.insertionSort(arr, i, min((i+31), (n-1)))

        # start merging from size RUN (or 32). It will merge
        # to form size 64, then 128, 256 and so on ....
        size = self.run_size
        while size < n:

            # pick starting point of left sub array. We
            # are going to merge arr[left..left+size-1]
            # and arr[left+size, left+2*size-1]
            # After every merge, we increase left by 2*size
            for left in range(0, n, 2*size):

                # find ending point of left sub array
                # mid+1 is starting point of right sub array
                mid = left + size - 1
                right = min((left + 2*size - 1), (n-1))

                # merge sub array arr[left.....mid] &
                # arr[mid+1....right]
                self.merge(arr, left, mid, right)

            size = 2*size


if __name__ == "__main__":
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    timSort = TimSort(array)
    arr = timSort.sort()
    print(arr)
