# [Exploring Physiological Correlates of Visual Complexity Adaptation: Insights from EDA, ECG, and EEG Data for Adaptation Evaluation in VR Adaptive Systems](./chiossi2023lbw.pdf)

Francesco Chiossi, Changkun Ou, Sven Mayer<br/>
In Extended Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems (CHI EA ’23), April 23–28, 2023, Hamburg, Germany. ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3544549.3585624

Physiologically-adaptive Virtual Reality can drive interactions and adjust virtual content to better fit users’ needs and support specific goals. However, the complexity of psychophysiological inference hinders efficient adaptation as the relationship between cognitive and physiological features rarely show one-to-one correspondence. Therefore, it is necessary to employ multimodal approaches to evaluate the effect of adaptations. In this work, we analyzed a multimodal dataset ( EEG, ECG, and EDA) acquired during interaction with a VR-adaptive system that employed EDA as input for adaptation of secondary task difficulty. We evaluated the effect of dynamic adjustments on different physiological features and their correlation. Our results show that when the adaptive system increased the secondary task difficulty, theta, Beta, and phasic EDA features increased. Moreover, we found a high correlation between theta, alpha and beta oscillations during difficulty adjustments. Our results show how specific EEG and EDA features can be employed for evaluating VR adaptive systems.

![](teaser.jpg)

## Full Paper

The paper is available in [chiossi2023lbw.pdf](./chiossi2023exploring.pdf).

## Dataset

The original dataset is taken from Francesco Chiossi, Robin Welsch, Steeven Villa, Lewis Chuang, and Sven Mayer. 2022. Virtual Reality Adaptation using Electrodermal Activity to Support User Experience. In the DaRus Open Data Platform. https://doi.org/10.18419/darus-2820.

To run the provided jupyter notebook, place the dataset (`DataSet.7z`) in [./data](./data) folder and unzip it. The folder structure should look like:

```bash
├── 1.eda.ipynb
├── 2.ecg.ipynb
├── 3.eeg.ipynb
├── 4.behavior.ipynb
├── 5.correlation.ipynb
├── data
│   ├── ID0-adaptation.csv
│   ├── ID0-ECG.csv
│   ├── ID0-EDA.csv
│   ├── ID0-EEG.csv
│   ├── ID0-feedback.csv
│   ├── ID0-flow.csv
│   ├── ID0-sphere.csv
│   ├── ID0-state.csv
│   ├── ID0-visitorCount.csv
│   ├── ID0-visitor.csv
│   ├── ID10-adaptation.csv
│   ├── ...
│   └── ID9-visitor.csv
├── LICENSE
└── README.md
```

## Figures

All figures appearing in the paper are placed in [./figures](./figures) and are generated by the provided Jupyter Notebooks.

## Analysis

The included Jupyter Notebooks for the analysis reproduces the entire Section 3 of the paper:

- [1.eda.ipynb](./1.eda.ipynb): EDA analysis that reproduces Section 3.1.1 and Figure 1a.
- [2.ecg.ipynb](./2.ecg.ipynb): ECG analysis that reproduces Section 3.1.2 and Figure 1b.
- [3.eeg.ipynb](./3.eeg.ipynb): EEG analysis that reproduces Section 3.1.3 and Figure 2 and Figure 3.
- [4.behavior.ipynb](./4.behavior.ipynb): Behavior performance that reproduces Section 3.1.4 and Figure 4.
- [5.correlation.ipynb](./5.correlation.ipynb): Correlation analysis that reproduces Section 3.2 and Figure 5.

## Contribute

The easiest way to contribute is to provide feedback! We would love to hear what you think. Please write to [francescochiossi93@gmail.com](mailto:francescochiossi93@gmail.com) and [research@changkun.de](mailto:research@changkun.de) for closer communication.

## Licenses and Citation

Copyright &copy; 2023. [LMU Munich Media Informatics Group](https://www.medien.ifi.lmu.de). All rights reserved.

The [data](./data) itself, available in [Creative Commons Public Domain Dedication (CC-4.0)](https://creativecommons.org/licenses/by/4.0/), represented the results from consented anonymous participants and was collected by Francesco Chiossi. The contained "source code" (i.e., Python scripts and Jupyter Notebooks) of this work is made available under the terms of [GNU GPLv3](./LICENSE).

If you find our research is helpful, we would appreciate a citation via:

```bibtex
@inproceedings{chiossi2023lbw,
	title        = {{Exploring Physiological Correlates of Visual Complexity Adaptation: Insights from EDA, ECG, and EEG Data for Adaptation Evaluation in VR Adaptive Systems}},
	author       = {Chiossi, Francesco and Ou, Changkun and Mayer, Sven},
	year         = 2023,
	booktitle    = {ACM Conference on Human-Computer Interaction},
	publisher    = {Association for Computing Machinery},
	address      = {Hamburg, Germany},
	series       = {CHI '23 Extended Abstracts},
	doi          = {10.1145/3544549.3585624},
}
```
