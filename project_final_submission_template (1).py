#!/usr/bin/env python
# coding: utf-8

# # Project Final Submission Template

# In[4]:


from cs103 import*


# You must sign up for a canvas Project Group on the People page even if you're working alone.
# 
# Student 1: Aariyana Sayani
# 
# Student 2: Jade Hendy
#     
# Canvas Project Group Number: 217 

# ### Step 1a: Planning 
# #### Identify the information in the file your program will read
# 
# Double click this cell to edit.
# 
# The program will read and interpret data about the world happiness rankings in 2017. The program can read any of the following in the csv file of world happiness rankings we provide, within a given country, so long as it has a score: 
# - Happiness rank
# - Happiness score 
# - Whisker high
# - Whisker low
# - Economy (GDP per capita)
# - Family
# - Health (Life expentacy)
# - Freedom, Generosity
# - Trust (Government corruption)
# - Dystopia residual
# 
# All values in the data are in floats. 

# ### Step 1b: Planning 
# #### Brainstorm ideas for what your program will produce
# #### Select the idea you will build on for subsequent steps
# 
# Double click this cell to edit.
# 
# ### Brainstorm
# #### Our program could produce the following:
# - percentage of countries that have a dystopia residual greater than 2 (pie chart)
# - average happiness score for countries that have a Family score below 1 (scatter plot???)
# - average Health (life expectancy) score of the 20 countries with the highest happiness rank (scatter plot???)
# - percentage of European countries whose Economic (GDP) related happiness contributes to at least 20% of their overall happiness score
# - for a given continent, what percentage of the total happiness score is made up of Economic (GDP) related happiness score

# ### Step 1c: Planning 
# #### Write or draw examples of what your program will produce
# 
# Double click this cell to edit. 
# 
# You must include an image that shows what your chart or plot will look like. You can insert an image using the Insert Image command near the bottom of the Edit menu.
# 
# ![image.png](attachment:image.png)

# ### Step 2a: Building
# #### Document which information you will represent in your data definitions
# #### Design data definitions
# 
# Double click this cell to edit.
# 
# Before you design data definitions in the code cell below, you must explicitly document here which information in the file you chose to represent and why that information is crucial to the chart or graph that you'll produce when you complete step 2c.

# In[5]:


from cs103 import*
#enum data definition
Continent = Enum ("Continent", ['Africa', 'Antarctica', 'Asia', 'Australia', 'Europe', 'NorthAmerica', 'SouthAmerica'])
#interp. a continent as being either Africa, Antarctica, Asia, Australia, Europe, North America, or South America
#examples are redundant for enumerations

@typecheck
#template based on one of (7 cases), and atomic distinct (7 times)
def fn_for_continent(c: Continent) -> ...:
    if c == Continent.Africa:
        return ...
    elif c == Continent.Antarctica:
        return ...
    elif c == Continent.Asia:
        return ...
    elif c == Continent.Australia:
        return ...
    elif c == Continent.Europe:
        return ...
    elif c == Continent.NorthAmerica:
        return ...
    elif c == Continent.SouthAmerica:
        return ...


#list of countries that belong to a certain continent
#interp. a list of countries (str), that belong to a certain continent
Africa_list = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Central African Republic', 
          'Chad', 'Congo(Brazzaville)', 'Congo(Kinshasa)', 'Egypt', 'Ethiopia', 'Gabon', 'Ghana', 'Guinea', 'Ivory Coast',
          'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 
          'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda','Senegal', 'Sierra Leone', 'Somalia', 'South Africa', 
          'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
