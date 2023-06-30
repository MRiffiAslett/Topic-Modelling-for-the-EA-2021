import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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

        # Calculate standard error of the mean
        sem = df[column].rolling(window=window_size).std() / np.sqrt(window_size)

        # Add standard error to the rolling mean
        df_smoothed_plus_sem = df_smoothed + sem
        df_smoothed_minus_sem = df_smoothed - sem

        axs[i].plot(df.index, df_smoothed, label='Rolling Mean')
        axs[i].fill_between(df.index, df_smoothed_minus_sem, df_smoothed_plus_sem, color='b', alpha=0.2)
        axs[i].set_xlabel("Date")
        axs[i].set_ylabel("Value")
        axs[i].set_title(column)  # Set the title as the column name
        axs[i].legend()

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




def plot_df_bootstrapped(df, window_size=7, indexes=None):
    # Convert PeriodIndex to DateTimeIndex if needed
    if isinstance(df.index, pd.PeriodIndex):
        df.index = df.index.to_timestamp()

    n = len(df.columns)
    fig, axs = plt.subplots(n if indexes is None else len(indexes), 1, figsize=(10, 5*(n if indexes is None else len(indexes))))  # adjust the size based on number of plots

    # Convert indexes to list if None is provided
    if indexes is None:
        indexes = list(range(n))

    # Ensure indexes are within valid range
    indexes = [i for i in indexes if i >= 0 and i < n]

    # Check if axs is a single AxesSubplot or an array of AxesSubplots
    if not isinstance(axs, np.ndarray):
        axs = np.array([axs])

    # Loop over specified indexes
    for i, ax in zip(indexes, axs):
        column = df.columns[i]

        # Apply rolling mean
        df_smoothed = df[column].rolling(window=window_size).mean()

        ax.plot(df.index, df_smoothed)
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")
        ax.set_title(column)  # Set the title as the column name

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

        