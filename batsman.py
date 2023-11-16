import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\deliveries.csv')

def dissmisal_pie(name):
    print(name)
    filt = df["batsman"] == name
    x = df[filt]
    print(x.shape)

    x["dismissal_kind"].value_counts().plot.pie(autopct="%1.2f%%")
    plt.title("{} KIND OF DISMISSAL ".format(name))
    plt.gcf().canvas.set_window_title("Pie chart for dissmisal kind")
    plt.show()

def dissmisal_bar(name):
    filt = df["batsman"] == name
    x = df[filt]
    print(x.shape)

    x["dismissal_kind"].value_counts().plot.bar()
    plt.title("{} KIND OF DISMISSAL ".format(name))
    plt.gcf().canvas.set_window_title("Bar graph for dissmisal kind")
    plt.xticks(rotation=20)
    plt.show()

def runs_pie(name):
    filt = df["batsman"] == name
    x = df[filt]




    a = len(x[x['batsman_runs'] == 1]) * 1
    b = len(x[x['batsman_runs'] == 2]) * 2
    c = len(x[x['batsman_runs'] == 3]) * 3
    d = len(x[x['batsman_runs'] == 4]) * 4
    e = len(x[x['batsman_runs'] == 6]) * 6
    slices = [a, b, c, d, e]
    labels = [1, 2, 3, 4, 6]
    explode = [0.1, 0.1, 0.1, 0.1, 0.1]
    plt.pie(slices, labels=labels, autopct="%1.2f%%", explode=explode)
    plt.title("{} Runs Scored ".format(name))
    plt.gcf().canvas.set_window_title("Pie chart for runs scored")
    plt.show()

def runs_bar(name):
    filt = df["batsman"] == name
    x = df[filt]

    a = len(x[x['batsman_runs'] == 1]) * 1
    b = len(x[x['batsman_runs'] == 2]) * 2
    c = len(x[x['batsman_runs'] == 3]) * 3
    d = len(x[x['batsman_runs'] == 4]) * 4
    e = len(x[x['batsman_runs'] == 6]) * 6
    l1 = ['one', 'two', 'three', 'four', 'six']
    l2 = [a, b, c, d, e]
    plt.bar(l1, l2, color='black', width=0.2)

    plt.title("{} Runs Scored ".format(name))
    plt.gcf().canvas.set_window_title("Bar graph for runs scored")
    plt.show()

#4s
four=df[df["batsman_runs"]==4]
print(four)
runs_4=four.groupby("batsman")["batsman_runs"].count().reset_index()
runs_4.columns=["batsman","4s"]
print(runs_4)

# 6's by batsman
six = df[df["batsman_runs"] == 6]
print(six)
runs_6 = six.groupby("batsman")["batsman_runs"].count().reset_index()
runs_6.columns = ["batsman", "6s"]
print(runs_6)

#balls played by batsman
ball=df.groupby("batsman")["ball"].count().reset_index()
print(ball)

#runs scored by batsman
runs=df.groupby("batsman")["batsman_runs"].sum().reset_index()
print(runs)

#concatenate df for batsman avg
player=pd.concat([runs,ball.iloc[:,1],runs_4.iloc[:,1],runs_6.iloc[:,1]],axis=1)
print(player)
player.fillna(0,inplace=True)
print(player)

#most runs by batsman
def max_runs():
    max_runs=df.groupby("batsman")["batsman_runs"].sum()
    b=max_runs.sort_values(ascending=False)[:10]
    b.plot.bar(x="batsman",y="max_runs")
    plt.title("Top 10 batsman with maximum runs")
    plt.gcf().canvas.set_window_title("Maximum runs")
    plt.show()
    print(b)
#max_runs()

#strike_rate
def higest_sr():
    player["strike_rate"]=(player["batsman_runs"]/player["ball"])*100
    print(player)
    a=player.sort_values("strike_rate",ascending=False)[:10]
    a.plot.bar(x="batsman",y="strike_rate")
    print(a)
    plt.title("Top 10 batsman having highest strike rate ")
    plt.gcf().canvas.set_window_title("Highest strike rate")
    plt.xticks(rotation=20)
    plt.show()

#higest_sr()

def most_4():
    #top10 batsman with most 4s
    a=runs_4.sort_values("4s",ascending=False)[:10]
    a.plot.bar(x="batsman",y="4s")
    print(a)
    plt.title("Top 10 batsman who scored most 4 runs")
    plt.gcf().canvas.set_window_title("Most 4 runs")
    plt.show()

#most_4()

def most_6():
    #top10 batsman with most 6s
    b=runs_6.sort_values("6s",ascending=False)[:10]
    b.plot.bar(x="batsman",y="6s")
    print(b)
    plt.title("Top 10 batsman who scored most 6 runs")
    plt.gcf().canvas.set_window_title("Most 6 runs")
    plt.show()

#most_6()