import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="To-Do List App",
    page_icon="📝",
    layout="centered"
)

# Title
st.title("📝 To-Do List Application")
st.write("Manage your daily tasks easily")

# Session State for Tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []


st.header("➕ Add New Task")

new_task = st.text_input("Enter your task")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(
            {
                "task": new_task,
                "completed": False
            }
        )
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a valid task.")


st.header("📋 Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks available.")
else:

    for index, task in enumerate(st.session_state.tasks):

        col1, col2, col3 = st.columns([6, 2, 2])

        # Task Checkbox
        with col1:
            completed = st.checkbox(
                task["task"],
                value=task["completed"],
                key=f"check_{index}"
            )

            st.session_state.tasks[index]["completed"] = completed

        # Edit Button
        with col2:
            if st.button("✏️ Edit", key=f"edit_{index}"):

                st.session_state.edit_index = index

        # Delete Button
        with col3:
            if st.button("🗑 Delete", key=f"delete_{index}"):

                st.session_state.tasks.pop(index)
                st.rerun()


if "edit_index" in st.session_state:

    st.header("✏️ Edit Task")

    current_task = st.session_state.tasks[
        st.session_state.edit_index
    ]["task"]

    updated_task = st.text_input(
        "Update your task",
        value=current_task
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Save Changes"):

            st.session_state.tasks[
                st.session_state.edit_index
            ]["task"] = updated_task

            del st.session_state.edit_index

            st.success("Task updated successfully!")
            st.rerun()

    with col2:
        if st.button("Cancel"):

            del st.session_state.edit_index
            st.rerun()


st.sidebar.title("📌 Task Summary")

total_tasks = len(st.session_state.tasks)

completed_tasks = len(
    [
        task for task in st.session_state.tasks
        if task["completed"]
    ]
)

pending_tasks = total_tasks - completed_tasks

st.sidebar.write(f"✅ Completed Tasks: {completed_tasks}")
st.sidebar.write(f"⌛ Pending Tasks: {pending_tasks}")
st.sidebar.write(f"📋 Total Tasks: {total_tasks}")

# Clear All Tasks
if st.sidebar.button("🗑 Clear All Tasks"):

    st.session_state.tasks = []
    st.success("All tasks cleared!")
    st.rerun()