def print_what_makes_happy():
    print("""
  WHAT MAKES A COUNTRY HAPPY?
  ───────────────────────────
  GDP per capita correlates most strongly with happiness (0.789), followed by
  health/life expectancy (0.742) and social support (0.648). Freedom (0.551)
  and corruption (0.398) play secondary roles. Generosity shows negligible
  correlation (0.137) and is excluded from analysis.

  Wealthier nations consistently score higher in health, freedom, and social
  support. No country below the 25th percentile of GDP per capita was found
  above the 75th percentile of happiness — confirming GDP as the single most
  important factor in national happiness.
""")


def print_limitations():
    print("""
  LIMITATIONS
  ───────────
  The 2015–2017 dataset anchors factor scores against "Dystopia" — a
  hypothetical worst-case country — meaning factors mathematically sum to the
  happiness index. From 2018–2019, factors are independently calculated and
  do not. This methodological shift is acknowledged.

  The region column was excluded due to inconsistent availability and
  non-uniform naming across years.
""")


def print_header():
    print(f"\n{'═'*55}")
    print(f"  ARIA — World Happiness Report Analysis")
    print(f"{'═'*55}")


def print_footer():
    print(f"{'═'*55}\n")


def run_report(country):
    print_header()
    print_what_makes_happy()
    print_footer()