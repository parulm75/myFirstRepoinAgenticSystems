import pandas as pd
import plotly.express as plt
import numpy as np
np.random.seed(42)
data={
    "epochs": range(1,11),
    "loss":np.random.randn(10)
}
df=pd.DataFrame(data)
fig=plt.line(
    df,
    x="epochs",
    y="loss",
    title="Line graph epochs vs loss",
)
fig.add_annotation(
    x=5.5,
    y=-0.2341,
    text="Loss stabilizes here",
    showarrow=True,
    arrowhead=2
)
fig.show()