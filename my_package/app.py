import os
import sys
import runpy

import streamlit as st

from my_package.my_module import my_func
# from .my_module import my_func  # Won't work


def main():
    st.title('Main Page')
    st.write('Hello Main Page!')
    st.write(my_func())


def run_app():
    script_path = os.path.abspath(__file__)
    sys.argv = ['streamlit', 'run', script_path] + sys.argv[1:]
    runpy.run_module('streamlit', run_name='__main__')


if __name__ == '__main__':
    main()
