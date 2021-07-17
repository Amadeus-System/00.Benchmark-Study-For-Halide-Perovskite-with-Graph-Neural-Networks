# 00.Crystal_Graph_Convolutional_Neural_Network
Repository for my CGCNN research record

## Abstract:
The use of machine learning methods for accelerating the design of crystalline materials usually requires
manually constructed feature vectors or complex transformation of atom coordinates to input the crystal
structure, which either constrains the model to certain crystal types or makes it difficult to provide chemical
insights. Here, we develop a crystal graph convolutional neural networks framework to directly learn material
properties from the connection of atoms in the crystal, providing a universal and interpretable representation
of crystalline materials. Our method provides a highly accurate prediction of density functional theory
calculated properties for eight different properties of crystals with various structure types and compositions
after being trained with 104 data points. Further, our framework is interpretable because one can extract the
contributions from local chemical environments to global properties. Using an example of perovskites, we
show how this information can be utilized to discover empirical rules for materials design

The following Figure explains that how the structure of solid state physics can be transformed to a Graph structure.
<img src = 'https://drive.google.com/uc?export=view&id=1nC5Dv7eqk04dCpp-lsw0Bysh6onyN2Qi' width = 60%>

FIG. 1. Illustration of the crystal graph convolutional neural
networks. (a) Construction of the crystal graph. Crystals are
converted to graphs with nodes representing atoms in the unit cell
and edges representing atom connections. Nodes and edges are
characterized by vectors corresponding to the atoms and bonds in
the crystal, respectively. (b) Structure of the convolutional neural
network on top of the crystal graph. R convolutional layers and
L1 hidden layers are built on top of each node, resulting in a new
graph with each node representing the local environment of each
atom. After pooling, a vector representing the entire crystal is
connected to L2 hidden layers, followed by the output layer to
provide the prediction.

<br>
FIG. 2. Performance of CGCNN on the Materials Project
database [11]. (a) Histogram representing the distribution of
the number of elements in each crystal. (b) Mean absolute error as
a function of training crystals for predicting formation energy per
atom using different convolution functions. The shaded area
denotes the MAEs of DFT calculations compared with experiments [28]. (c) 2D histogram representing the predicted formation per atom against DFT calculated value. (d) Receiver
operating characteristic curve visualizing the result of metalsemiconductor classification. It plots the proportion of correctly
identified metals (true positive rate) against the proportion of
wrongly identified semiconductors (false positive rate) under
different thresholds.

<img src = 'https://drive.google.com/uc?export=view&id=1Dz36Ob0pqWAE3ollmld8ESZgI570gPHt' width = 60%>

<img src = 'https://drive.google.com/uc?export=view&id=1CTaG3RBFmDi6kZa7BogS0Ru-zjl1S4Tw' width = 60%>

