"""
Python Data Visualization Assignment - Starter Code
Author: Mergington High School
Description: Starter code for creating data visualizations with matplotlib and plotly
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Sample data: Student test scores across subjects
data = {
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'],
    'Q1_Scores': [85, 78, 88, 92, 79],
    'Q2_Scores': [88, 82, 90, 95, 85],
    'Q3_Scores': [92, 86, 94, 98, 88]
}

df = pd.DataFrame(data)

# TODO: Task 1 - Create Basic Charts with Matplotlib
# Create at least 3 different types of charts (line, bar, scatter)
# Example starter for a bar chart:

def create_bar_chart():
    """Create a simple bar chart"""
    plt.figure(figsize=(10, 6))
    x = df['Subject']
    y = df['Q1_Scores']
    plt.bar(x, y, color='steelblue')
    plt.title('Student Scores by Subject (Q1)', fontsize=14, fontweight='bold')
    plt.xlabel('Subject', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.ylim([0, 100])
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('bar_chart.png')
    plt.show()


# TODO: Task 2 - Customize and Style Visualizations
# Create subplots with custom styling

def create_styled_subplots():
    """Create multiple styled charts in subplots"""
    # TODO: Implement custom styling
    pass


# TODO: Task 3 - Create Interactive Visualizations with Plotly
# Create interactive charts that users can interact with

def create_interactive_chart():
    """Create an interactive visualization with Plotly"""
    # Example: Interactive line chart
    fig = px.line(df, x='Subject', y=['Q1_Scores', 'Q2_Scores', 'Q3_Scores'],
                  title='Student Performance Across Quarters',
                  labels={'value': 'Score', 'Subject': 'Subject'},
                  markers=True)
    fig.update_layout(
        xaxis_title='Subject',
        yaxis_title='Score',
        hovermode='x unified'
    )
    fig.write_html('interactive_chart.html')
    fig.show()


# Main execution
if __name__ == '__main__':
    # Uncomment to run each function
    # create_bar_chart()
    # create_styled_subplots()
    # create_interactive_chart()
    
    print("Data Visualization Assignment - Starter Code Ready!")
    print("Complete the TODO sections above to finish the assignment.")
    print(f"\nSample Data:\n{df}")
