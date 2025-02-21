"""
Implementing the DFA in Python (Steps/Instructions):

1. Implement the DFA in your favorite programming language:
   - We'll use Python here.

2. The program should read input characters one by one and update its current state
   as specified by the DFA transition function.

3. Once the input string has been read completely, the program should check the current
   state and report "accept" or "reject" based on whether the current state is an accepting
   state.

4. You should implement the transition function δ: Q × Σ → Q and then use it in a loop.
   In each iteration, one character will be read and used to update the current state.

5. Demonstrate that your program works by running it on some test cases:
   - Include cases that should be accepted and cases that should be rejected.
   - Don't forget edge cases (e.g., empty input).
"""


START_STATE = 0
ACCEPT_STATE = 8

def next_state(current_state, symbol):
    """
    Transition function δ: Q × Σ -> Q.
    Given the current_state and the next input symbol,
    returns the next state of the DFA.
    """
    # Matching "helen" part (states 0..5)
    if current_state == 0:   # no match yet
        if symbol == 'h':
            return 1
        else:
            return 0

    elif current_state == 1: # matched "h"
        if symbol == 'e':
            return 2
        elif symbol == 'h':
            return 1  # might be starting "h" again
        else:
            return 0

    elif current_state == 2: # matched "he"
        if symbol == 'l':
            return 3
        elif symbol == 'h':
            return 1
        else:
            return 0

    elif current_state == 3: # matched "hel"
        if symbol == 'e':
            return 4
        elif symbol == 'h':
            return 1
        else:
            return 0

    elif current_state == 4: # matched "hele"
        if symbol == 'n':
            return 5
        elif symbol == 'h':
            return 1
        else:
            return 0

    elif current_state == 5:
        """
        We have matched "helen". Now we look for "ton" in sequence.
        But if we see an 'h' again, we might be starting over "helen" 
        (in case "helen" could appear multiple times).
        """
        if symbol == 't':
            return 6  # start matching "ton"

        else:
            return 5  # reset, we start on this state again, because we already got helen already

    # Matching "ton" part (states 6..8)
    elif current_state == 6: # matched "helen" + "t"
        if symbol == 'o':
            return 7
        elif symbol == 'h':
            return 1  # might be new "helen" starting
        else:
            return 5 # we start from 5 to see if we can get the last name "ton" again

    elif current_state == 7: # matched "helen" + "to"
        if symbol == 'n':
            return 8  # accept
        elif symbol == 'h':
            return 1
        else:
            return 5 #same, retrying to get ton

    elif current_state == 8:
        # Once we've matched "helen" followed by "ton", 
        # we accept everything else (stay in accept state).
        return 8

    # Fallback (shouldn't happen if states are 0..8)
    return 0


def dfa_accepts(input_string):
    current_state = START_STATE
    for char in input_string:
        current_state = next_state(current_state, char)
    return current_state == ACCEPT_STATE

if __name__ == "__main__":
    
    #  Test cases
    test_strings = [
        "aosnaheleniusajbtoniaebuieabn",  # ✅ Accept
        "helehelhelentootona",  # ✅ Accept
        "aosnaheeleniusajbtooniaebuieabn", # ❌ Reject
        "jednwjdniwetonnhdeiuwndihelenuwendiuewndewdewdewfewfkkewjkejncnoiewndi", # ❌ Reject
        "nicwcniwhelenniucnhelentonwuncunckjndtonjksnjcndscjns", #✅ Accept
        "heleeeennnnttonnnn", #❌ Reject
        "", #❌ Reject
        "nicwcniwhe lenn iucnhelen tonwunc unckjndtonjksnjc ndscjns"#✅ Accept
    ]
    
    for test in test_strings:
        print(f"Input: {test} -> {'ACCEPT' if dfa_accepts(test) else 'REJECT'}")

    