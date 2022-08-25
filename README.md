## ZK Proof of Age

- implementation of stack overflow answer for: [ZKP: Prove that >18 while hiding age](https://crypto.stackexchange.com/questions/96232/zkp-prove-that-18-while-hiding-age) 
- Riley wants to buy an fun cocktail at a bar in the United States. The bartender, Bert, needs Riley to prove that they are over 21. Riley loves privacy and doesn't feel the need to share their birthday or age with Bert. 
- Prove: because they're both big nerds, Riley will instead share two signatures, each represented by a hash, with Bert: one representing their age, in days, from 21 years ago (a "proof of age" signature); and one representing their age, in days, at some terminal date T in the distant future (a "terminal age" signature). 
- Verify: using these two signatures, Bert can verify that Riley is over 21. Given the "proof of age" signature, Bert can apply the hash function many times (the number of days between the "proof of age" date and the terminal date) and verify that the result matches the "terminal age" signature. 


### How does it work?

- Start with a public hash function H and a secret private seed _s_.
- Given a person's birthdate _d_, we, as a third party, provide a signed statement. This statement essentially is _s_ hashed _n_ times, where _n_ is the number of days from _d_ to a terminal date in the future, _T_. This is the "terminal age" signature, and it has been signed by a trusted third party (us). For example, maybe Riley's ID card contains their "terminal age" signature, and Bert trusts the issuer of the ID card. 
- Riley keeps _s_ to themselves. With _s_, Riley can generate a valid "proof of age" for any age that they are older than. 
