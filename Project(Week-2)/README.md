## Part 2 - RSA Digital Signatures

This part of the project includes a script called ```sign.py``` that takes in a the name of a text file as input and prints out the digital signature of that file as follows:
- It generates the SHA-256 hash of the file (as bytes).
- Then it creates a random semiprime `N` to be used in the RSA digital signature.
- Then it signs the hash using RSA digital signature with `N` above and `e = 65537`.
- Finally, it returns `(N, e)` as a tuple and the the signature (in hex)


A separate script called ```verifier.py``` is also created that takes in tha name of a text file, N, e, and a signature in hex and verifies the digital signature of the contents of the text file and returns ```accept``` or ```reject``` depending on whether the signature is valid or not.

### Usage
For running the signature signing program i.e. sign.py, use the following command:
```
python3 sign.py
```
For running the signature verification program i.e. verifier.py, use the following command:
```
python3 verifier.py
```

