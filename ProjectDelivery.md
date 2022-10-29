###Team project Summary things to do

Important dates and tasks

**Due Date   Task Description**
**Oct 3      Group formation & (candidate) paper selection [3]**
**Oct 17     Project proposal [4, 5]**
**Nov 21     Project draft [6, 7]**
**Dec 5      Final Submission (final paper + code + presentation) [8, 9]**


1. Select a paper  - add options to list [
61,  FarSight: Long-Term Disease Prediction Using Unstructured Clinical Nursing Notes 
168, Med7: A transferable clinical natural language processing model for electronic health records - David
267, AI-Driven Clinical Decision Support: Enhancing Disease Diagnosis Exploiting Patients Similarity - Rezana 


2. Register Team on excel link  - Done

3. Register Paper by submitting a pdf to gradescope with the team details and paper selection, follow instructions on Submit_at_team_level_pdf - Done 

4. Project Proposal 
	a. Review selection from previous steps and then select 1
	b. Audience of project proposal is someone who has **not** read the paper
	c. Create a projet poposal doc with summaries of all three  options and the teams selection 
	d. Submit to gradescope at team level

5. Project proposal guidelines:

	For each paper selection complete the below 

	Index, Paper title, Venue, Authors 
	a. Task: 
	b. Innovation: 
	c. Dis/Adv:
	d. Data Accessibility: 
	e. Code Accessibility:


	Decide your teams target paper


6. Project Draft 
	a. Fully understood paper and code
	b. Document full scope of experiments to reproduce
	c. Set up basic code  ( complete ETL process, and ML model to be developed)
	d. Run one experiment
	e. Conclude results
	f. Add futuure optimisation plan


7. Project Draft format:
	a. Introduction
	b. Scope of reproducibility
	c. Methodology
		- Model descriptions
		- Data descriptions
		- Computational implementation
		- Code
	h. Results:
	i. Discussion: 



8. Final Report - 8 pages max
	a. Complete all sections 
		a. Introduction
		b. Scope of reproducibility
		c. Methodology
			- Model descriptions
			- Data descriptions
			- Computational implementation
			- Code
		h. Results:
		i. Discussion: 
	b. Upload your well-documented codebase to Github, Gitlab, etc and attach the link at beginning of your report.
	c. Upload your presentation video in Youtube, OneDrive, Google Drive, etc and attach the link at beginning of your report.


9. Presentation
	a. Prepare slides wiht main points +  results. 
	b. Presentation  5-8 minutes long.
	c. It should delivered through online platform (Youtube, OneDrive, Google Drive, and any other places that grader can access easily).
	d. It is fine that the presentation is done by either both members or only one member.
	e. Good visuals are important here. Text should be in large font, figure and tables are captioned with description.



------


Team Delivery Plan


Meeting notes:
Date: Tue Sept 20

To do:
1. Select a paper each - done
2. Find code reference  - done
3. Review choices all choices and create summarise content to make decision for the project proposal - Done
4. Provide feedback to eachother about the reviewed - Done
5. Aim for 28th 29th to be completed

6. Complete the project proposal - on going to be completed by 12th october git push - offline
7. Complete the review of all papers (Rezana to do AI-Driven Clinical Decision... and David to rereview his existing submission) - done
8. Decide on the paper - present to each other in before week 1 ends and then use week 2 to try and get to the project draft and decide on a technical solution.  - done
9. Meet around Oct 7 and 8 - done

10. Reread + understand selected paper, schedule a discussion, understanding the libaries the referenced paper for the model - Saturday 10 am - Lunch break - till the afternoon
11. Plan technical approach
12. Plan a delivery high level plan + first delivery.  - clean the data, pass it through BioSentVec, we pass new patient data through BioSentVec, compare the similarity of new patient to all old, and then we a result and from the result we determine if this was T/F  - reproduce the two graphs and precision recall and the bar plot for big data. 

Fold 0 
Decide 75% testing and 25% training. 
13. Replicate bioSentVec example with our data - https://github.com/ncbi-nlp/BioSentVec/blob/master/BioSentVec_tutorial.ipynb  - David -> output structure 
14. Get orginal data - from https://github.com/ncbi-nlp/BioSentVec/blob/master/BioSentVec_tutorial.ipynb
15. Simalrity equation used to be understood.  - Rezana figure out how we can use in our example .
need the output structure  from 13 to produce the correct equation - to consider how to produce the graphs.
16. Next meeting is on slack chat - update about what we are doing, thereafter we should commit to a date to showcase the solution and try integrate. (By 22 Oct)

Next steps 
17. David - to submit code + add logic to store vectors, descale the table/files we are using - 1 Nov
18. Try and implement similarity equation on the output - try and implement this - Rezana - write this to a file - 1 Nov - 5 Nov
19. Start proposal_draft - Rezana + David - Rezana push template, offline on slack Rezana to update David what he can do. 





Model Similarity: test 1 : train 2
Actual: test 1: actual result



-----

Issue tracker for Med7: https://github.com/kormilitzin/med7/issues/23


----

Med7 Pros and Cons
1. Pros - Easy to understand paper 
2. Pros - Library exists - code exist, there is someone who can answer questions on the  paper and the library. 

3. Con - Lack of understanding code etc - code does not work
4. Con - Data access - UK data not acccessible - challenging
5. Con - We have to reproduce this paper exactly/better

AI driven CDS Pros and Cons
1. Pros - Understandable
2. Pros - We do not have to replicate the paper exactly as is 
3. Pros - The framework can be built similar to the paper

4. Cons - a lot of time dedicated to complete
5. Cons - having to understand some complex libraries Sent2Vec or BioSentVec
