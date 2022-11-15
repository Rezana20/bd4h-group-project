## Project goals

1. Read training data and create sentence vectors = DONE
   
   a. Read input to training files
   
   b. store transformed data - as list of x features and y being hadm_id - using biosentvec

   
2. Perform patient similarity calculation
   
   a. Calculate using the similarity distance vs RNN 
   
   b. Store prediction vs actual value  - for later use in metrics


3. Later retrieve the model for testing - CDS

   
4. Create metrics per paper


## Project structure


data:
- contains all the data for training and testing the model. 
- we will store the folds here

models:
- all the classes used in the project 

data_transformer.py
- input data transformed into sentence vectors usong biosentvec as well as persisted.

main.py
- choreography pattern for the CDS framework

cds.py
- this class will test be used to take in a list of symptoms from a physician and then provide a diagnosis 

metrics.py
- class used to recreate paper metrics 


##  How to set up the project environment

- after downloading the project run `conda env create -f environment.yml
`
- now activate the enviroment: run `conda activate project`

- navigate to the sent2vec folder and run `pip install .`

//ultimate goal
- run the cds.py to use the framework to make a prediction


When making changes to the environment, update the environment.yml and then run ` conda env update`


Prior to set up I had to download sent2vec from git, this is now stored in the package and you do not need to repeat this step. 
I followed the below steps after creating and setting up my local environment

1. `git clone https://github.com/epfml/sent2vec.git`
2. `cd sent2vec`
3. `pip install . `





