"""Select a fresh record from synthetic official and secondary fixtures."""

from dataclasses import dataclass
from datetime import date
from typing import Iterable, Literal


@dataclass(frozen=True)
class Observation:
    tier: Literal["official", "secondary"]
    observed: date
    label: str


def select_observation(
    observations: Iterable[Observation], as_of: date, max_age_days: int
) -> Observation | None:
    """Prefer the most recent eligible official record, then secondary."""
    if max_age_days < 0:
        raise ValueError("max_age_days must be nonnegative")
    eligible = [
        record
        for record in observations
        if 0 <= (as_of - record.observed).days <= max_age_days
    ]
    return max(
        eligible,
        key=lambda record: (record.tier == "official", record.observed),
        default=None,
    )


if __name__ == "__main__":
    as_of = date(2026, 1, 10)
    examples = [
        Observation("official", date(2026, 1, 6), "Synthetic exchange record"),
        Observation("secondary", date(2026, 1, 9), "Synthetic secondary record"),
    ]
    for window in (5, 2, 0):
        print(f"{window}-day window: {select_observation(examples, as_of, window)}")
