"""Page for tasks."""
import streamlit as st
from utils.st_utils import footer
from services.task_service import TaskService

# Initialize the TaskService
task_service = TaskService()

# get the current user
current_user = st.session_state.user


def display_page():
    """Display the tasks page."""
    st.title("Taches")

    # Create Task
    st.write("\n")

    # Add Task
    st.markdown(
        "<div style='font-weight: bold; color: grey; font-size: 30px'>"
        "Formulaire tache</div>",
        unsafe_allow_html=True
    )
    form_col1, form_col2, form_col3 = st.columns([3, 3, 3])
    task_name = form_col1.text_input("Nom")
    task_description = form_col2.text_input("Description")
    task_category = form_col3.text_input("Catégorie")

    if st.button("Ajouter"):
        task_service.create_task(
                                    task_name,
                                    task_description,
                                    current_user,
                                    task_category)
        st.success("Tache bien ajoutée!")

    # List Tasks
    st.write("\n\n")
    st.markdown(
        "<div style='font-weight: bold; color: grey; font-size: 30px'>"
        "Liste de taches</div>",
        unsafe_allow_html=True)

    # set filters
    st.write("\n")
    col1, col2 = st.columns([2, 2])

    # Category Selection
    categories = task_service.get_categories(current_user)
    selected_category = col1.selectbox("Catégorie", ["Tous"] + categories)

    statuses = ["Tous", "ongoing", "completed"]
    selected_status = col2.selectbox("status:", statuses)

    # Fetch tasks based on category
    if selected_category == "Tous":
        tasks = task_service.fetch_all_tasks_for_user(current_user)
    else:
        tasks = task_service.get_tasks_by_category(
            selected_category,
            current_user)

    if selected_status != "Tous":
        tasks = [task for task in tasks if task.status == selected_status]

    # Display tasks
    st.write("\n")
    hcol1, hcol2, hcol3, hcol4, hcol5, hcol6 = st.columns([2, 3, 3, 3, 3, 3])

    hcol1.markdown(
        "<div style='font-weight: bold; color: grey;'>Nom</div>",
        unsafe_allow_html=True)
    hcol2.markdown(
        "<div style='font-weight: bold; color: grey;'>Date</div>",
        unsafe_allow_html=True)
    hcol3.markdown(
        "<div style='font-weight: bold; color: grey;'>Description</div>",
        unsafe_allow_html=True)
    hcol4.markdown(
        "<div style='font-weight: bold; color: grey;'>Statut</div>",
        unsafe_allow_html=True)
    hcol5.markdown(
        "<div style='font-weight: bold; color: grey;'>Supprimer</div>",
        unsafe_allow_html=True)
    hcol6.markdown(
        "<div style='font-weight: bold; color: grey;'>Completer</div>",
        unsafe_allow_html=True)

    st.write("\n")
    col5, col6, col7, col8, col9, col10 = st.columns([2, 3, 5, 3, 3, 3])

    for task in tasks:
        col5.text(task.name)
        col6.text(task.creation_date.strftime('%Y-%m-%d'))
        col7.text(task.description)
        col8.text(task.status)

        if col9.button("Supprimer", key=f"delete_{task.id}"):
            task_service.delete_task(task.id)
            st.success("Tâche supprimée avec succès!")
            st.experimental_rerun()

        if task.status != "completed":
            if col10.button("Completer", key=f"complete_{task.id}"):
                task_service.set_task_completed(task.id)
                st.success(f"Tâche {task.name} complétée!")
                st.experimental_rerun()

    st.write("\n")

    footer()


if __name__ == "__main__":
    display_page()
