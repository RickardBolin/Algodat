import sys
import fileinput


def main():
    women, men = parse_input()
    matches = gale_shapley(women, men)
    for pairs in matches:
        print(pairs)


def parse_input():
    # Read the number of people from the first line of the input
    N = int(sys.stdin.readline())
    # Create arrays to store preferences for the men and women
    men = [None]*N
    women = [None]*N
    preferences = []
    for line in fileinput.input():
        preferences += (list(map(int, line.split(" "))))
        if len(preferences) >= N+1:
            # Split into two parts, the latter of which we reuse for then next person
            chunk, preferences = preferences[:N+1], preferences[N+1:]

            if women[chunk[0] - 1] is None:
                # Invert preference list
                inv_list = [None] * N
                for i in range(1, N+1):
                    inv_list[chunk[i]-1] = i
                women[chunk[0]-1] = [chunk[0]] + inv_list
            else:
                men[chunk[0] - 1] = chunk
    return women, men


def gale_shapley(women, men):
    matches = [None]*len(women)
    matched_men = {}
    while len(men) is not 0:
        # Take out the first man
        m = men.pop(0)  # POP(0) IS DUMB, CHANGE TO DEQUE OR SOMETHING!
        # Get his preferred woman and remove her from the preferences
        pref_w = m.pop(1) - 1 # POP(0) IS DUMB, CHANGE TO DEQUE OR SOMETHING!
        # If the woman doesnt have a partner, make new pair and add to matches
        if matches[pref_w] is None:
            matches[pref_w] = m[0]
            matched_men[m[0]] = m
        # If the woman prefers the new man to her current husband
        elif women[pref_w][matches[pref_w]] > women[pref_w][m[0]]:
            # Handle paperwork of previous husband
            old_man = matches[pref_w]
            men.append(matched_men.pop(old_man))
            # Handle paperwork of new husband
            matches[pref_w] = m[0]
            matched_men[m[0]] = m
        # Let the man return to fight another day
        else:
            men.append(m)
    return matches


if __name__ == "__main__":
    main()
