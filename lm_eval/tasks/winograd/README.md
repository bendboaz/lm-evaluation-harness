# Winograd Hebrew

### Paper Substitute

Translated by Vered Shwartz, see [her research page](https://www.cs.ubc.ca/~vshwartz/research.html).

Based on the original [Winograd Schema challenge](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html).

#### The WinoGrande dataset - comparison
This dataset is not directly compatible with the `winogrande` dataset (`allenai/winogrande`), due to different dataset columns. However, the evaluation schema (processing and metrics) are based off of this original implementation.

The WinoGrande dataset can be found in the `lm_eval` implementation as the `winogrande` task.


### Groups and Tasks

#### Groups

No groups defined for this evaluation.

#### Tasks

The following tasks evaluate languages in the Winograd dataset using loglikelihood-based multiple-choice scoring:
- `winograd_heb`

Currently only implementing the 0-shot multiple-choice method, not a prompting-based solution.


### Checklist

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation?
    * [ ] Yes, original implementation contributed by author of the benchmark

If other tasks on this dataset are already supported:
* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?
