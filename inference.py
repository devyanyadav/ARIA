from patterns import build_profile
import pandas as pd 

def infer(country): 
    print(f"\n{'='*55}")
    print(f"  ARIA — Analysing: {country.title()}")
    print(f"{'='*55}\n")
    
    country = country.title()
    df = pd.read_csv("data/processed/merged.csv")

    if df[df["country"] == country].empty:
        print(f"  {country} is not in the database.")
        return

    means, happiness_score, profile = fetch_data(country)
    strength, weakness, moderate = [], [], []

    # Classify GDP
    gdp_score = profile["gdp_per_capita"]["score"]
    if gdp_score >= 4:
        print(f"  [{gdp_score}/5] GDP per capita is high.")
        strength.append(("gdp per capita", gdp_score))
    elif gdp_score == 3:
        print(f"  [{gdp_score}/5] GDP per capita is moderate.")
        moderate.append(("gdp per capita", gdp_score))
    else:
        print(f"  [{gdp_score}/5] GDP per capita is low.")
        weakness.append(("gdp per capita", gdp_score))

    if gdp_score >= 4:
        if happiness_score > means["happiness_score"]:
            wealthy_and_high_happiness(country, profile, strength, moderate, weakness)
        else:
            wealthy_but_unhappy(country, profile, strength, moderate, weakness)
    else:
        if happiness_score < means["happiness_score"]:
            poor_and_low_happiness(country, profile, strength, moderate, weakness)
        else:
            poor_but_happy(country, profile, strength, moderate, weakness)

    conclude(country, strength, moderate, weakness)


def wealthy_and_high_happiness(country, profile, strength, moderate, weakness):
    print(f"\n  {country} is wealthy and scores above average in happiness. Investigating why...\n")

    le_score = profile["life_expectancy"]["score"]
    ss_score = profile["social_support"]["score"]

    if le_score >= 4:
        print(f"  [{le_score}/5] Life expectancy is high — a core driver of happiness here.")
        strength.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is also high — compounds with life expectancy.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate — not a major driver but not a drag.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low — surprisingly, despite overall high happiness.")
            weakness.append(("social support", ss_score))

    elif le_score == 3:
        print(f"  [{le_score}/5] Life expectancy is moderate — not the key driver here.")
        moderate.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high — likely compensating for moderate life expectancy.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate as well.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low.")
            weakness.append(("social support", ss_score))

    else:
        print(f"  [{le_score}/5] Life expectancy is low — investigating what else drives happiness.")
        weakness.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high — a likely substitute driver.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low — some other factor must be driving happiness.")
            weakness.append(("social support", ss_score))

    check_freedom(country, profile, strength, moderate, weakness)
    check_corruption(country, profile, strength, moderate, weakness)


def poor_and_low_happiness(country, profile, strength, moderate, weakness):
    print(f"\n  {country} has low GDP and low happiness. Investigating compounding factors...\n")

    le_score = profile["life_expectancy"]["score"]
    ss_score = profile["social_support"]["score"]

    if le_score >= 4:
        print(f"  [{le_score}/5] Life expectancy is high — not contributing to the low happiness score.")
        strength.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high as well.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low — a contributing factor to unhappiness.")
            weakness.append(("social support", ss_score))

    elif le_score == 3:
        print(f"  [{le_score}/5] Life expectancy is moderate — a partial drag on happiness.")
        moderate.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low — compounds with life expectancy.")
            weakness.append(("social support", ss_score))

    else:
        print(f"  [{le_score}/5] Life expectancy is low — a clear factor behind low happiness.")
        weakness.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high — a relative bright spot.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low — compounds with life expectancy to deepen unhappiness.")
            weakness.append(("social support", ss_score))

    check_freedom(country, profile, strength, moderate, weakness)
    check_corruption(country, profile, strength, moderate, weakness)


