"""
DESCRIPTION:
The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic.

The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.

Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";
"""

# my solution

def chromosome_check(chromosome):
    # Your code here
    return 'Congratulations! You\'re going to have a son.' if chromosome == 'XY' else 'Congratulations! You\'re going to have a daughter.'

# other solution

# 1

def chromosome_check(chromosome):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')

# 2

def chromosome_check(chromosome):
    return f'Congratulations! You\'re going to have a {"son" if sperm == "XY" else "daughter"}.'

