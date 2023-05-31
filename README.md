# JaNLI (Japanese Adversarial Natural Language Inference)
- repository for our BlackboxNLP2021 paper "Assessing the Generalization Capacity of Pre-trained Language Models through Japanese Adversarial Natural Language Inference"
- **You can use JaNLI at [huggingface dataset](https://huggingface.co/datasets/hpprc/janli)!**

## Install Tools
Python3.6
pandas

## Dataset Creation
```
$ cd JaNLI
$ python scripts/generate.py
```
`data/JaNLI_template.csv` is a template for generating a JaNLI dataset and `janli.tsv` is a generated JaNLI dataset.

The fields in this file are:
- ``sentence_A_Ja``: The premise
- ``sentence_B_Ja``: The hypothesis 
- ``entailment_label_Ja``: The correct label for this sentence pair (either ``entailment`` or ``non-entailment``); in our setting, ``non-entailment`` = neutral + contradiction)
- ``heuristics``: The heuristics (structural pattern) tag. The tags are: subsequence, constituent, full-overlap, order-subset, and mixed-subset. 
- ``number_of_NPs``: The number of noun phrase in a sentence.
- ``semtag``: The linguistic phenomena tag.
- ``split``: The train/test split.


## Citation
If you use this dataset and code in any published research, please cite the following:
* Hitomi Yanaka, Koji Mineshima, [Assessing the Generalization Capacity of Pre-trained Language Models through Japanese Adversarial Natural Language Inference](https://aclanthology.org/2021.blackboxnlp-1.26/), Proceedings of the 2021 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP (BlackboxNLP2021), 2021.

```
@InProceedings{yanaka-EtAl:2021:blackbox,
  author    = {Yanaka, Hitomi and Mineshima, Koji},
  title     = {Assessing the Generalization Capacity of Pre-trained Language Models through Japanese Adversarial Natural Language Inference},
  booktitle = {Proceedings of the 2021 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP (BlackboxNLP2021)},
  year      = {2021},
}
```

## Contact
For questions and usage issues, please contact hyanaka@is.s.u-tokyo.ac.jp .

## License
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
