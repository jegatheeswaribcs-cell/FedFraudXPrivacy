FedFraud-X privacy accounting files

Files:
- privacy_accounting.py: computes cumulative epsilon after each of 34 rounds.
- epsilon_by_round_template.csv: blank template for the 34-round report.

Run:
    pip install opacus
    python privacy_accounting.py

Important:
The paper specifies noise multiplier 1.12, delta 1e-7, and 34 rounds, but
does not specify clipping norm, sampling method/rate, or provide original code.
The script uses illustrative assumptions (L2 clipping norm 1.0 and Poisson
sampling rate 0.01). Replace these with the actual training configuration.
The final epsilon must be checked; do not claim it equals 2.00 unless verified.

GitHub:
I cannot create or publish a repository on your behalf from this environment.
Create a new GitHub repository, then upload privacy_accounting.py,
epsilon_by_round_template.csv, and this README. Your repository link will be:
https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
