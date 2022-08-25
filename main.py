# imports

### TRUSTED THIRD PARTY

def generate_terminal_hash(birthdate):
    """
    Input: a birthdate in the format MM/DD/YYYY
    Output: a private seed s and a "terminal date" signature.
    """
    pass


### PROVER

def generate_proof_of_age(private_seed, minimum_age):
    """
    Input:
        - private seed s
        - minimum age, e.g. 21
    Output: a proof of age signature
    """
    pass


### VERIFIER

def verify(minimum_age, proof_of_age, terminal_signature):
    """
    Inputs:
    - a minimum age, e.g. 21
    - a proof of age signature, provided by the prover
    - a terminal signature, signed by a trusted third party

    Returns:
    - True if the verification passes, i.e. the hashing the proof of age
        signature x times results in the terminal signature
    - False otherwise
    """
    pass

