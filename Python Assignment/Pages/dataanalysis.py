import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    return pd.read_csv("InfluenceofAI_Tools_inCompleting_Assignments_python.csv")  

df = load_data()

st.set_page_config(page_title="Generative AI Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Generative AI Data Analysis DashBoard")

# Description of total and average time and Retain knowledge apply
average_time = round(df["Time_management"].mean(), 1)
average_rating = round(df["Review Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))

left_column, middle_column = st.columns(2)
with left_column:
    st.subheader("Average Time Management:")
    st.subheader(f"🕜{average_time:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")

st.markdown("""---""")

##sidebar
st.sidebar.header("Filter Data")
age = st.sidebar.multiselect("Select Age Range:", options=df["Age"].unique())
gender = st.sidebar.multiselect("Select Gender:", options=df["Gender"].unique(),
                                default=df["Gender"].unique())
education_level = st.sidebar.multiselect("Select Education Level:", options=df["Education_level"].unique())
ai_tools_used = st.sidebar.multiselect("Select Motivation to deep thinking:", options=df["Motivation_to_deep_thinking"].unique())
frequency_of_ai_use = st.sidebar.multiselect("Select problem sloving approach:",options=df["problem_solving_approach"].unique())
df_filtered = df[(df["Age"].isin(age)) &
                 (df["Gender"].isin(gender)) &
                 (df["Education_level"].isin(education_level)) &
                 (df["Motivation_to_deep_thinking"].isin(ai_tools_used)) &
                 (df["problem_solving_approach"].isin(frequency_of_ai_use))]

# Display the filtered data
st.write("Filtered Data:")
st.write(df_filtered)

filtered_edu = df_filtered.groupby(by=["Education_level"])[["Motivation_to_deep_thinking"]].sum().sort_values(by="Motivation_to_deep_thinking")
fig_edu_filtered = px.bar(
    filtered_edu,
    x="Motivation_to_deep_thinking",
    y=filtered_edu.index,
    orientation="h",
    title="<b>Motivation for Deep Thinking by Education Level</b>",
    color = filtered_edu.index, color_discrete_sequence = px.colors.qualitative.Plotly * len(filtered_edu),
    template="plotly_white",
)
fig_edu_filtered.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False)
)

problem_filtered = df_filtered.groupby(by=["Age"])[["problem_solving_approach"]].sum()
fig_problem_filtered = px.bar(
    problem_filtered,
    x=problem_filtered.index,
    y="problem_solving_approach",
    title="<b>Problem Solving Approach By Gender</b>",
    color = problem_filtered.index, color_discrete_sequence = px.colors.qualitative.Set1 * len(problem_filtered),
    template="plotly_white",
)
fig_problem_filtered.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(showgrid=False),
)

# Display the charts based on filtered data
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_edu_filtered, use_container_width=True)
right_column.plotly_chart(fig_problem_filtered, use_container_width=True)

##age count
st.header("Students Age Distribution")
age_counts = df["Age"].value_counts().sort_index()
fig_age = px.bar(x=age_counts.index, y=age_counts.values,
                 labels={"x": "Age", "y": "Number of Users"},
                 title="Students Age Distribution",
                 color=age_counts.index, color_discrete_sequence = px.colors.qualitative.Safe)
st.plotly_chart(fig_age)

# Calculate the number of males and females
gender_counts = df["Gender"].value_counts()
gender_distribution = px.pie(
    gender_counts,
    values=gender_counts.values,
    names=gender_counts.index,
    title="<b>Gender Distribution</b>",
    color_discrete_sequence=["#006699","#009999"],
    template="plotly_white",
)
st.plotly_chart(gender_distribution)

# Calculate the number of males and females
gender_counts = df["AI_tools"].value_counts()
gender_distribution = px.pie(
    gender_counts,
    values=gender_counts.values,
    names=gender_counts.index,
    title="<b>Generative AI Used</b>",
    color_discrete_sequence = px.colors.qualitative.Dark2,
    template="plotly_white",
)
st.plotly_chart(gender_distribution)

#Calculate the number of males and females
edu_distribution = df["Education_level"].value_counts().sort_index()
fig_age = px.bar(data_frame=edu_distribution, x=edu_distribution.index, y=edu_distribution.values,
             labels={"x": "Age", "y": "Number of Customers"}, 
             title="Education Level", color =edu_distribution.index, color_discrete_sequence = px.colors.qualitative.D3)
st.plotly_chart(fig_age)


# Calculate overall quality of work
overall_counts = df["overall_quality"].value_counts()
quality_distribution = px.pie(
    overall_counts,
    values=overall_counts.values,
    names=overall_counts.index,
    title="<b>Overall Quality of Work While using Generative AI</b>",
    color_discrete_sequence = px.colors.qualitative.Bold,
    template="plotly_white",
)
st.plotly_chart(quality_distribution)


# Calculate Influence of Time 
time_counts = df["influneceoftime"].value_counts()
time_distribution = px.pie(
    time_counts,
    values=time_counts.values,
    names=time_counts.index,
    title="<b>Influence of Time While using Generative AI</b>",
    color_discrete_sequence = px.colors.qualitative.T10,
    template="plotly_white",
)
st.plotly_chart(time_distribution)


# Grouping by Age and calculating the mean of Retain Knowledge
data = df.groupby('Age')['Retain_Knowledge_apply'].mean().reset_index()
bar_chart = px.bar(
    data,
    x='Age',
    y='Retain_Knowledge_apply',
    title='Average Retain Knowledge Score by Age',
    labels={'Retain_Knowledge_apply': 'Average Retain Knowledge Score'},
    color='Age',
    template='plotly_white'
)
st.plotly_chart(bar_chart)

# Grouping by Age and calculating the mean of Retain Knowledge
data1 = df.groupby('Education_level')['Apply_critical_thinking'].mean().reset_index()
bar_chart1 = px.bar(
    data1,
    x='Education_level',
    y='Apply_critical_thinking',
    title='Average Apply Critical Thinking Score by Age',
    labels={'Apply_critical_thinking': 'Average Apply_critical_thinking'},
    color='Education_level',
    color_discrete_sequence = px.colors.qualitative.Antique,
    template='plotly_white'
)
st.plotly_chart(bar_chart1)


violin_plot = px.violin(
    df,
    x='Gender',
    y='problem_solving_approach',
    title='Distribution of Problem-Solving Approach by Gender',
    labels={'problem_solving_approach': 'Problem-Solving Approach', 'Gender': 'Gender'},
    color = 'Gender', color_discrete_sequence = px.colors.qualitative.Light24
)
st.plotly_chart(violin_plot)


