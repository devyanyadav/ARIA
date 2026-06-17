# What Makes a Country Happy? — A Data-Driven Analysis
### Using the World Happiness Report 2015-2019

---

## Abstract
Understand how to establish a happy population is extremely important for individual countries. At the national level, it ensures maximum productivity, economic development and helps diagnose problems in a country. Today, one of the leading factors of low happiness is lack of understanding on how to keep a population happy, This study depicts what are the important factors that a country should focus on to improve their happiness score. On top of the analysis, a rule based system named ARIA has been designed that diagnoses the problems of the strengths and weakness of a country.
ARIA outputs a conclusion after the chain of thinking, In which it provides its recommendations for the country. The analysis showed that for a country to be happy, the most important factor is gdp per capita which has a correlation measurement of 0.789 with happiness, it is followed up by health with 0.742  and social relations with 0.648. Further it also showed that rich countries enjoy more freedom, better health and better social relations while the poor mostly suffered in these factors. However, richer countries are know to have higher rates of corruption than poor countries. Moreover, this study finds that the global happiness trend remained flat over the years 2015 to 2019. At last, the study found no outlier that were both poor as in below 25th percentile and happy as in above 75th percentile. From this study it can be taken that governments should prioritise economic development, education, and basic services. 

## 1. Introduction

Understanding how to achieve a happy population is extremely important. A happy population ensures maximum productivity and fulfils the goal of a national level organisation who want to work for the betterment of their people. This data is also important at the national level as it helps international organsisations identify which countries need help and intervention.
The current problem many individual countries have in improving their happiness is not understanding what actually affects the happiness scores of their own people. This lack of understanding can cause problems in productivity and development.
My study and ARIA, a rule based system bridge this lack of understanding. This research report goes over what are the important factors to invest in to make the overall  population happy. ARIA can find weakness and strengths of a country and evaluate which factors the country can improve in.


## 2. Dataset & Methodology

The dataset was sourced from Kaggle (kaggle.com/datasets/unsdsn/world-happiness), published by the Sustainable Development Solutions Network for the United Nations, and covers the years 2015 to 2019.The happiness score is measured by the Gallup Cantril ladder survey method.It's considered one of the most reliable ways to measure subjective wellbeing across different cultures because it's self-referential — people define "best" and "worst" for themselves rather than being given fixed criteria.
The data was cleaned by standardising uniform columns for each csv file. Further, many columns that were considered a distraction were also dropped like Dystopia, Standard Error, region and other columns that were not uniform throughout all the data. Dystopia was excluded from the main dataset because it contained unnecessary data that would have created inconsistencies in the analysis. Region column was excluded from the main dataset because of the inconsistent availability across different years and the non-uniform naming conventions. 
The final merged dataset contains approximately 780 rows covering 150+ countries across five years.


## 3. Findings

### 3.1 What Drives Happiness?

Two different measurements were found each giving different rankings, between who was the more influencing factor wealth or social relations. When each factor was expressed as a proportion  of the happiness score, social relations contributed the most with 33.7 percent, followed by gdp per capita with 27.6 percent and health with 18.7 per cent. However, after calculating the correlations with each factor to the happiness  gdp per capita correlated with happiness score the most  with 0.789284, followed by health with 0.742456 and social support with 0.648799. 
After analysing the two different measurements that had formed out of the same data, a conclusion was achieved that the reason for the high gdp per capita correlation is because it boosts some factors like health,freedom and social relations. This was verified by plotting a scatter graph showing that the rich scored high in other factors like freedom,health and social relations , When the same graph was plotted for the poor it showed the opposite, low scores in other factors.The correlation measurement is more trusted as it gives more information about the pattern of a happy country, whereas a proportion  contribution does not give us all this information.

### 3.2 Rich vs poor

Does money buy happiness ? A key pattern was identified between gdp per capita and happiness score. As explored in section 3.1, The pattern identified was that richer countries scored comparatively higher in factors like freedom,health and social relations than the poor who scored considerably  worse. Corruption was also higher in richer countries but lower in poorer countries. No pattern was seen in generosity, poor or rich had no effect on this factor.
The methodology consisted of plotting scatter graphs of poor and rich and analysing them. The scatter graphs for the rich were plotted for the  countries who were above the 75th percentile of gdp per capita and the scatter graph of the poor were plotted for the countries who were below the 25th percentile of gdp per capita.
Money does not buy happiness but it buys some factors that contribute to a happy population and is still not able to buy factors like generosity and low corruption.


### 3.3 Global Trend 2015-2019

Has the global population grown happier over the years ? It was found that the human population has not grown happier over the years and remained quite stable between 5.35 and 5.40. A minor dip was also noticed in the year 2017, where the happiness score fell by approximately 0.02.
This was found by plotting a line graph representing the overall growth of the happiness score of the entire world over the years. 

### 3.4 Outlier Analysis

When Attempted to find outliers who were below the 25th percentile of poor and above 75th percentile of happiness score, zero outliers were found. This indicates that no country with a low gdp is happy.  This strengthens my argument that gdp per capita is the most important factor to produce a happy population.


## 4. ARIA System 
ARIA's system is entirely built upon the findings of the analysis. ARIA is a rule-based system  whose inference chain begins when it creates a profile of the country which gives each factor a score out of 5. ARIA has four built-in scenarios which are rich and happy, poor and sad, rich and sad and poor and happy. ARIA calculates the gdp per capita and happiness scores and compares it to the global average. After the scenario selection has occurred, ARIA uses these scores to traverse across the inference chain.
It's structure and priority is not random, but decided by the data. Based on the findings, ARIA prioritises each factor with each factor's correlation measurement. The rankings in order are gdp per capita with 0.789, health with 0.742 and social relations with 0.648. It calculates freedom and corruption separately as their contributions are significantly less than the top three with
0.551 and 0.398. Moreover, corruption and freedom don't participate in the inference chain but are called when the inference chain has reached its end. Freedom and corruption are calculated using a separate function. ARIA does not take into account the country's generosity as its correlation measurement is negligible at 0.137. Including generosity, would tamper with the happiness score, as a good generosity score is not equal to a good gdp per capita score, and does not provide much benefit to the country.


## 6. Conclusion

This study found that gdp per capita correlates with happiness scores the most with a correlation measurement of 0.789, rich countries are also seen with higher freedom, health and social relation scores, the global happiness trend has remained flat from 2015 to 2019 and that there were no outliers detected who fell below the 25th percentile of gdp per capita and were above the 75th percentile of happiness score.
The key take away from this study is that gdp per capita is the most important factor in influencing the happiness of a country. Investment in economic development, education and basic services can benefit a country suffering with a low happiness score. This investment can help the country with increased productivity and overall development.


## 7. Limitations

A key limitation in this dataset is that the factors of the happiness index ranging from 2015 to
2017 is based on a hypothetical country named "Dystopia" -- which consists of the worst possible 
scores in each factor. In these years the factors mathematically contribute to the happiness index.
From the years 2018 to 2019 the dataset shifted to independently calculated factors which do not 
sum to the happiness index. I acknowledge this methodological limitation in my study.
Another limitation in this study is the exclusion of the region column from the main dataset, due to inconsistent availability across different years and non-uniform naming conventions.
An attempt was made to incorporate weighted correlation values, Which involved a predicted happiness scores using all the correlation factors as weights. This proved to be extremely inconsistent and was later scrapped.
