"""
Proposed RDP privacy-accounting script for the FedFraud-X paper.

Install:
    pip install opacus

Important:
- The paper reports noise_multiplier=1.12, delta=1e-7, and 34 rounds.
- The paper does NOT specify clipping norm or sampling method/rate.
- CLIPPING_NORM=1.0 and SAMPLE_RATE=0.01 below are example assumptions,
  not values reported by the paper.
- The computed epsilon trajectory may NOT end at epsilon=2.00.
  Verify the configuration against the actual training pipeline.
"""

import csv
from opacus.accountants import RDPAccountant

CLIPPING_NORM = 1.0       # Example only; replace with actual training value
SAMPLE_RATE = 0.01        # Example Poisson sampling rate; replace as needed
NOISE_MULTIPLIER = 1.12   # Reported in the paper
DELTA = 1e-7              # Reported in the paper
ROUNDS = 34               # Reported in the paper
OUTPUT_CSV = "epsilon_by_round.csv"


def main():
    if CLIPPING_NORM <= 0:
        raise ValueError("CLIPPING_NORM must be positive.")
    if not 0 < SAMPLE_RATE <= 1:
        raise ValueError("SAMPLE_RATE must be in (0, 1].")

    accountant = RDPAccountant()
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["round", "epsilon", "delta"]
        )
        writer.writeheader()

        for round_number in range(1, ROUNDS + 1):
            accountant.step(
                noise_multiplier=NOISE_MULTIPLIER,
                sample_rate=SAMPLE_RATE,
            )
            epsilon = accountant.get_epsilon(delta=DELTA)
            writer.writerow({
                "round": round_number,
                "epsilon": f"{epsilon:.8f}",
                "delta": f"{DELTA:.1e}",
            })
            print(f"Round {round_number:02d}: epsilon={epsilon:.8f}")

    print(f"Saved cumulative privacy budgets to {OUTPUT_CSV}")
    print("Note: clipping norm affects training, but is not an input to "
          "RDPAccountant.step(); ensure it matches the training pipeline.")


if __name__ == "__main__":
    main()
