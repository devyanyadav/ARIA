import pandas as pd 



def build_profile(country):
    df = pd.read_csv("data/processed/merged.csv")

    country = country.title()

    country_avg = df[df["country"] == country].mean(numeric_only=True) #variable for country averages

    country_average_factors = {
        "gdp_per_capita" : country_avg["gdp_per_capita"],
        "life_expectancy" : country_avg["life_expectancy"],
        "social_support" : country_avg["social_support"],
        "freedom" : country_avg["freedom"],
        "corruption" : country_avg["corruption"],
        "generosity" : country_avg["generosity"]
    }
    
    #global average mean and std 
    means = df.mean(numeric_only=True)
    std = df.std(numeric_only=True)
    


    # comparing each factor with the global average
    factor_strength = {}
    for factor,value in country_average_factors.items() :
        if value > means[factor] +(std[factor]*1.5) : 
            factor_strength[factor] = { "label" : "very_strong", "score" : 5}
        elif value > means[factor] +(std[factor]*0.5) : 
            factor_strength[factor] = { "label" : "strong", "score" : 4}
        elif value > means[factor] - ( std[factor]*0.5): #and value<means[factor] - (std[factor]*1.5): 
            factor_strength[factor] = { "label" : "moderate", "score" : 3}

        elif value > means[factor] - ( std[factor]*1.5): 
            factor_strength[factor] = { "label" : "weak", "score" : 2}
        else : 
            factor_strength[factor] = { "label" : "very weak", "score": 1}


    return factor_strength

     





