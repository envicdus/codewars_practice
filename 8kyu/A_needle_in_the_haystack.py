'''
DESCRIPTION:
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
'''

# my solution

def find_needle(haystack):
    # your code here
    return f"found the needle at position {haystack.index('needle')}"

# other solution

# 1

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

# 2

def find_needle(haystack):
	return 'found the needle at position {}'.format(haystack.index('needle'))

# 3

def find_needle(haystack):
    return 'found the needle at position %d' % haystack.index('needle')