def gr(arr):
    n = len(arr)
    nge = [-1] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and st[-1] <= arr[i]:
            st.pop()
        if st:
            nge[i] = st[-1]
        st.append(arr[i])
    return nge
input_list = [14, 2, 16, 4, 3, 5]
n_g = gr(input_list)
print(n_g)

