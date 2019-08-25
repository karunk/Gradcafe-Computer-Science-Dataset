###GRADCAFE DATA (2014 - Present)

[Link to dataset](https://www.kaggle.com/karun95/gradcafe-computer-science-results)

Repository also includes the script used to generate this dataset.

## The Data
Data contains the following fields


| Column Name        | Description                                                                                                                                                                                                         |
|--------------------|---------------------
| university         | The name of the university (noisy)                   
| major              | The major being pursued (noisy)  
| season              | Fall / Spring                  
| degree             | The degree to be earned. (Masters / PhD)           
| gre_quant          | GRE quant score (where available)   
| gre_verbal          | GRE verbal score (where available)   
| gre_awa          | GRE awa score (where available)              
| decision           | Accepted  / Rejected / Others    
| term_year          | Year of Admission
| undergrad_gpa      | Undergraduate GPA (where available)
| date_added      | Date of entry in gradcafe
| date_of_result | Date of result declaration
| applicant_status      | Status of applicant (International without US degree, International with US degree or American)
| comment | Comment blob written by author

## Script Usage

1. Clone this repository
2. Set your configuration in `config.yaml`. You may change the below two 
variables as per your requirement. `PAGE_LIMIT` specifies the number of 
gradcafe pages to query.

    ```buildoutcfg
   COURSE: 'Computer Science
   PAGE_LIMIT: 200
   
3. Run the command `python scrape.py`

## Requirements
1. python3 (`brew install python3`)
2. yaml (`pip install pyyaml`)
3. bs4 (`pip install beautifulsoup4`)
