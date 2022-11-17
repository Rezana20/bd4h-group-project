## Project goals

1. Read training data and create sentence vectors = DONE
   
   a. Read input to training files - DONE
   
   b. store transformed data - as list of x features and y being hadm_id - using biosentvec - DONE

   
2. Perform patient similarity calculation
   
   a. Calculate using the similarity distance - DONE
   
   b. Store prediction vs actual value  - for later use in metrics - IN PROGRESS
      - Convert each test folder to ordered
      - For each test find best match(across all folds) within alpha for each alpha
         [0][4][1]   -> k:[1][0], k:[4][1], k:[0.1][2][4][1.1], k:[1][0][3], k:[0.2][2][4][1.2][1.4][1.3]
         [0][4][1]   -> k:[1][0] within alpha = 0.7
         [0] -> [1] ~  0.65  no
         [0] -> [0] ~  0.90  yes
         [4] -> [1] ~  0.3   no
         [4] -> [0] ~  0.1   no
         [1] -> [1] ~  0.9   yes
         [1] -> [0] ~  0.7   yes
         ~ Average 0.5 increase the average to 0.7
         1 value for this entire comparison  1 
      - store prediction (best match= pred value , test y = actual value) for every file


3. Later retrieve the model for testing - CDS - P2
   - finding exact match 
   - decreasing similarity threshold from 100 to 95 to 90 

   
4. Create metrics per paper - TO DO 
   - Read every prediction fold, calculate TP and FP 
   - Calculate Recall and Precision 
   - Calculate Beta P2
   - Report on our clock time P2





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






