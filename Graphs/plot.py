import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[5, 7, 10, 9],
    y=[1, 7, 5, 9],
    text=['Buy cords for Torben', 'Send email to Ann / Nike', 'Buy ticket for Portland', '500 days board presentation'],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        size=[10, 20, 40, 100],
    )
)
data = [trace0]
layout = go.Layout(
    showlegend=False,
    height=600,
    width=600,
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='bubblechart-text')