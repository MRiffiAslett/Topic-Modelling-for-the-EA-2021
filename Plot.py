import pandas as pd
import matplotlib.pyplot as plt

def plot_df(df, window_size=7):
    # Convert PeriodIndex to DateTimeIndex if needed
    if isinstance(df.index, pd.PeriodIndex):
        df.index = df.index.to_timestamp()

    n = len(df.columns)
    fig, axs = plt.subplots(n, 1, figsize=(10, 5*n))  # adjust the size based on number of plots

    # Loop over every column
    for i, column in enumerate(df.columns):
        # Apply rolling mean
        df_smoothed = df[column].rolling(window=window_size).mean()

        axs[i].plot(df.index, df_smoothed)
        axs[i].set_xlabel("Date")
        axs[i].set_ylabel("Value")
        axs[i].set_title(column)  # Set the title as the column name

    plt.tight_layout()
    plt.show()


def print_coherence(dic, topics_list,text):
    from gensim.models.coherencemodel import CoherenceModel
    from gensim.corpora.dictionary import Dictionary

    # Coherence model
    cm = CoherenceModel(topics=topics_list,
                        texts=text,
                        coherence='c_v',
                        dictionary=dic)

    coherence_per_topic = cm.get_coherence_per_topic()

    topics_str = [','.join(t)[:45] for t in topics_list]
    data_topic_score = zip(topics_str, coherence_per_topic)

    for topic, coherence in data_topic_score:
        print(f"Topic: {topic}\tCoherence: {coherence:.2f}")

        