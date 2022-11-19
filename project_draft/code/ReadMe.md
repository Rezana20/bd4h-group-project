

## Project structure

>data :
- contains all the data for training and testing the model. 
- we will store the folds here
- you will notice extra data folder paths namely processed, sorted and ordered. These directories allow the storing of processed data throughout the creation of historic patient vectors

> main.py
- choreography pattern for the CDS framework
- this class contains the framework steps and is in charge of treating the historic patient data using the data_transformer module
- this class also uses the cds module which uses the output of data transformation, that is the vectorised symptoms and directs the steps to do patient similarity. 
- this class also calls the metrics class to perform testing 
- this class also signals the metrics for analysing accuracy 

>data_transformer.py
- input data transformed into sentence vectors using the biosentvec model 
- data goes through 3 levels of treatment, that is converting to vectors, sorting symptoms per diagnosis and then ordering diagnosis
- at each stage data is persisted into folders with corresponding names 

>cds.py
- this class uses the results from the data_transformer and converts the data into dictionaries at read
- this class then implements the patient cosine similarity equation as defined in the paper to efficiently search target patient against historic patient data  persist into data storage 
- this class also contains the capability to tests the framework  and could take in a list of symptoms from a physician and then provide a diagnosis 
- the results of the tests are persisted into maps of predicted value -> actual value for later metric analysis

> metrics.py
- class used to recreate performance metrics 
- this class uses output from testing for various aplha by reading in the data 
- this class calculates TPs and FPs for Precision and Recall calcultions
- this class does our metric graphing

> models:
- defined as any domain objects that we would want to use in the project 

----


##  How to set up the project environment

###Step 1 
- download the biosentvec model used to train the vectors from https://github.com/ncbi-nlp/BioSentVec

- Make sure you download the BioSentVec model 21GB (700dim, trained on PubMed+MIMIC-III) from https://ftp.ncbi.nlm.nih.gov/pub/lu/Suppl/BioSentVec/BioSentVec_PubMed_MIMICIII-bigram_d700.bin

- Note that this model is 21GB and will require disk space to download and use, you will also need to pre-download as this takes time

###Step 2

- download this folder (https://github.com/Rezana20/bd4h-group-project/tree/main/project_draft/code)

###Step 3

- after retrieving source code place downloaded biosenvec  model into the folder named: biosentvec_model

###Step4
- run `conda env create -f environment.yml`

###Step5 
- now activate the enviroment: run `conda activate project`

###Step 6
- to re-produce project run `python main.py`

---------




## Team Project delivery tracker

1. Read training data and create sentence vectors = DONE
   
   a. Read input + convert to csv to training files - DONE
   
   b. store transformed data - as list of x features and y being hadm_id - using BioSentVec - DONE

   c. sort and order data - DONE
   
   d. store transformed data at each stage - DONE 

   
2. Perform patient similarity calculation
   
   a. Calculate using the similarity distance explained in the paper- DONE
   
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
   
    a. finding exact match 
   
    b. decreasing similarity threshold from 100 to 95 to 90 

   
4. Create metrics per paper - IN PROGRESS
    
    a. Read every prediction fold, calculate TP and FP 
   
    b. Calculate Recall and Precision 
   
    c. Calculate Beta P2 
   
    d. Consider report on our clock time P2
    

5. Build a scalable framework:
    
    a. Allow adding of folds of data with minimal change - DONE

    b. Allow sorting/ordering without reprocessing all historic data - DONE

    c. Allow new prediction on CDS without any new training - DONE

//ultimate goal
- run the cds.py to use the framework to make a prediction

//note

When making changes to the environment, update the environment.yml and then run ` conda env update`



