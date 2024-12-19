import streamlit as st

from my_package.my_module import my_func


def main():
    st.title('Page 1')
    st.write('Hello Page 1!')
    st.write(my_func())


if __name__ == '__main__':
    main()