Antarctica_list = ["Antarctica"]
Asia_list = ['Afghanistan', 'Armenia', "Azerbaijan", 'Bahrain', 'Bangladesh', 'Bhutan', 'Cambodia', 'China', 'India', 
        'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Lebanon', 
        'Malaysia', 'Mongolia', 'Myanmar', 'Nepal', 'Oman', 'Pakistan', 'Philippines', 'Qatar', 'Saudia Arabia', 
        'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan',
        'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
Australia_list = ['Australia', 'New Zealand']
Europe_list = ['Russia', 'Ukraine', 'France', 'Spain', 'Sweden', 'Norway', 'Germany', 'Finland', 'Poland', 'Italy', 
         'United Kingdom', 'Romania', 'Belarus', 'Greece', 'Bulgaria', 'Iceland', 'Hungary', 'Portugal', 'Austria', 
         'Czech Republic', 'Serbia', 'Ireland', 'Lithuania', 'Latvia', 'Croatia', 'Bosnia and Herzegovina', 'Slovakia',
         'Estonia', 'Denmark', 'Switzerland', 'Netherlands', 'Moldova', 'Belgium', 'Armenia', 'Macedonia', 'Slovenia',
         "Montenegro", 'Kosovo', 'Cyprus', 'Luxembourg', 'Malta', 'Georgia']
North_America_list = ["Canada", 'United States', 'Mexico','Guatemala', 'Haiti', 'Dominican Republic', 'Honduras',
                'El Salvador', 'Nicaragua', 'Costa Rica', 'Panama', 'Jamaica', 'Trinidad and Tobago', 'Belize']
South_America_list = ['Brazil', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Chile', 'Ecuador', 'Bolivia', 'Paraguay', 
                'Uruguay'] 


#compound data definition
HappinessRank = NamedTuple('HappinessRank', [('continent', Continent),
                                             ('country', str),
                                             ('happiness_score', float), # in range[0,...)
                                             ('gdp_score', float)]) # in range[0,...)

#interp. a happiness rank including country, GDP score and happiness score
HR_NORWAY = HappinessRank(Continent.Europe, 'Norway', 7.537000179, 1.616463184)
HR_DENMARK = HappinessRank(Continent.Europe,'Denmark', 7.521999836, 1.482383013)
HR_ICELAND = HappinessRank(Continent.Europe,'Iceland', 7.504000187, 1.48063302)
HR_ITALY = HappinessRank(Continent.Europe,'Italy', 5.964000225, 1.395066619)
HR_RUSSIA = HappinessRank(Continent.Europe,'Russia', 5.962999821, 1.281778097)
HR_BELIZE = HappinessRank(Continent.NorthAmerica, 'Belize', 5.955999851, 0.907975316)
HR_JAPAN = HappinessRank(Continent.Asia, 'Japan', 5.920000076, 1.416915178)
HR_GREECE = HappinessRank(Continent.Europe,'Greece', 5.227000237, 1.289487481)
HR_LEBANON = HappinessRank(Continent.Asia, 'Lebanon', 5.224999905, 1.074987531)
HR_PORTUGAL = HappinessRank(Continent.Europe, 'Portugal', 5.195000172,1.315175295)

#template based on atomic non-distinct and compound
def fn_for_happiness_rank(hr: HappinessRank) -> ...:
    return ...(fn_for_continent(hr.continent), 
                hr.country,
                hr.happiness_score,
                hr.gdp_score)

# List[HappinessRank]
# interp. a list of HappinessRank

LOHR0 = []
LOHR1 = [HR_DENMARK, HR_JAPAN, HR_PORTUGAL]

# template based on arbitrary-sized and the reference rule
@typecheck
def fn_for_lohr(lohr: List[HappinessRank]) -> ...:
    # description of the acc
    acc = ... # type: ...
    for hr in lohr:
        acc = ... (acc, fn_for_happines_rank(hr))
    return ...(acc)


# ### Step 2b and 2c: Building
# #### Design a function to read the information and store it as data in your program
# #### Design functions to analyze the data
# 
# 
# Complete these steps in the code cell below. You will likely want to rename the analyze function so that the function name describes what your analysis function does.

# # PLAN for program
# ### For a given continent with lots of countries in it: 
# 1. check if a country is in the specififed continent
#     - if the country is in the continent, append it to the list
# 2. calculate overall happiness score and overall gdp related happiness for all countries in the list
# 3. find out the average contribution fo GDP related happiness to the overall happiness score
# 4. make pie chart showing the percentage tha GDP related happiness contributes to the overall happiness score
# 
# We will aim to make a helper function so that we can just change the inputs and then it would generate a pie chart for the specified continent

# - Write a parse_continent()
#     - Should take in a country and produce a continent
# - In parse_continent() use the lists of countries for each continent
#     1. change your data def so it holds a continent and not a country
#     2. write this parse_continent function()
#         - ^^^ this will allow you to read in the data so it matches your compound (ie. has a continent for a field instead of a country)
#     3. make a plan for you analyze with this new data definition
# 

# In[6]:


###########
# Functions

# @typecheck
# def main(filename: str) -> ...:
#     """
#     Reads the file from given filename, analyzes the data, returns the result 
#     """
#     # Template from HtDAP, based on function composition 
#     return analyze(read(filename)) 

@typecheck
def parse_enum(country: str) -> Continent:
    """
    convert a country to a continent
    """
    #return Europe #stub
    #template based on atomic non-distinct (since country is a str it would be atomic non-distinct but the actual
    #template used here looks similar to an enum as well)
    if country in Africa_list:
        return Continent.Africa
    elif country in Antarctica_list:
        return Continent.Antarctica
    elif country in Asia_list:
        return Continent.Asia
    elif country in Australia_list:
        return Continent.Australia
    elif country in Europe_list:
        return Continent.Europe
    elif country in North_America_list:
        return Continent.NorthAmerica
    elif country in South_America_list:
        return Continent.SouthAmerica

start_testing()
expect(parse_enum('Greece'), Continent.Europe)
expect(parse_enum('Japan'), Continent.Asia)
expect(parse_enum('Uganda'), Continent.Africa)
expect(parse_enum('Antarctica'), Continent.Antarctica)
expect(parse_enum('Australia'), Continent.Australia)
expect(parse_enum('Canada'), Continent.NorthAmerica)
expect(parse_enum('Brazil'), Continent.SouthAmerica)

summary()
    

@typecheck
def read(world_happiness_ranking_2017: str) -> List[HappinessRank]:
    """    
    reads information from the specified file and returns a list of happiness rank data
    """
    #return []  #stub
    
    # Template from HtDAP
    # lohr contains the result so far
    lohr = [] # type: List[HappinessRank]

    with open(world_happiness_ranking_2017) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            # you may not need to store all the rows, and you may need
            # to convert some of the strings to other types
            hr = HappinessRank(parse_enum(row[0]), row[0], parse_float(row [2]), parse_float(row[5]))
            lohr.append(hr)
    
        return lohr


# Begin testing
start_testing()

# Examples and tests for read
expect(read("world_happiness_ranking_2017_test1.csv"), [HR_NORWAY, HR_DENMARK, HR_ICELAND])
expect(read("world_happiness_ranking_2017_test2.csv"), [HR_ITALY, HR_RUSSIA, HR_BELIZE, HR_JAPAN])
expect(read("world_happiness_ranking_2017_test3.csv"), [HR_GREECE, HR_LEBANON, HR_PORTUGAL])

# show testing summary
summary()

# @typecheck
# def analyze(loc: List[Consumed]) -> Produced: 
#     """ 
#     ... 
#     """ 

#     return ...


# start_testing()

# # Examples and tests for main
# expect(..., ...)

# summary()

# start_testing()

# # Examples and tests for read
# expect(..., ...)

# summary()

# start_testing()

# # Examples and tests for analyze 
# expect(..., ...) 

# summary()


# # PLAN of helper functions
# 1. check if a country is in a continent
#     - if it is, acc.append to the list
# 2. make a list of all countries in a certain continent
# 3. calculate gdp/overall for a single country
# 4. add up all gdps of all countries in a certain continent
# 5. add up all overalls of all countries in a certain continent
# 6. 
# 7. 
# 8. calculate gdp/overall of a whole continent (and return as a single value)
# 

# In[7]:


#a continent is a list of countries

@typecheck
def check_country_against_continent(hr: HappinessRank, cont: Continent) -> bool:
    """
    return True if a country is in a specified continent and False otherwise
    """
    #return False #stub 
    return hr.continent == cont

@typecheck
def add_country_to_list(hr: HappinessRank, c: Continent) -> List[HappinessRank]:
    """
    if a country is in the specified continent, append it to the list
    """
    #return [] #stub
    for cont in loc:
        if check_country_against_continent(hr, cont):
            acc.append(hr)
    return acc

@typecheck
def calc_country_gdp_hap_score(hr: HappinessRank) -> float:
    """
    return a percentage of a country's GDP related hapiness out of their overall happiness score 
    """
    #return 79 #stub
    return hr.gdp_score/hr.happiness_score

@typecheck
def calc_continent_gdp_hap_score(lohr: List[HappinessRank]) -> float:
    """
    calculate the contribution of a continent's GDP related happiness contribution to their overall hapiness score
    """
    #return 40.3 #stub
    return compile_gdp_scores(c)/calc_continent_avg_overall_hap_score(c)

@typecheck
def compile_gdp_scores(c: Continent) -> float:
    """
    return the sum of all gdp related happiness scores for countries in a certain continent
    """
    #return 0.0 #stub
    acc = 0  #type: int
    for c in loc:
        acc += hr.gdp_score
    return acc

@typecheck
def calc_continent_avg_overall_hap_score(c: Continent) -> float:
    """
    calculate a continent's average overall happiness score by taking the overall happiness score of all countries in a
    continent and dividing by the total amount of countries in the continent
    """
    #return 93.4 #stub
    return calc_country_gdp_hap_score(lohr)

@typecheck
def calc_continent_gdp_contribution(c: Continent) -> float:
    """
    return the percentage that a continent's gdp related happiness contributes to their overall happiness
    """
    #return 0.0 #stub
    return (calc_cont_gdp_hap_score(c)/ calc_continent_avg_overall_hap_score(c))
    
start_testing()

#check_country_against_continent
expect(check_country_against_continent(HR_GREECE, Continent.Europe), True)
expect(check_country_against_continent(HR_JAPAN, Continent.Europe), False)

#add_country_to_list
expect(add_country_to_list(HR_GREECE, Europe_list), )
expect(add_country_to_list(HR_JAPAN, Asia_list), )

#calc_country_gdp_hap_score
expect(calc_country_gdp_hap_score(HR_GREECE), HR_GREECE.gdp_score/HR_GREECE.happiness.score)
expect(calc_country_gdp_hap_score(HR_JAPAN), HR_JAPAN.gdp_score/HR_JAPAN.happiness.score)

#compile_gdp_scores



#calc_continent_gdp_hap_score


#calc_continent_avg_overall_hap_score


#calc_continent_gdp_contribution


summary()


# ### Final Graph/Chart
# 
# Now that everything is working, you **must** call `main` on the intended information source in order to display the final graph/chart:

# In[8]:


main(...)


# In[ ]:


# Be sure to select ALL THE FILES YOU NEED (including csv's) 
# when you submit. As usual, you cannot edit this cell.
# Instead, run this cell to start the submission process.
from cs103 import submit

COURSE = 53525
ASSIGNMENT = 596984 # Final submission

submit(COURSE, ASSIGNMENT)

# If your submission fails, SUBMIT by downloading your files and uploading them 
# to Canvas. You can learn how on the page "How to submit your Jupyter notebook" 
# on our Canvas site.


# In[ ]:




