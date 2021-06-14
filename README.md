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

<img src = 'https://drive.google.com/uc?export=view&id=1YUcTpyJLAg2U6AD9VGLLf3-PiUyuseQ_' width = 60%>

Figure 2 shows performance of CGCNN on the Materials Project database. (a) Histogram representing the distribution of the number of
elements in each crystal. (b) Mean absolute error as a function of training crystals for predicting formation energy per atom using
different convolution functions. The shared area denotes the MAEs of DFT calculations compared with experiments.


<img src = 'https://drive.google.com/uc?export=view&id=1Dz36Ob0pqWAE3ollmld8ESZgI570gPHt' width = 60%>

<img src = 'https://drive.google.com/uc?export=view&id=1CTaG3RBFmDi6kZa7BogS0Ru-zjl1S4Tw' width = 60%>