def wealthy_but_unhappy(country, profile, strength, moderate, weakness):
    print(f"\n  {country} is wealthy but scores below average in happiness. Investigating why...\n")

    le_score = profile["life_expectancy"]["score"]
    ss_score = profile["social_support"]["score"]

    if le_score >= 4:
        print(f"  [{le_score}/5] Life expectancy is high — not the cause of low happiness.")
        strength.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high too — the problem lies elsewhere.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low — a likely core reason for unhappiness despite wealth.")
            weakness.append(("social support", ss_score))

    elif le_score == 3:
        print(f"  [{le_score}/5] Life expectancy is moderate.")
        moderate.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate — combined with life expectancy, this may explain the happiness gap.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low — compounds with moderate life expectancy.")
            weakness.append(("social support", ss_score))

    else:
        print(f"  [{le_score}/5] Life expectancy is low — a core reason for unhappiness despite wealth.")
        weakness.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low — low life expectancy and low social support together explain the unhappiness.")
            weakness.append(("social support", ss_score))

    check_freedom(country, profile, strength, moderate, weakness)
    check_corruption(country, profile, strength, moderate, weakness)


def poor_but_happy(country, profile, strength, moderate, weakness):
    print(f"\n  {country} has low GDP but scores above average in happiness. Investigating what compensates...\n")

    le_score = profile["life_expectancy"]["score"]
    ss_score = profile["social_support"]["score"]

    if le_score >= 4:
        print(f"  [{le_score}/5] Life expectancy is high — a key reason happiness holds despite low GDP.")
        strength.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high — together with life expectancy, this explains a lot.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low.")
            weakness.append(("social support", ss_score))

    elif le_score == 3:
        print(f"  [{le_score}/5] Life expectancy is moderate.")
        moderate.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high — compensates for moderate life expectancy.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate as well.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low.")
            weakness.append(("social support", ss_score))

    else:
        print(f"  [{le_score}/5] Life expectancy is low.")
        weakness.append(("life expectancy", le_score))
        if ss_score >= 4:
            print(f"  [{ss_score}/5] Social support is high — the primary driver of happiness here.")
            strength.append(("social support", ss_score))
        elif ss_score == 3:
            print(f"  [{ss_score}/5] Social support is moderate.")
            moderate.append(("social support", ss_score))
        else:
            print(f"  [{ss_score}/5] Social support is low.")
            weakness.append(("social support", ss_score))

    check_freedom(country, profile, strength, moderate, weakness)
    check_corruption(country, profile, strength, moderate, weakness)


def check_freedom(country, profile, strength, moderate, weakness):
    score = profile["freedom"]["score"]
    if score >= 4:
        print(f"  [{score}/5] Freedom is high in {country}.")
        strength.append(("freedom", score))
    elif score == 3:
        print(f"  [{score}/5] Freedom is moderate in {country}.")
        moderate.append(("freedom", score))
    else:
        print(f"  [{score}/5] Freedom is low in {country}.")
        weakness.append(("freedom", score))


def check_corruption(country, profile, strength, moderate, weakness):
    score = profile["corruption"]["score"]
    if score >= 4:
        print(f"  [{score}/5] Corruption perception is low in {country} — governance is trusted.")
        strength.append(("corruption", score))
    elif score == 3:
        print(f"  [{score}/5] Corruption perception is moderate in {country}.")
        moderate.append(("corruption", score))
    else:
        print(f"  [{score}/5] Corruption perception is high in {country} — governance is distrusted.")
        weakness.append(("corruption", score))


def conclude(country, strength, moderate, weakness):
    print(f"\n{'─'*55}")
    print(f"  CONCLUSION — {country}")
    print(f"{'─'*55}\n")

    if strength:
        s = ", ".join(f"{name} ({score}/5)" for name, score in strength)
        print(f"  Strengths:   {s}")
    else:
        print(f"  Strengths:   none detected")

    if moderate:
        m = ", ".join(f"{name} ({score}/5)" for name, score in moderate)
        print(f"  Moderate:    {m}")
    else:
        print(f"  Moderate:    none")

    if weakness:
        w = ", ".join(f"{name} ({score}/5)" for name, score in weakness)
        print(f"  Weaknesses:  {w}")
    else:
        print(f"  Weaknesses:  none detected")

    print(f"\n{'='*55}\n")


def fetch_data(country): 
    df = pd.read_csv("data/processed/merged.csv") 
    happiness_score = df[df["country"] == country]["happiness_score"].mean()
    profile = build_profile(country)
    means = df.mean(numeric_only=True)
    return means, happiness_score, profile


infer("south korea")