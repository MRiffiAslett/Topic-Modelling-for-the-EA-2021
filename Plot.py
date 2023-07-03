import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_df(df, model, span_size=7, add_error_bars=False):
    # Convert PeriodIndex to DateTimeIndex if needed
    if isinstance(df.index, pd.PeriodIndex):
        df.index = df.index.to_timestamp()

    if add_error_bars:
        
        save_directory = 'saved_plots_SE'
        os.makedirs(save_directory, exist_ok=True)
    else:
            # Create the 'saved_plots' directory if it doesn't exist
        save_directory = 'saved_plots'
        os.makedirs(save_directory, exist_ok=True)

    # Loop over every column
    for i, column in enumerate(df.columns):
        # Apply moving average
        df_smoothed = df[column].rolling(window=span_size).mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlabel("Date in Months (From January 2012 to May 2023)")
        ax.set_ylabel("Topic Proportion")
        
        # Construct the title with topic number and column name
        title = f"{model}, Topic {i+1}: [{column}]"
        
        ax.set_title(title)
    
        if add_error_bars:
            # Calculate standard errors
            std_error = df[column].ewm(span=span_size).std() / np.sqrt(span_size)
    
            ax.fill_between(df.index, df_smoothed - std_error, df_smoothed + std_error, color='blue', alpha=0.3)
            ax.plot(df.index, df_smoothed, label='Moving averages')
            ax.plot([], [], color='blue', alpha=0.3, linewidth=10, label='Standard Error')

            # Get the legend and update the handler for the error bar
            legend = ax.legend()
            legend.legendHandles[1].set_color('blue')
            legend.legendHandles[1].set_alpha(0.3)
            legend.get_texts()[1].set_color('blue')

            save_filename = os.path.join(save_directory, f"topic_{i+1}_{model}_{column}_plot_with_SE.png")
        else:
            ax.plot(df.index, df_smoothed, label='Moving Average')
            save_filename = os.path.join(save_directory, f"topic_{i+1}_{model}_{column}_plot.png")
    
        ax.legend()
        plt.tight_layout()
        fig.savefig(save_filename)
        plt.close(fig)

    # Save all plots in one image
    fig, axs = plt.subplots(len(df.columns), 1, figsize=(10, 5 * len(df.columns)))  # adjust the size based on the number of plots
    
    for i, column in enumerate(df.columns):
        # Apply moving average
        df_smoothed = df[column].rolling(window=span_size).mean()

        if add_error_bars:
            # Calculate standard errors
            std_error = df[column].ewm(span=span_size).std() / np.sqrt(span_size)
    
            axs[i].fill_between(df.index, df_smoothed - std_error, df_smoothed + std_error, color='blue', alpha=0.3)
            axs[i].plot(df.index, df_smoothed, label='Moving averages')
            axs[i].plot([], [], color='blue', alpha=0.3, linewidth=10, label='Standard Error')

            # Get the legend and update the handler for the error bar
            legend = axs[i].legend()
            legend.legendHandles[1].set_color('blue')
            legend.legendHandles[1].set_alpha(0.3)
            legend.get_texts()[1].set_color('blue')
        else:
            axs[i].plot(df.index, df_smoothed, label='Moving averages')

        axs[i].set_xlabel("Date in Months (From January 2012 to May 2023)")
        axs[i].set_ylabel("Topic Proportion")
        
        # Set the title with topic number and column name
        axs[i].set_title(f"{model}, Topic {i+1}: [{column}]")
        
    
    plt.tight_layout()
    plt.show()
    # Display the combined plot
    if add_error_bars:
        save_filename_all = os.path.join(save_directory, f"{model}_all_plots_with_SE.png")
    else:
        save_filename_all = os.path.join(save_directory, f"{model}_all_plots.png")
    fig.savefig(save_filename_all)
    plt.close(fig)


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




def plot_df_bootstrapped(df, span_size=7, indexes=None):
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

        # Apply exponential moving average
        df_smoothed = df[column].ewm(span=span_size).mean()

        ax.plot(df.index, df_smoothed)
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")
        ax.set_title(column)  # Set the title as the column name

    plt.tight_layout()
    plt.show()





        