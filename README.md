# Word Frequency Database from Hungarian Webcorpus 2

Search using web interface / SQL [here](https://hungarian-word-frequencies-production.up.railway.app/frequencies/words).

Plz cite:

```
Péter, Rácz. (2025). Word frequency list from the Hungarian Webcorpus (Version 1.0) [Software/Data]. Zenodo. [https://doi.org/10.5281/zenodo.17508385](https://doi.org/10.5281/zenodo.17508385)
```

```bibtex
@software{racz2025hungarian,
  author       = {Rácz, Péter},
  title        = {Word frequency list from the Hungarian Webcorpus},
  year         = {2025},
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.17508385},
  url          = {https://doi.org/10.5281/zenodo.17508385}
}
```

Original [here](https://hlt.bme.hu/en/resources/webcorpus2).

## Dictionary

| Column | Description |
|--------|-------------|
| form | word form, orthographic |
| lemma | word lemma, orthographic |
| xpostag | form pos tag |
| freq | form raw frequency |
| corpus_size | corpus size (total frequency) |
| lemma_freq | lemma raw frequency |
| lfpm10 | log10 form frequency per million |
| llfpm10 | log10 lemma frequency per million |
| form_length | nchar form |
| form_syl_count | n vowels form |
| lemma_length | nchar lemma |
| lemma_syl_count | n vowels lemma |
| hunspell | does the hunspell spelling dictionary contain the lemma? |
