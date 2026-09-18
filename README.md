# Recall Checker

The best product in the recall pile is not another alert feed. It is the thing that reads the label on the box still sitting on the counter and tells you, this week, whether that lot is in a live file.

The notice exists. The household never matches it to the object they already bought. That gap is the product.

## How it works

1. Photograph the back of the package, the VIN plate, or the receipt that still has the UPC.
2. The checker pulls the identifier — UPC/GTIN + lot, establishment number, or VIN.
3. It matches against mirrored agency files: CPSC, FDA enforcement, USDA-FSIS, NHTSA campaigns.
4. Verdict in thirty seconds: **match** (agency page, date, class, plus a drafted next step), **no match**, or **need a clearer lot line**.

No account. No seat fee to see the first answer.

## The gate

A lot-code match is not a diagnosis and not a filing. Returns, dealer repairs, warranty claims — the model drafts the next step, a person owns the send. Same rule this shop runs everywhere: irreversible steps need a human signer.

## Quickstart

```bash
pip install -r requirements.txt
python src/checker.py --photo path/to/label.jpg
```

## Build order

- **Week 1–2:** one checker. Photo in, match or no-match out. Start with UPC + lot, or VIN — not both.
- **Week 3–4:** a next-step draft — return script, dealer scheduling note, warranty email — with a human signer.
- **Month 2:** the second identifier in the same customer's drawer.
- **Month 3:** the first ugly internal scoreboard. Brands, plants, VIN prefixes that keep showing up. That scoreboard is the seed of the B2B product.

If you cannot get a stranger to photograph one label this week, you do not have a company. You have a thesis.

## What this is not

Not a medical diagnostic. Not a class-action mill. Not four micro-SaaS names for four agencies — one matcher, one map.

---

Part of the [idea-mill series](https://tygartmedia.com/the-best-recall-product-reads-the-label-before-you-throw-the-box-away/). MIT licensed.
