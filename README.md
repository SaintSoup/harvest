# Harvest

## Table of contents

* [General information](#general-info)
* [Requirements](#requirements)
* [Directory Hierarchy](#directory-hierarchy)
* [References](#references)

## General Information

About the Project
-----------------

This project aims to optimize the performance of a near-limits [1] energy harvester [2] by implementing a prediction model to serve as the basis for a switching decision in the device to enhance the entire system's dynamic performance. It was done in the initial stages by Salim Khemira, under the supervision of [Prof. Dimitri Galayko](https://scholar.google.fr/citations?user=_u3mqkcAAAAJ&hl=fr) of Sorbonne University - LIP6 laboratory (Paris).

Stages
------

The project comprises two stages:

* Conception and training of models: 
The training sequences range from ambient vibrations acquired through already-present accelerometers in smartphones or publically-available data available through the Real Vibrations project from the Physics department of the University of Perugia [link](https://realvibrations.nipslab.org/).

* Implementation of the trained model on hardware: 
Initially, the goal was to research the implementation of such models on neuromorphic circuits through neural networks' direct implementation. Notwithstanding, the initial project, due to mitigating circumstances, did not reach this point. The current effort is to migrate the initial files to a Tensorflow API, thus unifying the interface, and then to implement the models through the Tensorflow Lite API on embedded devices (The first tests will are run on Arduino Nano V3.0 (ATmega328P) and an ESP32 WROOM 32)

Timeline
--------------------

* February - June 2020: Acquisition of theoretical background and initial work on the data and models. Very much guided by the work of Aileen Nielsen [3] and Aurélien Géron [4]. Promising results, but the code was patchy in places

* November 2020 -: Starting the migration from MXNET Gluon to Tensorflow (Primarily Keras), followed by the implementation on microcontrollers [5] [6]. The models are also being finetuned with a rerun over optimizers to finetune performance [7].  

## Requirements

For the environment specifications, please refer to the Pipfile.The working environment is on Linux Mint Ulyana, with Python  3.8.5 as well as pipenv 2020.11.4 :

`$ sudo apt-get update`
`$ sudo apt install build-essential zlib1g-dev \`
`libncurses5-dev libgdbm-dev libnss3-dev \`
`libssl-dev libreadline-dev libffi-dev curl`
`$sudo apt-get install pipenv`

Once pipenv is installed, the following commands -run in the project directory- `pipenv install`  `pipenv shell`, will activate the environment.

## Directory Hierarchy

In case of discrepancies between the information cited below and the repository, the reason would be that the file is still offline and has not been pushed yet.

* `/sources` : Different sources from the project
* `/build` : Contains the saved models with checkpoints
* `/exports` : Contains the exported models ready for implementation

## References

[1] A. Haji Hosseinloo, K. Turitsyn. "Fundamental Limits to Nonlinear Energy Harvesting
" [link](https://dspace.mit.edu/handle/1721.1/100750)  
[2] A. Karami, J. Juillard, E. Blokhina, P. Basset, D. Galayko. "Electrostatic Near-Limits Kinetic Energy
Harvesting from Arbitrary Input Vibrations" [link](https://arxiv.org/abs/2002.07086)  
[3] A. Nielsen "Practical Time Series Analysis: Prediction with Statistics and Machine Learning, ISBN 13: 9781492041603"  
[4] A. Géron "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems, ISBN 13: 9781492032595"  
[5] J. Moolayil "Learn Keras for Deep Neural Networks, ISBN 13: 9781484242391"  
[6] P. Wardenm D. Situnayake "TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontroller, ISBN 13: 9781492051992"  
[7] M.J. Kochenderfer, T.A. Wheeler "Algorithms for Optimization, ISBN 13: 9780262039420"  