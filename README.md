# Paper Equity Research Lab

[Portfolio case study](https://scandial-portfolio.scandium.chatgpt.site/project-ai-systems.html) · This repository uses synthetic research examples. The portfolio describes the separate data-ingestion workflow.

A public research-methods repository for building a reproducible equity thesis from sources, assumptions, valuation drivers, and falsification criteria. It is strictly educational and paper-only.

## What it demonstrates

- Separate the company thesis from the stock thesis
- Record sources, dates, assumptions, and uncertainties
- Compare fundamental evidence with a technical-entry gate
- Define what would invalidate the thesis before acting on it
- Review prior predictions against later outcomes

## Important boundary

This is not investment advice, a trading system, or a record of personal holdings. The example is fictional and contains no broker data, account information, current recommendations, or executable orders.

## Start here

- [Research contract](docs/research-contract.md)
- [Scorecard template](docs/scorecard-template.md)
- [Synthetic example](examples/synthetic-company-example.md)

## License

Apache-2.0. See [LICENSE](LICENSE).

## Offline freshness example

Run `python freshness.py` to see official-source priority, an eligible secondary fallback, and rejection when no record is fresh. The fixture uses synthetic names and fixed dates. Run `python -m unittest -v` to check the rules.
