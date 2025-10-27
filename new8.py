import streamlit as st
import sys
from io import StringIO
import importlib.util

st.title("实训作业展示")
tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["数字档案", "南宁美食数据", "个人简历生成器","音乐播放器","视频播放器","简易相册"])

with tab1:
    st.header("数字档案")
    code_file="first.py"
    try:
        with open(code_file,'r',encoding="utf-8")as f:
            code_content = f.read()
    except FileNotFoundError:
        st.error(f"未找到代码文件：{code_file}")
        st.stop()
    old_stdout=sys.stdout
    captured_output=StringIO()
    sys.stdout=captured_output
    try:
        spec=importlib.util.spec_from_loader("temp_module",loader=None)
        temp_module=importlib.util.module_from_spec(spec)
        exec(code_content,temp_module.__dict__)
    except Exception as e:
        st.error(f"代码运行失败：{str(e)}")
    finally:
        sys.stdout=old_stdout

    output=captured_output.getvalue()
    if output:
        st.subheader("运行结果：")
        st.write(output)

with tab2:
    st.header("南宁美食数据")
    code_file="new.py"
    try:
        with open(code_file,'r',encoding="utf-8")as f:
            code_content = f.read()
    except FileNotFoundError:
        st.error(f"未找到代码文件：{code_file}")
        st.stop()
    old_stdout=sys.stdout
    captured_output=StringIO()
    sys.stdout=captured_output
    try:
        spec=importlib.util.spec_from_loader("temp_module",loader=None)
        temp_module=importlib.util.module_from_spec(spec)
        exec(code_content,temp_module.__dict__)
    except Exception as e:
        st.error(f"代码运行失败：{str(e)}")
    finally:
        sys.stdout=old_stdout

    output=captured_output.getvalue()
    if output:
        st.subheader("运行结果：")
        st.write(output)
        
with tab3:
    st.header("个人简历生成器")
    code_file="new7.py"
    try:
        with open(code_file,'r',encoding="utf-8")as f:
            code_content = f.read()
    except FileNotFoundError:
        st.error(f"未找到代码文件：{code_file}")
        st.stop()
    old_stdout=sys.stdout
    captured_output=StringIO()
    sys.stdout=captured_output
    try:
        spec=importlib.util.spec_from_loader("temp_module",loader=None)
        temp_module=importlib.util.module_from_spec(spec)
        exec(code_content,temp_module.__dict__)
    except Exception as e:
        st.error(f"代码运行失败：{str(e)}")
    finally:
        sys.stdout=old_stdout

    output=captured_output.getvalue()
    if output:
        st.subheader("运行结果：")
        st.write(output)   

with tab4:
    st.header("音乐播放器")
    code_file="music1.py"
    try:
        with open(code_file,'r',encoding="utf-8")as f:
            code_content = f.read()
    except FileNotFoundError:
        st.error(f"未找到代码文件：{code_file}")
        st.stop()
    old_stdout=sys.stdout
    captured_output=StringIO()
    sys.stdout=captured_output
    try:
        spec=importlib.util.spec_from_loader("temp_module",loader=None)
        temp_module=importlib.util.module_from_spec(spec)
        exec(code_content,temp_module.__dict__)
    except Exception as e:
        st.error(f"代码运行失败：{str(e)}")
    finally:
        sys.stdout=old_stdout

    output=captured_output.getvalue()
    if output:
        st.subheader("运行结果：")
        st.write(output)

with tab5:
    st.header("视频播放器")
    code_file="video.py"
    try:
        with open(code_file,'r',encoding="utf-8")as f:
            code_content = f.read()
    except FileNotFoundError:
        st.error(f"未找到代码文件：{code_file}")
        st.stop()
    old_stdout=sys.stdout
    captured_output=StringIO()
    sys.stdout=captured_output
    try:
        spec=importlib.util.spec_from_loader("temp_module",loader=None)
        temp_module=importlib.util.module_from_spec(spec)
        exec(code_content,temp_module.__dict__)
    except Exception as e:
        st.error(f"代码运行失败：{str(e)}")
    finally:
        sys.stdout=old_stdout

    output=captured_output.getvalue()
    if output:
        st.subheader("运行结果：")
        st.write(output)

with tab6:
    st.header("简易相册")
    code_file="two.py"
    try:
        with open(code_file,'r',encoding="utf-8")as f:
            code_content = f.read()
    except FileNotFoundError:
        st.error(f"未找到代码文件：{code_file}")
        st.stop()
    old_stdout=sys.stdout
    captured_output=StringIO()
    sys.stdout=captured_output
    try:
        spec=importlib.util.spec_from_loader("temp_module",loader=None)
        temp_module=importlib.util.module_from_spec(spec)
        exec(code_content,temp_module.__dict__)
    except Exception as e:
        st.error(f"代码运行失败：{str(e)}")
    finally:
        sys.stdout=old_stdout

    output=captured_output.getvalue()
    if output:
        st.subheader("运行结果：")
        st.write(output)        
