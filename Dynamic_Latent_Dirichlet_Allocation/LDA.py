import little_mallet_wrapper
import seaborn
import glob
from pathlib import Path
import random
import re
from Preprocess import preprocess
import os

path_to_mallet = os.getcwd()+ '/mallet-2.0.8/bin/mallet'

parent_directory = os.path.abspath('..')
sys.path.append(parent_directory)

# Run the preprocessing 
df= preprocess('articles.json')

training_data = [little_mallet_wrapper.process_string(content, numbers='remove') for content in df['content']]

text = [title for title in df['content']]

df['content'] = df['content'].astype(str)

little_mallet_wrapper.print_dataset_stats(training_data)

num_topics = 10

#Change to your desired output directory
output_directory_path =  os.getcwd() + '/Output_MALLET'

#No need to change anything below here
Path(f"{output_directory_path}").mkdir(parents=True, exist_ok=True)

path_to_training_data           = f"{output_directory_path}/training.txt"
path_to_formatted_training_data = f"{output_directory_path}/mallet.training"
path_to_model                   = f"{output_directory_path}/mallet.model.{str(num_topics)}"
path_to_topic_keys              = f"{output_directory_path}/mallet.topic_keys.{str(num_topics)}"
path_to_topic_distributions     = f"{output_directory_path}/mallet.topic_distributions.{str(num_topics)}"



little_mallet_wrapper.quick_train_topic_model(path_to_mallet,
                                                                     output_directory_path,
                                                                     num_topics,
                                                                     training_data)