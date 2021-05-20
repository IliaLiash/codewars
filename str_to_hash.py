def str_to_hash(st):
    st = st.replace(',', '')
    return {i[:i.index('=')] : int(i[i.index('=') + 1:]) for i in st.split()}