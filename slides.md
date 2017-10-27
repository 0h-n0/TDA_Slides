name: inverse
layout: true
class: center, middle, inverse
---
# Introduciton to TDA
#### 28/10/2017
#### Koji Ono

--
 
#### My major was Biology.

--

#### So I'm not familiar with Mathmatics...
---
layout:false
name: agenda

## Agenda

### 1. What is TDA? (Overview of TDA)

### 2. Application.

### 3. Homology.

### 4. Persistent Homology.

### 5. Let's caluculate Homology.

### 6. References

---
## 1. What is TDA? (Overview of TDA)

**TDA** stands for **T**oplogical **D**ata **A**nalysis

- ".red.bold[Topological]" means ...
    - Differential topology.
    - Geometric topology.
    - Homotopy theory.
    - Homology.
    - etc.

--

These mathematical methods are for analyzing **phase**. 

--

To find out "Topological Invariant.
    

---
## 1. What is TDA? (Overview of TDA)

.emphasize[One of the machine learning method.]

--

.left-column[
### Supervised
- Nerural Network
- SVN
- Bayeasian
- etc.

]

--

.right-column[
###Unsupervised
- PCA
- Clustering(hierachical)
- Clustering(non-hirerarchical)
- etc.
]

???
![Default-aligned image](https://i.ytimg.com/vi/TDL8WbnBvyo/hqdefault.jpg)

--

**TDA** is similar to Clustering(non-hirerarchical method)

---
## 1. What is TDA? (Overview of TDA)

#### Random data

.center[
<video preload="auto" width="70%" height="auto" data-setup="{}" loop controls><source src="https://github.com/0h-n0/TDA_Slides/blob/images/src/random.mp4?raw=true" type="video/mp4" /></video>
]

---
## 1. What is TDA? (Overview of TDA)

#### Circle data

.center[
<video preload="auto" width="70%" height="auto" data-setup="{}" loop controls><source src="https://github.com/0h-n0/TDA_Slides/blob/images/src/circle.mp4?raw=true" type="video/mp4" /></video>
]


---
## 2. Application.

There are a lot of Application of TDA in Biology.

* Sensor-network coverage
* Proteins
* 3-dimensional sturecture of DNA
* Development of cells
* robotics
* signals in images
* ... etc

TDA is based on .red[Homology] which is defined in mathematical Group theory.

---
## 3. Homology.

Homology is a way to uncover k-dimensional "holes" in  a simplical complex.

###  Definition of k-dimensional Homology Group.

$$H_k(K) = Z_k(K) / B_k(K)$$

#### k-cycles

$$
Z_k := ker ( \partial_k : C_k \to C(k+1)) \\ 
$$

#### k-boundaries

$$
\begin{array}
B_k := Im ( \partial(k+1) : C(k+1) \to C_k) \\ 
\end{array}
$$

---
## 3. Homology.

It is too difficult to understand all of previous equations.

--
...

--
...

--
...

--

We want to know how to calculate it and the meaning of k-dimensional homology

--

$$
\begin{array}
\beta_k(K) := dim H_p(K) = dim(ker(\partial_p) - dim(im(\partial(p+1)))
\end{array}
$$
is called pth Betti number of K. pth Betti number 'count' the number of p-holes.

---
## 3. Homology.

####  Simplical Complex

![image](http://raw.githubusercontent.com/0h-n0/TDA_Slides/images/src/simplical_complex.png)
###### Ref:『Topological Data Analysis of Biological Aggregation Models』(2015) C. M. Topaz et. al.

- Cach complex
- Vietoris-Rips complex
- etc..

---

## 4. Persistent Homology.

###  Definition of Persistent Homology Group.

For finite filltration of simple complex

    
$${\mathbb K} : \subset K^0 \subset K^1 \cdots \subset K^t \subset \cdots$$

, k-dimension Persistent Homology Group is


$$PH_k({\mathbb K}) = Z_k({\mathbb K}) / B_k({\mathbb K})$$


---
## 4. Persistent Homology.

#### Barcode

![image](http://raw.githubusercontent.com/0h-n0/TDA_Slides/images/src/barcode_image.png)

###### Ref:『A roadmap for the computation of persistent homology』(2015) Nina et. al.

---
## 5. Let's caluculate low-dimension Homology.

$$
\begin{array}
\\\C_{1+2} = \\{a,b,c,d,e\\} \\\
C_2 = \\{[a,b]\\} \\\
K = \\\C_{1+2} \cup C_2
\end{array}
$$

![image](http://raw.githubusercontent.com/0h-n0/TDA_Slides/images/src/example_0.1.png)

---
$$C_1$$

$$
A = \left(
\begin{array}{ccc}
    a & b & c \\\
    d & e & f \\\
    g & h & i
\end{array}\right)
$$
---

## 5. Let's caluculate low-dimension Homology.

$$
\begin{array}

CCC CCC_1 = \{a,b,c,d,e\} \\
C_2 = \{[a,b], [c,d]\}
\end{array}
$$


![image](http://raw.githubusercontent.com/0h-n0/TDA_Slides/images/src/example_0.2.png)

---

## 5. Let's caluculate low-dimension Homology.

$$
\begin{array}
C_1 = \{a,b,c,d,e\} \\
C_2 = \{[a,b],[a,d],[b,c],[c,d],[c,e]\} \\
C_3 = \{[a,d,c]\}
\end{array}
$$


![image](http://raw.githubusercontent.com/0h-n0/TDA_Slides/images/src/example_0.3.png)

---
## 6. References 1
### Group Theory
-  https://www.youtube.com/watch?v=VdLhQs_y_E8
    - Harvard lecture videos about abstract algebra on Youtube.
- 『代数学１、２、３』　雪江　明彦著
    - Japanese good reference book about abstract algebra.
---
## 6. References 2
### Homology

- https://www.youtube.com/watch?v=EA1FFtTGAfw
    - American university's lecture videos about introduction and application of homology on Youtube. 
- 『Computational Homology (Applied Mathematical Sciences)』(2004)
    - There are a lot of information that homology is applied for image data.
- 『Elementary Applied Topology』(2014)
    - It is said that this book is good, but I don't know well.
- 『計算で身につくトポロジー』 阿原 一志著
    - This is one of the book I want.

---
## 6. References 3
### Persist Homology
- 『Topological Data Analysis of Biological Aggregation Models』(2015) C. M. Topaz et. al.
    - Nice introduction.
- 『タンパク質構造とトポロジー ―パーシステントホモロジー群入門― (シリーズ・現象を解明する数学)』　平岡 裕章著
    - Japanese book about application of persistent homology to biology.
- 『A roadmap for the computation of persistent homology』(2015) Nina et. al.
    - Good review.

---
## 7. Book list

- コホモロジーのこころ
- ホモロジー代数　河田
- 代数的トポロジー
- トポロジー　田村
