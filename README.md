# One-Shot Data Preprocessing

The collection of raw and generated (with transformations) images from the original Omniglot Dataset.

## Setup

Run the following command to initialize the following submodules.

```sh
git submodule update --init
```

#### Submodules

- [brendenlake/omniglot: Omniglot data set for one-shot learning](https://github.com/brendenlake/omniglot).

## Usage

List of original Omniglot datasets.

- `images_background_small1`
- `images_background_small2`
- `images_background`
- `images_evalution`
- `strokes_background_small1`
- `strokes_background_small2`
- `strokes_background`
- `strokes_evalution`

To run preprocessing on a `<dataset>` from the list, issue the following command to generate the transformed data to `<output_dataset>`.

```sh
sh scripts/augment_wrapper.sh <dataset> <output_dataset>
```

**Ensure that `<dataset>` and `<output_dataset>` do not have the same name.**

## References

[Lake, B. M., Salakhutdinov, R., and Tenenbaum, J. B. (2015). Human-level concept learning through probabilistic program induction.](http://www.sciencemag.org/content/350/6266/1332.short) _Science_, 350(6266), 1332-1338.

- Update: [Lake, B. M., Salakhutdinov, R., and Tenenbaum, J. B. (2019). The Omniglot Challenge: A 3-Year Progress Report.](https://arxiv.org/abs/1902.03477) Preprint available on arXiv:1902.03477.
