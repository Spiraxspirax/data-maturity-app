# dashboard.py

import plotly.graph_objects as go

def create_radar(scores):
    categories = list(scores.keys())
    values = list(scores.values())

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # loop back for radar chart
        theta=categories + [categories[0]],
        fill='toself',
        name='Maturity'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        showlegend=False
    )
    return fig
