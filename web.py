import streamlit as st
import functions as fn

todos = fn.read_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.write_lines(todos)


# def checked():


st.title("My todo App")
st.write("This app is to increase your productivity")
for index,x in enumerate(todos):
    checkbox = st.checkbox(x, key=x)
    if(checkbox):
        todos.pop(index)
        fn.write_lines(todos)
        del st.session_state[x]
        st.experimental_rerun()
        print(checkbox)



st.text_input(label="enter the todo", placeholder="Add new todo : ",
              on_change=add_todo
              , key="new_todo")
st.session_state
